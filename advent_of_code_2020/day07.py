from advent_of_code_2020.fp.list import List
from typing import Dict, Generic, Optional, Tuple, Callable, TypeVar, Union, Set
import sys




def _read_file(path: str) -> Dict[str,Set[str]]:
    def map_tuple(l:str):
        tokens = l.split('contain')
        bags = list(tokens[1].strip().split(','))
        return tokens[0].strip(), set(map( lambda s: s[2:-5].strip(), bags))

    with open(path, "r") as file:
        return dict(List(file.readlines()).map(map_tuple))


def _find_chain(bag: str, data: Dict[str, Set[str]]) -> List[str]:
    return List( [a for a in data.keys() if bag in data[a] ] )


def _accumultate_chains(bags: List[str], data: Dict[str, Set[str]]) -> List[str]:
    return _accumultate_chains(List([_find_chain(b,data) for b in bags]).flatten(),data)


def matriosk_1(path: str) -> int:
    data = _read_file(path)
    print(_accumultate_chains(List(['shiny gold']), data))
    return 0


