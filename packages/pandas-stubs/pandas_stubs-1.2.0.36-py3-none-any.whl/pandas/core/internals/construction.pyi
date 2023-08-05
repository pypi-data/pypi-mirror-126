import numpy.ma as np
from pandas.core import algorithms as algorithms
from pandas.core.arrays import Categorical as Categorical
from pandas.core.construction import sanitize_array as sanitize_array
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, maybe_cast_to_datetime as maybe_cast_to_datetime, maybe_convert_platform as maybe_convert_platform, maybe_infer_to_datetimelike as maybe_infer_to_datetimelike, maybe_upcast as maybe_upcast

from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeIndex as ABCDatetimeIndex, ABCIndexClass as ABCIndexClass, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries, ABCTimedeltaIndex as ABCTimedeltaIndex
from pandas.core.indexes.api import Index as Index, ensure_index as ensure_index, get_objs_combined_axis as get_objs_combined_axis, union_indexes as union_indexes
from pandas.core.internals import create_block_manager_from_arrays as create_block_manager_from_arrays, create_block_manager_from_blocks as create_block_manager_from_blocks
from typing import Any, Optional

def arrays_to_mgr(arrays: Any, arr_names: Any, index: Any, columns: Any, dtype: Optional[Any] = ...) -> Any: ...
def masked_rec_array_to_mgr(data: Any, index: Any, columns: Any, dtype: Any, copy: Any) -> Any: ...
def init_ndarray(values: Any, index: Any, columns: Any, dtype: Optional[Any] = ..., copy: bool = ...) -> Any: ...
def init_dict(data: Any, index: Any, columns: Any, dtype: Optional[Any] = ...) -> Any: ...
def prep_ndarray(values: Any, copy: Any = ...) -> np.ndarray: ...
def extract_index(data: Any) -> Any: ...
def reorder_arrays(arrays: Any, arr_columns: Any, columns: Any) -> Any: ...
def get_names_from_index(data: Any) -> Any: ...
def to_arrays(data: Any, columns: Any, coerce_float: bool = ..., dtype: Optional[Any] = ...) -> Any: ...
def sanitize_index(data: Any, index: Any, copy: bool = ...) -> Any: ...
