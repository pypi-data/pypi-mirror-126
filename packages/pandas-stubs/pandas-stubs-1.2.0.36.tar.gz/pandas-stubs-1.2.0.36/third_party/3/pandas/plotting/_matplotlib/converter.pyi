import matplotlib.units as dates
import matplotlib.units as units
from matplotlib.ticker import Formatter, Locator

from typing import Any, Optional

HOURS_PER_DAY: float
MIN_PER_HOUR: float
SEC_PER_MIN: float
SEC_PER_HOUR: Any
SEC_PER_DAY: Any
MUSEC_PER_DAY: Any


def get_pairs() -> Any: ...
def register_pandas_matplotlib_converters(func: Any) -> Any: ...
def pandas_converters() -> None: ...
def register() -> None: ...
def deregister() -> None: ...
def time2num(d: Any) -> Any: ...

class TimeConverter(units.ConversionInterface): # type: ignore
    @staticmethod
    def convert(value: Any, unit: Any, axis: Any) -> Any: ...
    @staticmethod
    def axisinfo(unit: Any, axis: Any) -> Any: ...
    @staticmethod
    def default_units(x: Any, axis: Any) -> Any: ...

class TimeFormatter(Formatter): # type: ignore
    locs: Any = ...
    def __init__(self, locs: Any) -> None: ...
    def __call__(self, x: Any, pos: int = ...) -> Any: ...

class PeriodConverter(dates.DateConverter): # type: ignore
    @staticmethod
    def convert(values: Any, units: Any, axis: Any) -> Any: ...

def get_datevalue(date: Any, freq: Any) -> Any: ...

class DatetimeConverter(dates.DateConverter): # type: ignore
    @staticmethod
    def convert(values: Any, unit: Any, axis: Any) -> Any: ...
    @staticmethod
    def axisinfo(unit: Any, axis: Any) -> Any: ...

class PandasAutoDateFormatter(dates.AutoDateFormatter): # type: ignore
    def __init__(self, locator: Any, tz: Optional[Any] = ..., defaultfmt: str = ...) -> None: ...

class PandasAutoDateLocator(dates.AutoDateLocator): # type: ignore
    def get_locator(self, dmin: Any, dmax: Any) -> Any: ...

class MilliSecondLocator(dates.DateLocator): # type: ignore
    UNIT: Any = ...
    def __init__(self, tz: Any) -> None: ...
    @staticmethod
    def get_unit_generic(freq: Any) -> Any: ...
    def __call__(self) -> Any: ...
    def autoscale(self) -> Any: ...

def period_break(dates: Any, period: Any) -> Any: ...
def has_level_label(label_flags: Any, vmin: Any) -> Any: ...
def get_finder(freq: Any) -> Any: ...

class TimeSeries_DateLocator(Locator): # type: ignore
    freq: Any = ...
    base: Any = ...
    isminor: Any = ...
    isdynamic: Any = ...
    offset: int = ...
    plot_obj: Any = ...
    finder: Any = ...
    def __init__(self, freq: Any, minor_locator: bool = ..., dynamic_mode: bool = ..., base: int = ..., quarter: int = ..., month: int = ..., day: int = ..., plot_obj: Optional[Any] = ...) -> None: ...
    def __call__(self) -> Any: ...
    def autoscale(self) -> Any: ...

class TimeSeries_DateFormatter(Formatter): # type: ignore
    format: Any = ...
    freq: Any = ...
    locs: Any = ...
    formatdict: Any = ...
    isminor: Any = ...
    isdynamic: Any = ...
    offset: int = ...
    plot_obj: Any = ...
    finder: Any = ...
    def __init__(self, freq: Any, minor_locator: bool = ..., dynamic_mode: bool = ..., plot_obj: Optional[Any] = ...) -> None: ...
    def set_locs(self, locs: Any) -> None: ...
    def __call__(self, x: Any, pos: int = ...) -> Any: ...

class TimeSeries_TimedeltaFormatter(Formatter): # type: ignore
    @staticmethod
    def format_timedelta_ticks(x: Any, pos: Any, n_decimals: Any) -> Any: ...
    def __call__(self, x: Any, pos: int = ...) -> Any: ...
