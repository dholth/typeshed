# Stubs for selector
# See https://docs.python.org/3/library/selectors.html

from abc import ABCMeta, abstractmethod
from typing import Any, List, Mapping, NamedTuple, Optional, Protocol, Tuple, Union

class _HasFileno(Protocol):
    def fileno(self) -> int: ...

# Type aliases added mainly to preserve some context
_FileObject = Union[int, _HasFileno]
_FileDescriptor = int
_EventMask = int


EVENT_READ: _EventMask
EVENT_WRITE: _EventMask


SelectorKey = NamedTuple('SelectorKey', [
    ('fileobj', _FileObject),
    ('fd', _FileDescriptor),
    ('events', _EventMask),
    ('data', Any)
])


class BaseSelector(metaclass=ABCMeta):
    @abstractmethod
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...

    @abstractmethod
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...

    def modify(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...

    @abstractmethod
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...

    def close(self) -> None: ...

    def get_key(self, fileobj: _FileObject) -> SelectorKey: ...

    @abstractmethod
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

    def __enter__(self) -> BaseSelector: ...

    def __exit__(self, *args: Any) -> None: ...

class SelectSelector(BaseSelector):
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class PollSelector(BaseSelector):
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class EpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class DevpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class KqueueSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class DefaultSelector(BaseSelector):
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...
