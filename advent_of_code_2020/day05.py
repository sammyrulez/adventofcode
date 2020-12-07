
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


def _decode(seat_data:List[str]) -> List[int]:
    seats = [_eval_seat((0, 7), ('F', 'B'))(line) * 8 +
             _eval_seat((7, 10), ('L', 'R'))(line) for line in seat_data]
    return List(seats)


def part_1(path: str) -> int:
    return max(_decode(_read_file(path)))


def part_2(path: str) -> int:
    
    all_seats = List(range(0, 128*8))
    sorted_seats = _decode(_read_file(path)).sort()

    def _check_seat(i: int) -> Optional[int]:
        if i not in sorted_seats:
            return i
    missing_seats = all_seats.map(_check_seat).flatten()
    for i in missing_seats:
        if i-1 not in missing_seats and i+1 not in missing_seats:
            return i

    return sorted_seats


