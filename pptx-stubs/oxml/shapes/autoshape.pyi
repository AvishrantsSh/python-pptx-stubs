from collections.abc import Callable

from lxml.etree import _Element
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE, PP_PLACEHOLDER
from pptx.oxml.shapes.shared import (
    BaseShapeElement,
    CT_ApplicationNonVisualDrawingProps,
    CT_LineProperties,
    CT_NonVisualDrawingProps,
    CT_ShapeProperties,
)
from pptx.oxml.text import CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.util import Length

class CT_AdjPoint2D(BaseOxmlElement):
    @property
    def x(self) -> Length:
        """ST_Coordinate type-converted value of ``x`` attribute."""
        ...

    @x.setter
    def x(self, value: Length) -> None: ...
    @property
    def y(self) -> Length:
        """ST_Coordinate type-converted value of ``y`` attribute."""
        ...

    @y.setter
    def y(self, value: Length) -> None: ...

class CT_CustomGeometry2D(BaseOxmlElement):
    @property
    def pathLst(self) -> CT_Path2DList | None:
        """``<a:pathLst>`` child element or |None| if not present."""
        ...

    def get_or_add_pathLst(self) -> CT_Path2DList:
        """Return the ``<a:pathLst>`` child element, newly added if not present."""
        ...

class CT_GeomGuide(BaseOxmlElement):
    @property
    def name(self) -> str:
        """XsdString type-converted value of ``name`` attribute."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...
    @property
    def fmla(self) -> str:
        """XsdString type-converted value of ``fmla`` attribute."""
        ...

    @fmla.setter
    def fmla(self, value: str) -> None: ...

class CT_GeomGuideList(BaseOxmlElement):
    _add_gd: Callable[[], CT_GeomGuide]

    @property
    def gd_lst(self) -> list[CT_GeomGuide]:
        """A list containing each of the ``<a:gd>`` child elements, in the order they appear."""
        ...

class CT_NonVisualDrawingShapeProps(BaseShapeElement):
    @property
    def spLocks(self) -> _Element | None:
        """``<a:spLocks>`` child element or |None| if not present."""
        ...

    def get_or_add_spLocks(self) -> _Element:
        """Return the ``<a:spLocks>`` child element, newly added if not present."""
        ...

    @property
    def txBox(self) -> bool | None:
        """XsdBoolean type-converted value of ``txBox`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @txBox.setter
    def txBox(self, value: bool | None) -> None: ...

class CT_Path2D(BaseOxmlElement):
    _add_close: Callable[[], CT_Path2DClose]
    _add_lnTo: Callable[[], CT_Path2DLineTo]
    _add_moveTo: Callable[[], CT_Path2DMoveTo]

    @property
    def close_lst(self) -> list[CT_Path2DClose]:
        """A list containing each of the ``<a:close>`` child elements, in the order they appear."""
        ...

    @property
    def lnTo_lst(self) -> list[CT_Path2DLineTo]:
        """A list containing each of the ``<a:lnTo>`` child elements, in the order they appear."""
        ...

    @property
    def moveTo_lst(self) -> list[CT_Path2DMoveTo]:
        """A list containing each of the ``<a:moveTo>`` child elements, in the order they appear."""
        ...

    @property
    def w(self) -> Length | None:
        """ST_PositiveCoordinate type-converted value of ``w`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @w.setter
    def w(self, value: Length | None) -> None: ...
    @property
    def h(self) -> Length | None:
        """ST_PositiveCoordinate type-converted value of ``h`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @h.setter
    def h(self, value: Length | None) -> None: ...
    def add_close(self) -> CT_Path2DClose: ...
    def add_lnTo(self, x: Length, y: Length) -> CT_Path2DLineTo: ...
    def add_moveTo(self, x: Length, y: Length) -> CT_Path2DMoveTo: ...

class CT_Path2DClose(BaseOxmlElement): ...

class CT_Path2DLineTo(BaseOxmlElement):
    @property
    def pt(self) -> CT_AdjPoint2D | None:
        """``<a:pt>`` child element or |None| if not present."""
        ...

    def get_or_add_pt(self) -> CT_AdjPoint2D:
        """Return the ``<a:pt>`` child element, newly added if not present."""
        ...

class CT_Path2DList(BaseOxmlElement):
    _add_path: Callable[[], CT_Path2D]

    @property
    def path_lst(self) -> list[CT_Path2D]: ...
    def add_path(self, w: Length, h: Length) -> CT_Path2D: ...

class CT_Path2DMoveTo(BaseOxmlElement):
    _add_pt: Callable[[], CT_AdjPoint2D]

    @property
    def pt(self) -> CT_AdjPoint2D | None:
        """``<a:pt>`` child element or |None| if not present."""
        ...

    def get_or_add_pt(self) -> CT_AdjPoint2D:
        """Return the ``<a:pt>`` child element, newly added if not present."""
        ...

class CT_PresetGeometry2D(BaseOxmlElement):
    """`a:prstGeom` custom element class."""

    _add_avLst: Callable[[], CT_GeomGuideList]
    _remove_avLst: Callable[[], None]

    @property
    def avLst(self) -> CT_GeomGuideList | None:
        """``<a:avLst>`` child element or |None| if not present."""
        ...

    def get_or_add_avLst(self) -> CT_GeomGuideList:
        """Return the ``<a:avLst>`` child element, newly added if not present."""
        ...

    @property
    def prst(self) -> MSO_AUTO_SHAPE_TYPE:
        """MSO_AUTO_SHAPE_TYPE type-converted value of ``prst`` attribute."""
        ...

    @prst.setter
    def prst(self, value: MSO_AUTO_SHAPE_TYPE) -> None: ...
    @property
    def gd_lst(self) -> list[CT_GeomGuide]:
        """Sequence of `a:gd` element children of `a:avLst`. Empty if none are present."""
        ...

    def rewrite_guides(self, guides: list[tuple[str, int]]) -> None:
        """Replace any `a:gd` element children of `a:avLst` with ones forme from `guides`."""
        ...

class CT_Shape(BaseShapeElement):
    """`p:sp` custom element class."""

    get_or_add_txBody: Callable[[], CT_TextBody]

    @property
    def nvSpPr(self) -> CT_ShapeNonVisual:
        """Required ``<p:nvSpPr>`` child element."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties:
        """Required ``<p:spPr>`` child element."""
        ...

    @property
    def txBody(self) -> CT_TextBody | None:
        """``<p:txBody>`` child element or |None| if not present."""
        ...

    def get_or_add_txBody(self) -> CT_TextBody:
        """Return the ``<p:txBody>`` child element, newly added if not present."""
        ...

    def add_path(self, w: Length, h: Length) -> CT_Path2D: ...
    def get_or_add_ln(self) -> CT_LineProperties: ...
    @property
    def has_custom_geometry(self) -> bool: ...
    @property
    def is_autoshape(self) -> bool: ...
    @property
    def is_textbox(self) -> bool: ...
    @property
    def ln(self) -> CT_LineProperties | None: ...
    @staticmethod
    def new_autoshape_sp(id_: int, name: str, prst: str, left: int, top: int, width: int, height: int) -> CT_Shape: ...
    @staticmethod
    def new_freeform_sp(shape_id: int, name: str, x: int, y: int, cx: int, cy: int) -> CT_Shape: ...
    @staticmethod
    def new_placeholder_sp(id_: int, name: str, ph_type: PP_PLACEHOLDER, orient: str, sz, idx) -> CT_Shape: ...
    @staticmethod
    def new_textbox_sp(id_: int, name, left: str, top: int, width: int, height: int) -> CT_Shape: ...
    @property
    def prst(self) -> MSO_AUTO_SHAPE_TYPE | None: ...
    @property
    def prstGeom(self) -> CT_PresetGeometry2D | None: ...

class CT_ShapeNonVisual(BaseShapeElement):
    @property
    def cNvPr(self) -> CT_NonVisualDrawingProps:
        """Required ``<p:cNvPr>`` child element."""
        ...

    @property
    def cNvSpPr(self) -> CT_NonVisualDrawingShapeProps:
        """Required ``<p:cNvSpPr>`` child element."""
        ...

    @property
    def nvPr(self) -> CT_ApplicationNonVisualDrawingProps:
        """Required ``<p:nvPr>`` child element."""
        ...
