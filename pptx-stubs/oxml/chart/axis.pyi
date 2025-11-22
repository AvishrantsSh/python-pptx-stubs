from pptx.enum.chart import XL_AXIS_CROSSES, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.oxml.chart.shared import CT_Boolean, CT_Double, CT_NumFmt, CT_Title, CT_UnsignedInt
from pptx.oxml.shapes.shared import CT_ShapeProperties
from pptx.oxml.simpletypes import ST_Orientation
from pptx.oxml.text import CT_TextBody, CT_TextCharacterProperties
from pptx.oxml.xmlchemy import BaseOxmlElement

class BaseAxisElement(BaseOxmlElement):
    @property
    def defRPr(self) -> CT_TextCharacterProperties: ...
    @property
    def orientation(self) -> ST_Orientation: ...
    @orientation.setter
    def orientation(self, value: ST_Orientation) -> None: ...

class CT_AxisUnit(BaseOxmlElement):
    @property
    def val(self) -> float:
        """ST_AxisUnit type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: float) -> None: ...

class CT_CatAx(BaseAxisElement):
    @property
    def scaling(self) -> CT_Scaling:
        """Required ``<c:scaling>`` child element."""
        ...

    @property
    def delete_(self) -> CT_Boolean | None:
        """``<c:delete>`` child element or |None| if not present."""
        ...

    def get_or_add_delete_(self) -> CT_Boolean:
        """Return the ``<c:delete>`` child element, newly added if not present."""
        ...

    @property
    def majorGridlines(self) -> CT_ChartLines | None:
        """``<c:majorGridlines>`` child element or |None| if not present."""
        ...

    def get_or_add_majorGridlines(self) -> CT_ChartLines:
        """Return the ``<c:majorGridlines>`` child element, newly added if not present."""
        ...

    @property
    def minorGridlines(self) -> CT_ChartLines | None:
        """``<c:minorGridlines>`` child element or |None| if not present."""
        ...

    def get_or_add_minorGridlines(self) -> CT_ChartLines:
        """Return the ``<c:minorGridlines>`` child element, newly added if not present."""
        ...

    @property
    def title(self) -> CT_Title | None:
        """``<c:title>`` child element or |None| if not present."""
        ...

    def get_or_add_title(self) -> CT_Title:
        """Return the ``<c:title>`` child element, newly added if not present."""
        ...

    @property
    def numFmt(self) -> CT_NumFmt | None:
        """``<c:numFmt>`` child element or |None| if not present."""
        ...

    def get_or_add_numFmt(self) -> CT_NumFmt:
        """Return the ``<c:numFmt>`` child element, newly added if not present."""
        ...

    @property
    def majorTickMark(self) -> CT_TickMark | None:
        """``<c:majorTickMark>`` child element or |None| if not present."""
        ...

    def get_or_add_majorTickMark(self) -> CT_TickMark:
        """Return the ``<c:majorTickMark>`` child element, newly added if not present."""
        ...

    @property
    def minorTickMark(self) -> CT_TickMark | None:
        """``<c:minorTickMark>`` child element or |None| if not present."""
        ...

    def get_or_add_minorTickMark(self) -> CT_TickMark:
        """Return the ``<c:minorTickMark>`` child element, newly added if not present."""
        ...

    @property
    def tickLblPos(self) -> CT_TickLblPos | None:
        """``<c:tickLblPos>`` child element or |None| if not present."""
        ...

    def get_or_add_tickLblPos(self) -> CT_TickLblPos:
        """Return the ``<c:tickLblPos>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    @property
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def crosses(self) -> CT_Crosses | None:
        """``<c:crosses>`` child element or |None| if not present."""
        ...

    def get_or_add_crosses(self) -> CT_Crosses:
        """Return the ``<c:crosses>`` child element, newly added if not present."""
        ...

    @property
    def crossesAt(self) -> CT_Double | None:
        """``<c:crossesAt>`` child element or |None| if not present."""
        ...

    def get_or_add_crossesAt(self) -> CT_Double:
        """Return the ``<c:crossesAt>`` child element, newly added if not present."""
        ...

    @property
    def lblOffset(self) -> CT_LblOffset | None:
        """``<c:lblOffset>`` child element or |None| if not present."""
        ...

    def get_or_add_lblOffset(self) -> CT_LblOffset:
        """Return the ``<c:lblOffset>`` child element, newly added if not present."""
        ...

class CT_ChartLines(BaseOxmlElement):
    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

