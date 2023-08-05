from pandas.core.construction import create_series_with_explicit_dtype as create_series_with_explicit_dtype

from pandas.errors import AbstractMethodError as AbstractMethodError, EmptyDataError as EmptyDataError
from pandas.io.common import is_url as is_url, urlopen as urlopen, validate_header_arg as validate_header_arg
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.io.parsers import TextParser as TextParser
from typing import Any, Optional

class _HtmlFrameParser:
    io: Any = ...
    match: Any = ...
    attrs: Any = ...
    encoding: Any = ...
    displayed_only: Any = ...
    def __init__(self, io: Any, match: Any, attrs: Any, encoding: Any, displayed_only: Any) -> None: ...
    def parse_tables(self) -> Any: ...

class _BeautifulSoupHtml5LibFrameParser(_HtmlFrameParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class _LxmlFrameParser(_HtmlFrameParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def read_html(io: Any, match: str = ..., flavor: Optional[Any] = ..., header: Optional[Any] = ..., index_col: Optional[Any] = ..., skiprows: Optional[Any] = ..., attrs: Optional[Any] = ..., parse_dates: bool = ..., thousands: str = ..., encoding: Optional[Any] = ..., decimal: str = ..., converters: Optional[Any] = ..., na_values: Optional[Any] = ..., keep_default_na: bool = ..., displayed_only: bool = ...) -> Any: ...
