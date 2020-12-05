
from advent_of_code_2020.fp.list import List
from typing import Any, Generic, Optional, Tuple, Callable, TypeVar
from dataclasses import dataclass
import re

T = TypeVar("T")

@dataclass
class Field(Generic[T]):
    name: str
    validation: Callable[[T], bool]

    @property
    def regexp(self):
        return rf"\b(?:{self.name}):[a-zA-Z0-9#]*"


def _check_hcl(s:str) -> bool:
    if s.startswith("#") and len(s) == 7:
        return not bool(set(s[1:]).difference(set("0123456789abcdef")))
    else:
        return False

fields = [
    Field("byr", lambda s: 1920 <= int(s) <= 2002),
    Field("iyr", lambda s: 2010 <= int(s) <= 2020),
    Field("eyr", lambda s: 2020 <= int(s) <= 2030),
    Field("hgt", lambda s: 
        (s.endswith("cm") and (150 <= int(s[:-2]) <= 193)) 
        or (s.endswith("in") and (59 <= int(s[:-2]) <= 76))),
    Field("hcl", _check_hcl ),
    Field("ecl", lambda s: s in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    Field("pid", lambda s: len(s) == 9 and not set(s).difference(set("0123456789")))
]    


def _read_file(path: str) -> List[str]:
    with open(path, "r") as file:
        return List(file.read().split("\n\n"))


def _check_passport(passport: str) -> bool:
    return List[Field](fields).fold(
        lambda a,f: (a and len(re.findall(f.regexp, passport)) >0),True
        )


def _validate_passports(passport: str) -> bool:
    return List[Field](fields).fold(
        lambda a, f: (a and  _validate_passport(passport,f)), True
    )
def _validate_passport(passport: str,field:Field) -> bool:
   match = re.findall(field.regexp, passport)
   if len(match) == 1:
       value = match[0][4:]
       print(value)
       return field.validation(value)
   else:
        return False




def hack_passport_check(path: str) -> int:
    password_data = _read_file(path)
    checked = password_data.map(_validate_passports)
    print(checked)
    return len(checked.flatten())

