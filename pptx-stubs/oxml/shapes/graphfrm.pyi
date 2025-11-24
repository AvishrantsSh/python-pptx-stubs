from pptx.oxml.chart.chart import CT_Chart
from pptx.oxml.shapes.shared import (
    BaseShapeElement,
    CT_ApplicationNonVisualDrawingProps,
    CT_NonVisualDrawingProps,
    CT_Transform2D,
)
from pptx.oxml.table import CT_Table
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_GraphicalObject(BaseOxmlElement):
    @property
    def graphicData(self) -> CT_GraphicalObjectData:
        """Required ``<a:graphicData>`` child element."""
        ...

    @property
    def chart(self) -> CT_Chart | None: ...

class CT_GraphicalObjectData(BaseShapeElement):
    @property
    def chart(self) -> CT_Chart | None:
        """``<c:chart>`` child element or |None| if not present."""
        ...

    def get_or_add_chart(self) -> CT_Chart:
        """Return the ``<c:chart>`` child element, newly added if not present."""
        ...

    @property
    def tbl(self) -> CT_Table | None:
        """``<a:tbl>`` child element or |None| if not present."""
        ...

    def get_or_add_tbl(self) -> CT_Table:
        """Return the ``<a:tbl>`` child element, newly added if not present."""
        ...

    @property
    def uri(self) -> str:
        """XsdString type-converted value of ``uri`` attribute."""
        ...

    @uri.setter
    def uri(self, value: str) -> None: ...
    @property
    def blob_rId(self) -> str | None: ...
    @property
    def is_embedded_ole_obj(self) -> bool | None: ...
    @property
    def progId(self) -> str | None: ...
    @property
    def showAsIcon(self) -> bool | None: ...

class CT_GraphicalObjectFrame(BaseShapeElement):
    @property
    def nvGraphicFramePr(self) -> CT_GraphicalObjectFrameNonVisual:
        """Required ``<p:nvGraphicFramePr>`` child element."""
        ...

    @property
    def xfrm(self) -> CT_Transform2D:
        """Required ``<p:xfrm>`` child element."""
        ...

    @property
    def graphic(self) -> CT_GraphicalObject:
        """Required ``<a:graphic>`` child element."""
        ...

    @property
    def chart(self) -> CT_Chart | None: ...
    @property
    def chart_rId(self) -> str | None: ...
    def get_or_add_xfrm(self) -> CT_Transform2D: ...
    @property
    def graphicData(self) -> CT_GraphicalObjectData: ...
    @property
    def graphicData_uri(self) -> str: ...
    @property
    def has_oleobj(self) -> bool: ...
    @property
    def is_embedded_ole_obj(self) -> bool | None: ...
    @classmethod
    def new_chart_graphicFrame(
        cls, id_: int, name: str, rId: str, x: int, y: int, cx: int, cy: int
    ) -> CT_GraphicalObjectFrame: ...
    @classmethod
    def new_graphicFrame(cls, id_: int, name: str, x: int, y: int, cx: int, cy: int) -> CT_GraphicalObjectFrame: ...
    @classmethod
    def new_ole_object_graphicFrame(
        cls,
        id_: int,
        name: str,
        ole_object_rId: str,
        progId: str,
        icon_rId: str,
        x: int,
        y: int,
        cx: int,
        cy: int,
        imgW: int,
        imgH: int,
    ) -> CT_GraphicalObjectFrame: ...
    @classmethod
    def new_table_graphicFrame(
        cls, id_: int, name: str, rows: int, cols: int, x: int, y: int, cx: int, cy: int
    ) -> CT_GraphicalObjectFrame: ...

class CT_GraphicalObjectFrameNonVisual(BaseOxmlElement):
    @property
    def cNvPr(self) -> CT_NonVisualDrawingProps:
        """Required ``<p:cNvPr>`` child element."""
        ...

    @property
    def nvPr(self) -> CT_ApplicationNonVisualDrawingProps:
        """Required ``<p:nvPr>`` child element."""
        ...

class CT_OleObject(BaseOxmlElement):
    @property
    def progId(self) -> str | None:
        """XsdString type-converted value of ``progId`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @progId.setter
    def progId(self, value: str | None) -> None: ...
    @property
    def rId(self) -> str | None:
        """XsdString type-converted value of ``r:id`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @rId.setter
    def rId(self, value: str | None) -> None: ...
    @property
    def showAsIcon(self) -> bool:
        """XsdBoolean type-converted value of ``showAsIcon`` attribute, or |False| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @showAsIcon.setter
    def showAsIcon(self, value: bool) -> None: ...
    @property
    def is_embedded(self) -> bool: ...
