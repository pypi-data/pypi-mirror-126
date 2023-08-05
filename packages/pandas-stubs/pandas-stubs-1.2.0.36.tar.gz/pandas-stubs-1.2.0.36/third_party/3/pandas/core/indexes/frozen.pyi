from pandas.core.base import PandasObject as PandasObject
from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Any, List


class FrozenList(PandasObject, List[Any]):
    def union(self, other: Any) -> FrozenList: ...
    def difference(self, other: Any) -> FrozenList: ...
    def __radd__(self, other: Any) -> Any: ...
    __req__: Any = ...
    def __mul__(self, other: Any) -> Any: ...
    __imul__: Any = ...
    pop: Any = ...
    append: Any = ...
    extend: Any = ...
    remove: Any = ...
    sort: Any = ...
    insert: Any = ...
