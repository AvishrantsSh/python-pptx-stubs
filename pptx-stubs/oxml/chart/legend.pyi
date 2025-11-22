from pptx.enum.chart import XL_LEGEND_POSITION
from pptx.oxml.chart.shared import CT_Boolean_Explicit, CT_Layout
from pptx.oxml.text import CT_TextBody, CT_TextCharacterProperties
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Legend(BaseOxmlElement):
    @property
    def legendPos(self) -> CT_LegendPos | None:
        """``<c:legendPos>`` child element or |None| if not present."""
        ...

    def get_or_add_legendPos(self) -> CT_LegendPos:
        """Return the ``<c:legendPos>`` child element, newly added if not present."""
        ...

    @property
    def layout(self) -> CT_Layout | None:
        """``<c:layout>`` child element or |None| if not present."""
        ...

    def get_or_add_layout(self) -> CT_Layout:
        """Return the ``<c:layout>`` child element, newly added if not present."""
        ...

    @property
    def overlay(self) -> CT_Boolean_Explicit | None:
        """``<c:overlay>`` child element or |None| if not present."""
        ...

    def get_or_add_overlay(self) -> CT_Boolean_Explicit:
        """Return the ``<c:overlay>`` child element, newly added if not present."""
        ...

    @property
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def defRPr(self) -> CT_TextCharacterProperties: ...
    @property
    def horz_offset(self) -> float: ...
    @horz_offset.setter
    def horz_offset(self, offset: float) -> None: ...

class CT_LegendPos(BaseOxmlElement):
    @property
    def val(self) -> XL_LEGEND_POSITION:
        """XL_LEGEND_POSITION type-converted value of ``val`` attribute, or |XL_LEGEND_POSITION.RIGHT|. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: XL_LEGEND_POSITION): ...
