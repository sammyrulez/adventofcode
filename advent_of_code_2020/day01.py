from typing import Optional, Set

def _read_file(path:str) -> Set[int]:
    with open(path,"r") as file:
        return set (
            [int(s) for s in file.readlines()]
        )

def _findMatch(data:Set[int], total :int) -> Optional[int]:
    result_generator = [d for d in data if total - d in data]
    k = result_generator.pop()
    return k * (total - k)

def megaProduct(path: str, total=2020) -> Optional[int]:

    return _findMatch(_read_file(path), total)




