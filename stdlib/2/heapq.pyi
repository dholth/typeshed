from typing import TypeVar, List, Iterable, Any, Callable, Optional, Protocol

_T = TypeVar('_T')

class _Sortable(Protocol):
    def __lt__(self: _T, other: _T) -> bool: ...

def cmp_lt(x, y) -> bool: ...
def heappush(heap: List[_T], item: _T) -> None: ...
def heappop(heap: List[_T]) -> _T:
    raise IndexError()  # if heap is empty
def heappushpop(heap: List[_T], item: _T) -> _T: ...
def heapify(x: List[_T]) -> None: ...
def heapreplace(heap: List[_T], item: _T) -> _T:
    raise IndexError()  # if heap is empty
def merge(*iterables: Iterable[_T]) -> Iterable[_T]: ...
def nlargest(n: int, iterable: Iterable[_T],
             key: Optional[Callable[[_T], _Sortable]] = ...) -> List[_T]: ...
def nsmallest(n: int, iterable: Iterable[_T],
              key: Optional[Callable[[_T], _Sortable]] = ...) -> List[_T]: ...
