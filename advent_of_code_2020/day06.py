
from advent_of_code_2020.fp.list import List
from typing import Any, Generic, Optional, Tuple, Callable, TypeVar, Union
from monads.currying import curry

def _read_file(path: str) -> List[List[str]]:
    with open(path, "r") as file:
        return List(file.read().split("\n\n")).map(lambda s: s.split("\n"))


def puzzle1(path: str) -> int:
    groups = _read_file(path)
    return sum([len(set("".join(g))) for g in groups])


def puzzle2(path: str):
    groups = _read_file(path)
    res = 0
    for group in groups:
        for i, answers in enumerate(group):
            curr = set(answers) if i == 0 else curr.intersection(set(answers))
        res += len(curr)
    return res