class CT_Crosses(BaseOxmlElement):
    @property
    def val(self) -> XL_AXIS_CROSSES:
        """XL_AXIS_CROSSES type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: XL_AXIS_CROSSES) -> None: ...

class CT_DateAx(BaseAxisElement):
    @property
    def scaling(self) -> CT_Scaling:
        """Required ``<c:scaling>`` child element."""
        ...

    @property
    def delete_(self) -> CT_Boolean | None:
        """``<c:delete>`` child element or |None| if not present."""
        ...

    def get_or_add_delete_(self) -> CT_Boolean:
        """Return the ``<c:delete>`` child element, newly added if not present."""
        ...

    @property
    def majorGridlines(self) -> CT_ChartLines | None:
        """``<c:majorGridlines>`` child element or |None| if not present."""
        ...

    def get_or_add_majorGridlines(self) -> CT_ChartLines:
        """Return the ``<c:majorGridlines>`` child element, newly added if not present."""
        ...

    @property
    def minorGridlines(self) -> CT_ChartLines | None:
        """``<c:minorGridlines>`` child element or |None| if not present."""
        ...

    def get_or_add_minorGridlines(self) -> CT_ChartLines:
        """Return the ``<c:minorGridlines>`` child element, newly added if not present."""
        ...

    @property
    def title(self) -> CT_Title | None:
        """``<c:title>`` child element or |None| if not present."""
        ...

    def get_or_add_title(self) -> CT_Title:
        """Return the ``<c:title>`` child element, newly added if not present."""
        ...

    @property
    def numFmt(self) -> CT_NumFmt | None:
        """``<c:numFmt>`` child element or |None| if not present."""
        ...

    def get_or_add_numFmt(self) -> CT_NumFmt:
        """Return the ``<c:numFmt>`` child element, newly added if not present."""
        ...

    @property
    def majorTickMark(self) -> CT_TickMark | None:
        """``<c:majorTickMark>`` child element or |None| if not present."""
        ...

    def get_or_add_majorTickMark(self) -> CT_TickMark:
        """Return the ``<c:majorTickMark>`` child element, newly added if not present."""
        ...

    @property
    def minorTickMark(self) -> CT_TickMark | None:
        """``<c:minorTickMark>`` child element or |None| if not present."""
        ...

    def get_or_add_minorTickMark(self) -> CT_TickMark:
        """Return the ``<c:minorTickMark>`` child element, newly added if not present."""
        ...

    @property
    def tickLblPos(self) -> CT_TickLblPos | None:
        """``<c:tickLblPos>`` child element or |None| if not present."""
        ...

    def get_or_add_tickLblPos(self) -> CT_TickLblPos:
        """Return the ``<c:tickLblPos>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    @property
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def crosses(self) -> CT_Crosses | None:
        """``<c:crosses>`` child element or |None| if not present."""
        ...

    def get_or_add_crosses(self) -> CT_Crosses:
        """Return the ``<c:crosses>`` child element, newly added if not present."""
        ...

    @property
    def crossesAt(self) -> CT_Double | None:
        """``<c:crossesAt>`` child element or |None| if not present."""
        ...

    def get_or_add_crossesAt(self) -> CT_Double:
        """Return the ``<c:crossesAt>`` child element, newly added if not present."""
        ...

    @property
    def lblOffset(self) -> CT_LblOffset | None:
        """``<c:lblOffset>`` child element or |None| if not present."""
        ...

    def get_or_add_lblOffset(self) -> CT_LblOffset:
        """Return the ``<c:lblOffset>`` child element, newly added if not present."""
        ...

class CT_LblOffset(BaseOxmlElement):
    @property
    def val(self) -> int:
        """ST_LblOffset type-converted value of ``val`` attribute, or |100|. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...

class CT_Orientation(BaseOxmlElement):
    @property
    def val(self) -> str:
        """ST_Orientation type-converted value of ``val`` attribute, or |minMax|. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: str) -> None: ...

class CT_Scaling(BaseOxmlElement):
    """`c:scaling` element.

    Defines axis scale characteristics such as maximum value, log vs. linear, etc.
    """

    @property
    def orientation(self) -> CT_Orientation | None:
        """``<c:orientation>`` child element or |None| if not present."""
        ...

    def get_or_add_orientation(self) -> CT_Orientation:
        """Return the ``<c:orientation>`` child element, newly added if not present."""
        ...

    @property
    def max(self) -> CT_Double | None:
        """``<c:max>`` child element or |None| if not present."""
        ...

    def get_or_add_max(self) -> CT_Double:
        """Return the ``<c:max>`` child element, newly added if not present."""
        ...

    @property
    def min(self) -> CT_Double | None:
        """``<c:min>`` child element or |None| if not present."""
        ...

    def get_or_add_min(self) -> CT_Double:
        """Return the ``<c:min>`` child element, newly added if not present."""
        ...

    @property
    def maximum(self) -> float | None: ...
    @maximum.setter
    def maximum(self, value: float | None) -> None: ...
    @property
    def minimum(self) -> float | None: ...
    @minimum.setter
    def minimum(self, value: float | None) -> None: ...

