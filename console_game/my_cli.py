from typing_extensions import Callable, Self


class Argument:
    def __init__(self: Self, name: str, required: bool = False, argtype: type = str, default: str = ""):
        self.name: str = name
        self.required: bool = required
        self.argtype: type = argtype
        self.default: str = default


class Command:
    def __init__(self: Self, name: str, func: Callable) -> None:
        self.name: str = name
        self.func: Callable = func
        self.args: list[Argument] = []

    def add_argument(self: Self, arg: Argument) -> None:
        self.args.append(arg)

    def sort_args(self: Self) -> tuple[list[Argument], list[Argument]]:
        required = []
        optional = []
        for i in self.args:
            if i.required:
                required.append(i)
            else:
                optional.append(i)
        return required, optional

    def __call__(self: Self, *args):
        try:
            kwargs = {}
            required, optional = self.sort_args()
            mylist = [*args]
            for i in required:
                kwargs[i.name] = mylist.pop(0)
            for i in mylist:
                kwargs[optional.pop(0).name] = i
            self.func(**kwargs)
        except BaseException as e:
            print(e)
            return 1
        else:
            return 0


def command(name: str) -> Callable:
    def wrapper(func: Callable):
        return Command(name=name, func=func)

    return wrapper


def argument(*args, **kwargs):
    def wrapper(func: Command):
        func.add_argument(Argument(*args, **kwargs))
        return func

    return wrapper

class CLI(dict[str, Command]):
    def __new__(cls: type[Self]) -> Self:
        return super().__new__(cls)
    def add_command(self, func: Command):
        self[func.name] = func
        return func
    def __call__(self, limit: int = -1, prompt: str = ">>> ", sep: str = " ") -> int:
        try:
            result = 0
            i = 0
            while i < limit:
                args = input(prompt).split(sep)
                result += self[args[0]](args[1:])
            return result
        except BaseException as e:
            print(e)
            return -1

def cli() -> CLI:
    return CLI()