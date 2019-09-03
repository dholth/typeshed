# NB: SocketServer.pyi and socketserver.pyi must remain consistent!
# Stubs for socketserver

from typing import Any, BinaryIO, Optional, Tuple, Type, Text, Union
from socket import SocketType
import sys
import types

class BaseServer:
    address_family: int
    RequestHandlerClass: type
    server_address: Tuple[str, int]
    socket: SocketType
    allow_reuse_address: bool
    request_queue_size: int
    socket_type: int
    timeout: Optional[float]
    def __init__(self, server_address: Any,
                 RequestHandlerClass: type) -> None: ...
    def fileno(self) -> int: ...
    def handle_request(self) -> None: ...
    def serve_forever(self, poll_interval: float = ...) -> None: ...
    def shutdown(self) -> None: ...
    def server_close(self) -> None: ...
    def finish_request(self, request: bytes,
                       client_address: Tuple[str, int]) -> None: ...
    def get_request(self) -> None: ...
    def handle_error(self, request: bytes,
                     client_address: Tuple[str, int]) -> None: ...
    def handle_timeout(self) -> None: ...
    def process_request(self, request: bytes,
                        client_address: Tuple[str, int]) -> None: ...
    def server_activate(self) -> None: ...
    def server_bind(self) -> None: ...
    def verify_request(self, request: bytes,
                       client_address: Tuple[str, int]) -> bool: ...
    if sys.version_info >= (3, 6):
        def __enter__(self) -> BaseServer: ...
        def __exit__(self, exc_type: Optional[Type[BaseException]],
                     exc_val: Optional[BaseException],
                     exc_tb: Optional[types.TracebackType]) -> None: ...
    if sys.version_info >= (3, 3):
        def service_actions(self) -> None: ...

class TCPServer(BaseServer):
    def __init__(self, server_address: Tuple[str, int],
                 RequestHandlerClass: type,
                 bind_and_activate: bool = ...) -> None: ...

class UDPServer(BaseServer):
    def __init__(self, server_address: Tuple[str, int],
                 RequestHandlerClass: type,
                 bind_and_activate: bool = ...) -> None: ...

if sys.platform != 'win32':
    class UnixStreamServer(BaseServer):
        def __init__(self, server_address: Union[Text, bytes],
                     RequestHandlerClass: type,
                     bind_and_activate: bool = ...) -> None: ...

    class UnixDatagramServer(BaseServer):
        def __init__(self, server_address: Union[Text, bytes],
                     RequestHandlerClass: type,
                     bind_and_activate: bool = ...) -> None: ...

class ForkingMixIn: ...
class ThreadingMixIn: ...

class ForkingTCPServer(ForkingMixIn, TCPServer): ...
class ForkingUDPServer(ForkingMixIn, UDPServer): ...
class ThreadingTCPServer(ThreadingMixIn, TCPServer): ...
class ThreadingUDPServer(ThreadingMixIn, UDPServer): ...
if sys.platform != 'win32':
    class ThreadingUnixStreamServer(ThreadingMixIn, UnixStreamServer): ...
    class ThreadingUnixDatagramServer(ThreadingMixIn, UnixDatagramServer): ...


class BaseRequestHandler:
    # Those are technically of types, respectively:
    # * Union[SocketType, Tuple[bytes, SocketType]]
    # * Union[Tuple[str, int], str]
    # But there are some concerns that having unions here would cause
    # too much inconvenience to people using it (see
    # https://github.com/python/typeshed/pull/384#issuecomment-234649696)
    request: Any
    client_address: Any

    server: BaseServer
    def setup(self) -> None: ...
    def handle(self) -> None: ...
    def finish(self) -> None: ...

class StreamRequestHandler(BaseRequestHandler):
    rfile: BinaryIO
    wfile: BinaryIO

class DatagramRequestHandler(BaseRequestHandler):
    rfile: BinaryIO
    wfile: BinaryIO
