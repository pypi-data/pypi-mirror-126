from typing import Any

class PyperclipException(RuntimeError): ...

class PyperclipWindowsException(PyperclipException):
    def __init__(self, message: Any) -> None: ...

class CheckedCall:
    def __init__(self, f: Any) -> None: ...
    def __call__(self, *args: Any) -> Any: ...
    def __setattr__(self, key: Any, value: Any) -> None: ...

def determine_clipboard() -> Any: ...
def set_clipboard(clipboard: Any) -> None: ...

copy: Any
paste: Any
clipboard_get = paste
clipboard_set = copy
