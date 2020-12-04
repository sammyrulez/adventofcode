from typing import Dict, Callable, Optional, Tuple
from advent_of_code_2020.fp.list import List 
from monads.currying import curry
from dataclasses import dataclass
import re
from functools import reduce

@dataclass
class PolicyDef:
    char: str
    min: int
    max: int
    password:str

reg = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

def _parse_line(line: str) -> Optional[PolicyDef]:
    matches = reg.match(line)
    if matches:
        g = matches.groups()
        return PolicyDef(g[2],int(g[0]),int(g[1]),g[3])
    else:
        return None


def _read_file(path: str) -> List[PolicyDef]:
    with open(path, "r") as file:
        return List(file.readlines()).map(_parse_line).flatten()
        

def _count_char(char:str,password:str) -> int:
        return password.count(char)


def validate(path: str) -> Tuple[int,int]:
    def check_psw_step1(policy: PolicyDef) -> bool:
        chars = _count_char(policy.char,policy.password)
        return chars >= policy.min and chars <= policy.max

    def check_psw_step2(policy: PolicyDef) -> bool:
        return (policy.password[policy.min-1] == policy.char and policy.password[policy.max-1] != policy.char) or (policy.password[policy.min-1] != policy.char and policy.password[policy.max-1] == policy.char)
    file_data = _read_file(path)
    valid_passwords = file_data.map(lambda p: (check_psw_step1(p), check_psw_step2(p)))

    @curry          
    def count_valid(index: int, value: int, element: Tuple[bool, bool]) -> int:
            if element[index]:
                return 1 +value
            else:
                return value

    step_1:int = valid_passwords.fold(count_valid(0), 0)
    step_2:int = valid_passwords.fold(count_valid(1), 0)
    return (step_1, step_2)


