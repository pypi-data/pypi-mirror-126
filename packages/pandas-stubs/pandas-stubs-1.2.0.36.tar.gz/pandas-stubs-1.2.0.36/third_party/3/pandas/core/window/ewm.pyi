from pandas.core.base import DataError as DataError
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame
from pandas.core.window.common import zsqrt as zsqrt
from pandas.core.window.rolling import _Rolling
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Any, Optional

class ExponentialMovingWindow(_Rolling):
    obj: Any = ...
    com: Any = ...
    min_periods: Any = ...
    adjust: Any = ...
    ignore_na: Any = ...
    axis: Any = ...
    on: Any = ...
    def __init__(self, obj: Any, com: Optional[Any] = ..., span: Optional[Any] = ..., halflife: Optional[Any] = ..., alpha: Optional[Any] = ..., min_periods: int = ..., adjust: bool = ..., ignore_na: bool = ..., axis: int = ...) -> None: ...
    def aggregate(self, func: Any, *args: Any, **kwargs: Any) -> Any: ...
    agg: Any = ...
    def mean(self, *args: Any, **kwargs: Any) -> Any: ...
    def std(self, bias: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    vol: Any = ...
    def var(self, bias: bool = ..., *args: Any, **kwargs: Any) -> Any: ...
    def cov(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., bias: bool = ..., **kwargs: Any) -> Any: ...
    def corr(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., **kwargs: Any) -> Any: ...
