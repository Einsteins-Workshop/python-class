from typing import Optional
from enum import Enum
from pprint import pprint


X = 'O'
O = 'O'


board: list[Optional[str]] = [None, None, None,
                                None, None, None,
                                None, None, O]


def visualize_board(board_list: list[Optional[str]]) -> None:
    for i, n in enumerate(board_list):
        if n is not None:
            print(f'|{n}|', end=" ")
        else:
            print(f'| |', end=" ")

        if i in [2, 5, 8]:
            print()


#while True:
visualize_board(board)

