from pptx.oxml.shapes.shared import (
    BaseShapeElement,
    CT_ApplicationNonVisualDrawingProps,
    CT_NonVisualDrawingProps,
    CT_ShapeProperties,
)
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Connection(BaseShapeElement):
    @property
    def id(self) -> int:
        """ST_DrawingElementId type-converted value of ``id`` attribute."""
        ...

    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def idx(self) -> int:
        """XsdUnsignedInt type-converted value of ``idx`` attribute."""
        ...

    @idx.setter
    def idx(self, value: int) -> None: ...

class CT_Connector(BaseShapeElement):
    @property
    def nvCxnSpPr(self) -> CT_ConnectorNonVisual:
        """Required ``<p:nvCxnSpPr>`` child element."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties:
        """Required ``<p:spPr>`` child element."""
        ...

    @classmethod
    def new_cxnSp(
        cls, id_: int, name: str, prst: str, x: int, y: int, cx: int, cy: int, flipH: bool, flipV: bool
    ) -> CT_Connector: ...

class CT_ConnectorNonVisual(BaseOxmlElement):
    @property
    def cNvPr(self) -> CT_NonVisualDrawingProps:
        """Required ``<p:cNvPr>`` child element."""
        ...

    @property
    def cNvCxnSpPr(self) -> CT_NonVisualConnectorProperties:
        """Required ``<p:cNvCxnSpPr>`` child element."""
        ...

    @property
    def nvPr(self) -> CT_ApplicationNonVisualDrawingProps:
        """Required ``<p:nvPr>`` child element."""
        ...

class CT_NonVisualConnectorProperties(BaseOxmlElement):
    @property
    def stCxn(self) -> CT_Connection | None:
        """``<a:stCxn>`` child element or |None| if not present."""
        ...

    def get_or_add_stCxn(self) -> CT_Connection:
        """Return the ``<a:stCxn>`` child element, newly added if not present."""
        ...

    @property
    def endCxn(self) -> CT_Connection | None:
        """``<a:endCxn>`` child element or |None| if not present."""
        ...

    def get_or_add_endCxn(self) -> CT_Connection:
        """Return the ``<a:endCxn>`` child element, newly added if not present."""
        ...
