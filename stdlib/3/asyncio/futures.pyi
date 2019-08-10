import sys
from typing import Any, Union, Callable, TypeVar, Type, List, Generic, Iterable, Generator, Awaitable, Optional, Tuple
from .events import AbstractEventLoop
from concurrent.futures import (
    CancelledError as CancelledError,
    TimeoutError as TimeoutError,
    Future as _ConcurrentFuture,
    Error,
)

if sys.version_info >= (3, 7):
    from contextvars import Context

__all__: List[str]

_T = TypeVar('_T')
_S = TypeVar('_S', bound=Future)

class InvalidStateError(Error): ...

class _TracebackLogger:
    exc: BaseException
    tb: List[str]
    def __init__(self, exc: Any, loop: AbstractEventLoop) -> None: ...
    def activate(self) -> None: ...
    def clear(self) -> None: ...
    def __del__(self) -> None: ...

def isfuture(obj: object) -> bool: ...

class Future(Awaitable[_T], Iterable[_T]):
    _state: str
    _exception: BaseException
    _blocking = False
    _log_traceback = False
    _tb_logger: Type[_TracebackLogger]
    def __init__(self, *, loop: Optional[AbstractEventLoop] = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __del__(self) -> None: ...
    if sys.version_info >= (3, 7):
        def get_loop(self) -> AbstractEventLoop: ...
        def _callbacks(self: _S) -> List[Tuple[Callable[[_S], Any], Context]]: ...
        def add_done_callback(self: _S, __fn: Callable[[_S], Any], *, context: Optional[Context] = ...) -> None: ...
    else:
        @property
        def _callbacks(self: _S) -> List[Callable[[_S], Any]]: ...
        def add_done_callback(self: _S, __fn: Callable[[_S], Any]) -> None: ...
    def cancel(self) -> bool: ...
    def _schedule_callbacks(self) -> None: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self) -> _T: ...
    def exception(self) -> BaseException: ...
    def remove_done_callback(self: _S, fn: Callable[[_S], Any]) -> int: ...
    def set_result(self, result: _T) -> None: ...
    def set_exception(self, exception: Union[type, BaseException]) -> None: ...
    def _copy_state(self, other: Any) -> None: ...
    def __iter__(self) -> Generator[Any, None, _T]: ...
    def __await__(self) -> Generator[Any, None, _T]: ...
    @property
    def _loop(self) -> AbstractEventLoop: ...

def wrap_future(f: Union[_ConcurrentFuture[_T], Future[_T]]) -> Future[_T]: ...
