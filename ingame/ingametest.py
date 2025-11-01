from typing import Optional


class Process:
    def __init__(self):
        pass

    def update(self) -> None:
        pass


class Renderer:
    objs: list[Process]

    def __init__(self, objs: Optional[list[Process]] = None):
        if objs is None:
            objs = []

        self.objs = objs

    def run(self):
        while True:
            for obj in self.objs:
                obj.update()

    def add(self, proc: Process) -> None:
        self.objs.append(proc)
