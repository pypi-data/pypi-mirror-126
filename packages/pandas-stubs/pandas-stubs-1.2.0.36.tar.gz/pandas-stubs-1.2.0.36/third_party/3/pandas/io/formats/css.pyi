from typing import Any, Optional

class CSSWarning(UserWarning): ...

class CSSResolver:
    def __call__(self, declarations_str: Any, inherited: Optional[Any] = ...) -> Any: ...
    UNIT_RATIOS: Any = ...
    FONT_SIZE_RATIOS: Any = ...
    MARGIN_RATIOS: Any = ...
    BORDER_WIDTH_RATIOS: Any = ...
    def size_to_pt(self, in_val: Any, em_pt: Optional[Any] = ..., conversions: Any = ...) -> Any: ...
    def atomize(self, declarations: Any) -> None: ...
    SIDE_SHORTHANDS: Any = ...
    SIDES: Any = ...
    expand_border_color: Any = ...
    expand_border_style: Any = ...
    expand_border_width: Any = ...
    expand_margin: Any = ...
    expand_padding: Any = ...
    def parse(self, declarations_str: str) -> Any: ...
