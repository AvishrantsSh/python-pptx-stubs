from pptx.enum.chart import XL_DATA_LABEL_POSITION
from pptx.oxml.chart.shared import CT_Boolean_Explicit, CT_NumFmt, CT_Tx, CT_UnsignedInt
from pptx.oxml.shapes.shared import CT_ShapeProperties
from pptx.oxml.text import CT_TextBody, CT_TextCharacterProperties
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_DLbl(BaseOxmlElement):
    @property
    def idx(self) -> CT_UnsignedInt:
        """Required ``<c:idx>`` child element."""
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
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def dLblPos(self) -> CT_DLblPos | None:
        """``<c:dLblPos>`` child element or |None| if not present."""
        ...

    def get_or_add_dLblPos(self) -> CT_DLblPos:
        """Return the ``<c:dLblPos>`` child element, newly added if not present."""
        ...

    def get_or_add_rich(self) -> CT_TextBody: ...
    def get_or_add_tx_rich(self) -> CT_TextBody: ...
    @property
    def idx_val(self) -> int: ...
    @classmethod
    def new_dLbl(cls) -> CT_DLbl: ...
    def remove_tx_rich(self) -> None: ...

class CT_DLblPos(BaseOxmlElement):
    @property
    def val(self) -> XL_DATA_LABEL_POSITION:
        """XL_DATA_LABEL_POSITION type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: XL_DATA_LABEL_POSITION) -> None: ...

class CT_DLbls(BaseOxmlElement):
    @property
    def dLbl_lst(self) -> list[CT_DLbl]:
        """A list containing each of the ``<c:dLbl>`` child elements, in the order they appear."""
        ...

    @property
    def numFmt(self) -> CT_NumFmt | None:
        """``<c:numFmt>`` child element or |None| if not present."""
        ...

    def get_or_add_numFmt(self) -> CT_NumFmt:
        """Return the ``<c:numFmt>`` child element, newly added if not present."""
        ...

    @property
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def dLblPos(self) -> CT_DLblPos | None:
        """``<c:dLblPos>`` child element or |None| if not present."""
        ...

    def get_or_add_dLblPos(self) -> CT_DLblPos:
        """Return the ``<c:dLblPos>`` child element, newly added if not present."""
        ...

    @property
    def showLegendKey(self) -> CT_Boolean_Explicit | None:
        """``<c:showLegendKey>`` child element or |None| if not present."""
        ...

    def get_or_add_showLegendKey(self) -> CT_Boolean_Explicit:
        """Return the ``<c:showLegendKey>`` child element, newly added if not present."""
        ...

    @property
    def showVal(self) -> CT_Boolean_Explicit | None:
        """``<c:showVal>`` child element or |None| if not present."""
        ...

    def get_or_add_showVal(self) -> CT_Boolean_Explicit:
        """Return the ``<c:showVal>`` child element, newly added if not present."""
        ...

    @property
    def showCatName(self) -> CT_Boolean_Explicit | None:
        """``<c:showCatName>`` child element or |None| if not present."""
        ...

    def get_or_add_showCatName(self) -> CT_Boolean_Explicit:
        """Return the ``<c:showCatName>`` child element, newly added if not present."""
        ...

    @property
    def showSerName(self) -> CT_Boolean_Explicit | None:
        """``<c:showSerName>`` child element or |None| if not present."""
        ...

    def get_or_add_showSerName(self) -> CT_Boolean_Explicit:
        """Return the ``<c:showSerName>`` child element, newly added if not present."""
        ...

    @property
    def showPercent(self) -> CT_Boolean_Explicit | None:
        """``<c:showPercent>`` child element or |None| if not present."""
        ...

    def get_or_add_showPercent(self) -> CT_Boolean_Explicit:
        """Return the ``<c:showPercent>`` child element, newly added if not present."""
        ...

    @property
    def defRPr(self) -> CT_TextCharacterProperties: ...
    def get_dLbl_for_point(self, idx: int) -> CT_DLbl | None: ...
    def get_or_add_dLbl_for_point(self, idx: int) -> CT_DLbl: ...
    @classmethod
    def new_dLbls(cls) -> CT_DLbls: ...
