from __future__ import annotations
from functools import reduce
from itertools import chain
from typing import Any, Callable, Iterable, Iterator, List as _List, TypeVar

from monads.monad import Monad  
from monads.monoid import Monoidal

T = TypeVar("T")
S = TypeVar("S")


class List(Monad[T], Monoidal[list]):  # type: ignore
    @classmethod
    def pure(cls, value: T) -> List[T]:
        return List([value])

    def bind(self, function: Callable[[T], List[S]]) -> List[S]:
        return reduce(List.mappend, map(function, self.value), List.mzero())

    def map(self, function: Callable[[T], S]) -> List[S]:
        return List(list(map(function, self.value)))
    

    def apply(self, functor: List[Callable[[T], S]]) -> List[S]:
        return List(
            list(chain.from_iterable([map(f, self.value)
                                      for f in functor.value]))
        )

    @classmethod
    def sequence(cls, xs: Iterable[List[T]]) -> List[_List[T]]:
        """Evaluate monadic actions in sequence, collecting results."""

        def mcons(acc: List[_List[T]], x: List[T]) -> List[_List[T]]:
            return acc.bind(lambda acc_: x.map(lambda x_: acc_ + [x_]))

        empty: List[_List[T]] = cls.pure([])  # type: ignore
        return reduce(mcons, xs, empty) 

    @classmethod
    def mzero(cls) -> List[T]:
        return cls(list())

    def mappend(self, other: List[T]) -> List[T]:
        return List(self.value + other.value)
    
    def flatten(self) -> List[T]:
        def flat(acc: List[T], element: T) -> List[T]:
            if element and isinstance(element,Iterable):
                for k in element:
                   acc = acc.mappend(List([k]))
            elif element:
                acc = acc.mappend(List([element]))
            return acc

        return List(
            reduce(flat, self, List.mzero())  # type: ignore
        )
    
    def fold(self, functor: Callable[[S,T], S], base_val:S) -> S:
        return reduce(functor,self.value,base_val)

    __add__ = mappend
    def __and__(other, self): return List.apply(self, other)  # type: ignore
    __mul__ = __rmul__ = map
    __rshift__ = bind

    def __sizeof__(self) -> int:
        return self.value.__sizeof__()
    
    def __len__(self) -> int:
        return len(list(self.value))

    def __iter__(self)-> Iterator[T]:
        return iter(self.value)


    

    

    

