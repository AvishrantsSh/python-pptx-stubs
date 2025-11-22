from pptx.enum.chart import XL_MARKER_STYLE
from pptx.oxml.shapes.shared import CT_ShapeProperties
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Marker(BaseOxmlElement):
    @property
    def symbol(self) -> CT_MarkerStyle | None:
        """``<c:symbol>`` child element or |None| if not present."""
        ...

    def get_or_add_symbol(self) -> CT_MarkerStyle:
        """Return the ``<c:symbol>`` child element, newly added if not present."""
        ...

    @property
    def size(self) -> CT_MarkerSize | None:
        """``<c:size>`` child element or |None| if not present."""
        ...

    def get_or_add_size(self) -> CT_MarkerSize:
        """Return the ``<c:size>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    @property
    def size_val(self) -> int | None: ...
    @property
    def symbol_val(self) -> XL_MARKER_STYLE | None: ...

class CT_MarkerSize(BaseOxmlElement):
    @property
    def val(self) -> int:
        """ST_MarkerSize type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...

class CT_MarkerStyle(BaseOxmlElement):
    @property
    def val(self) -> XL_MARKER_STYLE:
        """XL_MARKER_STYLE type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: XL_MARKER_STYLE) -> None: ...
