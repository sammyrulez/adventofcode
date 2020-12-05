
from advent_of_code_2020.fp.list import List
from typing import Any, Generic, Optional, Tuple, Callable, TypeVar, Union
from monads.currying import curry


def _read_file(path: str) -> List[str]:
    with open(path, "r") as file:
        return List(file.readlines())


T = TypeVar("T")
Marker = Tuple[T, T]

@curry
def _eval_seat(p: Marker[int], c: Marker[str], data: str):
    binary_seat = data[p[0]:p[1]]
    binary_seat = binary_seat.replace(c[0], "0").replace(c[1], "1")
    return int(binary_seat, 2)


def _decode(seat_data:List[str]) -> int:
    seats = [_eval_seat((0, 7), ('F', 'B'))(line) * 8 +
             _eval_seat((7, 10), ('L', 'R'))(line) for line in seat_data]
    return max(seats)


def part_1(path: str) -> int:
    return _decode(_read_file(path))


