# Stubs for heapq

# Based on http://docs.python.org/3.2/library/heapq.html

import sys
from typing import TypeVar, List, Iterable, Any, Callable, Optional

_T = TypeVar('_T')

def heappush(heap: List[_T], item: _T) -> None: ...
def heappop(heap: List[_T]) -> _T: ...
def heappushpop(heap: List[_T], item: _T) -> _T: ...
def heapify(x: List[_T]) -> None: ...
def heapreplace(heap: List[_T], item: _T) -> _T: ...
def merge(*iterables: Iterable[_T], key: Callable[[_T], Any] = ..., reverse: bool = ...) -> Iterable[_T]: ...
def nlargest(n: int, iterable: Iterable[_T],
             key: Optional[Callable[[_T], Any]] = ...) -> List[_T]: ...
def nsmallest(n: int, iterable: Iterable[_T],
              key: Callable[[_T], Any] = ...) -> List[_T]: ...
