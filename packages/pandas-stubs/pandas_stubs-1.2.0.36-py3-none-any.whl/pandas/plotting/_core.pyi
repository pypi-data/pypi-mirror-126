from pandas._config import get_option as get_option
from pandas.core.base import PandasObject as PandasObject

from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Any, Optional

def hist_series(self: Any, by: Optional[Any] = ..., ax: Optional[Any] = ..., grid: bool = ..., xlabelsize: Optional[Any] = ..., xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ..., yrot: Optional[Any] = ..., figsize: Optional[Any] = ..., bins: int = ..., backend: Optional[Any] = ..., **kwargs: Any) -> Any: ...
def hist_frame(data: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., grid: bool = ..., xlabelsize: Optional[Any] = ..., xrot: Optional[Any] = ..., ylabelsize: Optional[Any] = ..., yrot: Optional[Any] = ..., ax: Optional[Any] = ..., sharex: bool = ..., sharey: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., bins: int = ..., backend: Optional[Any] = ..., **kwargs: Any) -> Any: ...
def boxplot(data: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., return_type: Optional[Any] = ..., **kwargs: Any) -> Any: ...
def boxplot_frame(self: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., return_type: Optional[Any] = ..., backend: Optional[Any] = ..., **kwargs: Any) -> Any: ...
def boxplot_frame_groupby(grouped: Any, subplots: bool = ..., column: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., ax: Optional[Any] = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., sharex: bool = ..., sharey: bool = ..., backend: Optional[Any] = ..., **kwargs: Any) -> Any: ...

class PlotAccessor(PandasObject):
    def __init__(self, data: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def line(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def bar(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def barh(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def box(self, by: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def hist(self, by: Optional[Any] = ..., bins: int = ..., **kwargs: Any) -> Any: ...
    def kde(self, bw_method: Optional[Any] = ..., ind: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    density: Any = ...
    def area(self, x: Optional[Any] = ..., y: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def pie(self, **kwargs: Any) -> Any: ...
    def scatter(self, x: Any, y: Any, s: Optional[Any] = ..., c: Optional[Any] = ..., **kwargs: Any) -> Any: ...
    def hexbin(self, x: Any, y: Any, C: Optional[Any] = ..., reduce_C_function: Optional[Any] = ..., gridsize: Optional[Any] = ..., **kwargs: Any) -> Any: ...
