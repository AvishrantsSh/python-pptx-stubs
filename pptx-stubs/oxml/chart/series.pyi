from lxml.etree import _Element
from pptx.oxml.chart.datalabel import CT_DLbl, CT_DLbls
from pptx.oxml.chart.marker import CT_Marker
from pptx.oxml.chart.shared import CT_Boolean, CT_Boolean_Explicit, CT_Tx, CT_UnsignedInt
from pptx.oxml.shapes.shared import CT_ShapeProperties
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_AxDataSource(BaseOxmlElement):
    @property
    def multiLvlStrRef(self) -> _Element | None:
        """``<c:multiLvlStrRef>`` child element or |None| if not present."""
        ...
    def get_or_add_multiLvlStrRef(self) -> _Element:
        """Return the ``<c:multiLvlStrRef>`` child element, newly added if not present."""
        ...
    @property
    def lvls(self) -> list[CT_Lvl]: ...

class CT_DPt(BaseOxmlElement):
    @property
    def idx(self) -> CT_UnsignedInt:
        """Required ``<c:idx>`` child element."""
        ...

    @property
    def marker(self) -> CT_Marker | None:
        """``<c:marker>`` child element or |None| if not present."""
        ...

    def get_or_add_marker(self) -> CT_Marker:
        """Return the ``<c:marker>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    @classmethod
    def new_dPt(cls) -> CT_DPt: ...

class CT_Lvl(BaseOxmlElement):
    @property
    def pt_lst(self) -> list[CT_StrVal_NumVal_Composite]:
        """A list containing each of the ``<c:pt>`` child elements, in the order they appear."""
        ...

class CT_NumDataSource(BaseOxmlElement):
    @property
    def numRef(self) -> _Element:
        """Required ``<c:numRef>`` child element."""
        ...

    @property
    def ptCount_val(self) -> int: ...
    def pt_v(self, idx: int) -> float | None: ...

class CT_SeriesComposite(BaseOxmlElement):
    @property
    def idx(self) -> CT_UnsignedInt:
        """Required ``<c:idx>`` child element."""
        ...

    @property
    def order(self) -> CT_UnsignedInt:
        """Required ``<c:order>`` child element."""
        ...

    @property
    def tx(self) -> CT_Tx | None:
        """``<c:tx>`` child element or |None| if not present."""
        ...

    def get_or_add_tx(self) -> CT_Tx:
        """Return the ``<c:tx>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    @property
    def invertIfNegative(self) -> CT_Boolean_Explicit | None:
        """``<c:invertIfNegative>`` child element or |None| if not present."""
        ...

    def get_or_add_invertIfNegative(self) -> CT_Boolean_Explicit:
        """Return the ``<c:invertIfNegative>`` child element, newly added if not present."""
        ...

    @property
    def marker(self) -> CT_Marker | None:
        """``<c:marker>`` child element or |None| if not present."""
        ...

    def get_or_add_marker(self) -> CT_Marker:
        """Return the ``<c:marker>`` child element, newly added if not present."""
        ...

    @property
    def dPt_lst(self) -> list[CT_DPt]:
        """A list containing each of the ``<c:dPt>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

    @property
    def cat(self) -> CT_AxDataSource | None:
        """``<c:cat>`` child element or |None| if not present."""
        ...

    def get_or_add_cat(self) -> CT_AxDataSource:
        """Return the ``<c:cat>`` child element, newly added if not present."""
        ...

    @property
    def val(self) -> CT_NumDataSource | None:
        """``<c:val>`` child element or |None| if not present."""
        ...

    def get_or_add_val(self) -> CT_NumDataSource:
        """Return the ``<c:val>`` child element, newly added if not present."""
        ...

    @property
    def xVal(self) -> CT_NumDataSource | None:
        """``<c:xVal>`` child element or |None| if not present."""
        ...

    def get_or_add_xVal(self) -> CT_NumDataSource:
        """Return the ``<c:xVal>`` child element, newly added if not present."""
        ...

    @property
    def yVal(self) -> CT_NumDataSource | None:
        """``<c:yVal>`` child element or |None| if not present."""
        ...

    def get_or_add_yVal(self) -> CT_NumDataSource:
        """Return the ``<c:yVal>`` child element, newly added if not present."""
        ...

    @property
    def smooth(self) -> CT_Boolean | None:
        """``<c:smooth>`` child element or |None| if not present."""
        ...

    def get_or_add_smooth(self) -> CT_Boolean:
        """Return the ``<c:smooth>`` child element, newly added if not present."""
        ...

    @property
    def bubbleSize(self) -> CT_NumDataSource | None:
        """``<c:bubbleSize>`` child element or |None| if not present."""
        ...

    def get_or_add_bubbleSize(self) -> CT_NumDataSource:
        """Return the ``<c:bubbleSize>`` child element, newly added if not present."""
        ...

    @property
    def bubbleSize_ptCount_val(self) -> int: ...
    @property
    def cat_ptCount_val(self) -> int: ...
    def get_dLbl(self, idx) -> CT_DLbl | None: ...
    def get_or_add_dLbl(self, idx: int) -> CT_DLbl: ...
    def get_or_add_dPt_for_point(self, idx: int) -> CT_DPt: ...
    @property
    def xVal_ptCount_val(self) -> int: ...
    @property
    def yVal_ptCount_val(self) -> int: ...

class CT_StrVal_NumVal_Composite(BaseOxmlElement):
    @property
    def v(self) -> _Element:
        """Required ``<c:v>`` child element."""
        ...

    @property
    def idx(self) -> int:
        """XsdUnsignedInt type-converted value of ``idx`` attribute."""
        ...

    @idx.setter
    def idx(self, value: int) -> None: ...
    @property
    def value(self) -> float: ...
