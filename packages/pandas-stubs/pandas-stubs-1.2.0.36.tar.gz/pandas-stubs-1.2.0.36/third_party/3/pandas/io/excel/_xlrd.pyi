from pandas.io.excel._base import _BaseExcelReader
from typing import Any

class _XlrdReader(_BaseExcelReader):
    def __init__(self, filepath_or_buffer: Any) -> None: ...
    def load_workbook(self, filepath_or_buffer: Any) -> Any: ...
    @property
    def sheet_names(self) -> Any: ...
    def get_sheet_by_name(self, name: Any) -> Any: ...
    def get_sheet_by_index(self, index: Any) -> Any: ...
    def get_sheet_data(self, sheet: Any, convert_float: Any) -> Any: ...
