from collections.abc import Generator

from lxml.etree import _Element
from pptx.enum.shapes import MSO_CONNECTOR_TYPE, PP_PLACEHOLDER
from pptx.oxml.shapes import ShapeElement
from pptx.oxml.shapes.autoshape import CT_Shape
from pptx.oxml.shapes.connector import CT_Connector
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectFrame
from pptx.oxml.shapes.picture import CT_Picture
from pptx.oxml.shapes.shared import (
    BaseShapeElement,
    CT_NonVisualDrawingProps,
    CT_Point2D,
    CT_PositiveSize2D,
    CT_Transform2D,
)
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_GroupShape(BaseShapeElement):
    _shape_tags: tuple[str, ...] = ...

    @property
    def nvGrpSpPr(self) -> CT_GroupShapeNonVisual:
        """Required ``<p:nvGrpSpPr>`` child element."""
        ...

    @property
    def grpSpPr(self) -> CT_GroupShapeProperties:
        """Required ``<p:grpSpPr>`` child element."""
        ...

    def add_autoshape(self, id_: int, name: str, prst: str, x: int, y: int, cx: int, cy: int) -> CT_Shape: ...
    def add_cxnSp(
        self,
        id_: int,
        name: str,
        type_member: MSO_CONNECTOR_TYPE,
        x: int,
        y: int,
        cx: int,
        cy: int,
        flipH: bool,
        flipV: bool,
    ) -> CT_Connector: ...
    def add_freeform_sp(self, x: int, y: int, cx: int, cy: int) -> CT_Shape: ...
    def add_grpSp(self) -> CT_GroupShape: ...
    def add_pic(self, id_: int, name: str, desc: str, rId: str, x: int, y: int, cx: int, cy: int) -> CT_Picture: ...
    def add_placeholder(
        self, id_: int, name: str, ph_type: PP_PLACEHOLDER, orient: str, sz: str, idx: int
    ) -> CT_Shape: ...
    def add_table(
        self, id_: int, name: str, rows: int, cols: int, x: int, y: int, cx: int, cy: int
    ) -> CT_GraphicalObjectFrame: ...
    def add_textbox(self, id_: int, name: str, x: int, y: int, cx: int, cy: int) -> CT_Shape: ...
    @property
    def chExt(self) -> CT_PositiveSize2D: ...
    @property
    def chOff(self) -> CT_Point2D: ...
    def get_or_add_xfrm(self) -> CT_Transform2D: ...
    def iter_ph_elms(self) -> Generator[ShapeElement]: ...
    def iter_shape_elms(self) -> Generator[ShapeElement]: ...
    @property
    def max_shape_id(self) -> int: ...
    @classmethod
    def new_grpSp(cls, id_: int, name: str) -> CT_GroupShape: ...
    def recalculate_extents(self) -> None: ...
    @property
    def xfrm(self) -> CT_Transform2D | None: ...

class CT_GroupShapeNonVisual(BaseShapeElement):
    @property
    def cNvPr(self) -> CT_NonVisualDrawingProps:
        """Required ``<p:cNvPr>`` child element."""
        ...

class CT_GroupShapeProperties(BaseOxmlElement):
    @property
    def xfrm(self) -> CT_Transform2D | None:
        """``<a:xfrm>`` child element or |None| if not present."""
        ...

    def get_or_add_xfrm(self) -> CT_Transform2D:
        """Return the ``<a:xfrm>`` child element, newly added if not present."""
        ...

    @property
    def effectLst(self) -> _Element | None:
        """``<a:effectLst>`` child element or |None| if not present."""
        ...

    def get_or_add_effectLst(self) -> _Element:
        """Return the ``<a:effectLst>`` child element, newly added if not present."""
        ...