class CT_TickLblPos(BaseOxmlElement):
    @property
    def val(self) -> XL_TICK_LABEL_POSITION | None:
        """XL_TICK_LABEL_POSITION type-converted value of ``val`` attribute, or |None|. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: XL_TICK_LABEL_POSITION | None) -> None: ...

class CT_TickMark(BaseOxmlElement):
    @property
    def val(self) -> XL_TICK_MARK:
        """XL_TICK_MARK type-converted value of ``val`` attribute, or |XL_TICK_MARK.CROSS|. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: XL_TICK_MARK) -> None: ...

class CT_ValAx(BaseAxisElement):
    @property
    def scaling(self) -> CT_Scaling:
        """Required ``<c:scaling>`` child element."""
        ...

    @property
    def delete_(self) -> CT_Boolean | None:
        """``<c:delete>`` child element or |None| if not present."""
        ...

    def get_or_add_delete_(self) -> CT_Boolean:
        """Return the ``<c:delete>`` child element, newly added if not present."""
        ...

    @property
    def majorGridlines(self) -> CT_ChartLines | None:
        """``<c:majorGridlines>`` child element or |None| if not present."""
        ...

    def get_or_add_majorGridlines(self) -> CT_ChartLines:
        """Return the ``<c:majorGridlines>`` child element, newly added if not present."""
        ...

    @property
    def minorGridlines(self) -> CT_ChartLines | None:
        """``<c:minorGridlines>`` child element or |None| if not present."""
        ...

    def get_or_add_minorGridlines(self) -> CT_ChartLines:
        """Return the ``<c:minorGridlines>`` child element, newly added if not present."""
        ...

    @property
    def title(self) -> CT_Title | None:
        """``<c:title>`` child element or |None| if not present."""
        ...

    def get_or_add_title(self) -> CT_Title:
        """Return the ``<c:title>`` child element, newly added if not present."""
        ...

    @property
    def numFmt(self) -> CT_NumFmt | None:
        """``<c:numFmt>`` child element or |None| if not present."""
        ...

    def get_or_add_numFmt(self) -> CT_NumFmt:
        """Return the ``<c:numFmt>`` child element, newly added if not present."""
        ...

    @property
    def majorTickMark(self) -> CT_TickMark | None:
        """``<c:majorTickMark>`` child element or |None| if not present."""
        ...

    def get_or_add_majorTickMark(self) -> CT_TickMark:
        """Return the ``<c:majorTickMark>`` child element, newly added if not present."""
        ...

    @property
    def minorTickMark(self) -> CT_TickMark | None:
        """``<c:minorTickMark>`` child element or |None| if not present."""
        ...

    def get_or_add_minorTickMark(self) -> CT_TickMark:
        """Return the ``<c:minorTickMark>`` child element, newly added if not present."""
        ...

    @property
    def tickLblPos(self) -> CT_TickLblPos | None:
        """``<c:tickLblPos>`` child element or |None| if not present."""
        ...

    def get_or_add_tickLblPos(self) -> CT_TickLblPos:
        """Return the ``<c:tickLblPos>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    @property
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def crossAx(self) -> CT_UnsignedInt | None:
        """``<c:crossAx>`` child element or |None| if not present."""
        ...

    def get_or_add_crossAx(self) -> CT_UnsignedInt:
        """Return the ``<c:crossAx>`` child element, newly added if not present."""
        ...

    @property
    def crosses(self) -> CT_Crosses | None:
        """``<c:crosses>`` child element or |None| if not present."""
        ...

    def get_or_add_crosses(self) -> CT_Crosses:
        """Return the ``<c:crosses>`` child element, newly added if not present."""
        ...

    @property
    def crossesAt(self) -> CT_Double | None:
        """``<c:crossesAt>`` child element or |None| if not present."""
        ...

    def get_or_add_crossesAt(self) -> CT_Double:
        """Return the ``<c:crossesAt>`` child element, newly added if not present."""
        ...

    @property
    def majorUnit(self) -> CT_AxisUnit | None:
        """``<c:majorUnit>`` child element or |None| if not present."""
        ...

    def get_or_add_majorUnit(self) -> CT_AxisUnit:
        """Return the ``<c:majorUnit>`` child element, newly added if not present."""
        ...

    @property
    def minorUnit(self) -> CT_AxisUnit | None:
        """``<c:minorUnit>`` child element or |None| if not present."""
        ...

    def get_or_add_minorUnit(self) -> CT_AxisUnit:
        """Return the ``<c:minorUnit>`` child element, newly added if not present."""
        ...
