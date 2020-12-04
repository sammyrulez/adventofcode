
from advent_of_code_2020.fp.list import List
from typing import Tuple
from monads.currying import curry

MapExplorer = Tuple[int, int, ]

def _read_file(path: str) -> List[str]:
    with open(path, "r") as file:
        return List(file.readlines()[1:])
@curry
def _pattern_accumulator(step_right:int, starting_pos: MapExplorer, new_line:str) -> MapExplorer:
    r_pos,  acc_value = starting_pos[0] + step_right,  starting_pos[1]
    max_index = len(new_line) - 1
    if r_pos >= max_index:
            r_pos = r_pos - max_index
    char_at_loc = new_line[r_pos]
    if char_at_loc == '#':
        acc_value = acc_value + 1
    return r_pos, acc_value
            

def explore(path: str, step_right=3, step_down=1) -> int:
    slope_map = List([e for i, e in enumerate(
        _read_file(path)) if (i % step_down) == 0])

    trees = slope_map.fold(_pattern_accumulator(step_right),(0,0))[1]
    print(f"trees: {trees}")
    return trees


def find_slopes(path: str) -> int:
    slopes = List([
        ( 1,  1),
        ( 3,  1),
        ( 5,  1),
        ( 7,  1),
        ( 1,  2)
    ])

    return slopes.map(lambda t: explore(
        path, step_right=t[0], step_down=t[1])).fold(lambda v, e: v * e, 1)

    
    



