from lxml.etree import _Element
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import PP_PLACEHOLDER_TYPE
from pptx.oxml.action import CT_Hyperlink
from pptx.oxml.dml.fill import (
    CT_BlipFillProperties,
    CT_GradientFillProperties,
    CT_GroupFillProperties,
    CT_NoFillProperties,
    CT_PatternFillProperties,
    CT_SolidColorFillProperties,
    FillProperty,
)
from pptx.oxml.dml.line import CT_PresetLineDashProperties
from pptx.oxml.shapes.autoshape import CT_CustomGeometry2D, CT_PresetGeometry2D
from pptx.oxml.text import CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.util import Length

class BaseShapeElement(BaseOxmlElement):
    spPr: CT_ShapeProperties
    @property
    def cx(self) -> Length: ...
    @cx.setter
    def cx(self, value: Length) -> None: ...
    @property
    def cy(self) -> Length: ...
    @cy.setter
    def cy(self, value: Length) -> None: ...
    @property
    def flipH(self) -> bool: ...
    @flipH.setter
    def flipH(self, value: bool) -> None: ...
    @property
    def flipV(self) -> bool: ...
    @flipV.setter
    def flipV(self, value: bool) -> None: ...
    def get_or_add_xfrm(self) -> CT_Transform2D: ...
    @property
    def has_ph_elm(self) -> bool: ...
    @property
    def ph(self) -> CT_Placeholder | None: ...
    @property
    def ph_idx(self) -> int: ...
    @property
    def ph_orient(self) -> str: ...
    @property
    def ph_sz(self) -> str: ...
    @property
    def ph_type(self) -> PP_PLACEHOLDER_TYPE: ...
    @property
    def rot(self) -> float: ...
    @rot.setter
    def rot(self, value: float) -> None: ...
    @property
    def shape_id(self) -> int: ...
    @property
    def shape_name(self) -> str: ...
    @property
    def txBody(self) -> CT_TextBody | None: ...
    @property
    def x(self) -> Length: ...
    @x.setter
    def x(self, value: Length) -> None: ...
    @property
    def xfrm(self) -> CT_Transform2D | None: ...
    @property
    def y(self) -> Length: ...
    @y.setter
    def y(self, value: Length) -> None: ...

class CT_ApplicationNonVisualDrawingProps(BaseOxmlElement):
    @property
    def ph(self) -> CT_Placeholder | None:
        """``<p:ph>`` child element or |None| if not present."""
        ...

    def get_or_add_ph(self) -> CT_Placeholder:
        """Return the ``<p:ph>`` child element, newly added if not present."""
        ...

class CT_LineProperties(BaseOxmlElement):
    @property
    def noFill(self) -> CT_NoFillProperties:
        """``<a:noFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_noFill(self) -> CT_NoFillProperties:
        """Return the ``<a:noFill>`` child, replacing any other group element if found."""
        ...

    @property
    def solidFill(self) -> CT_SolidColorFillProperties:
        """``<a:solidFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_solidFill(self) -> CT_SolidColorFillProperties:
        """Return the ``<a:solidFill>`` child, replacing any other group element if found."""
        ...

    @property
    def gradFill(self) -> CT_GradientFillProperties:
        """``<a:gradFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_gradFill(self) -> CT_GradientFillProperties:
        """Return the ``<a:gradFill>`` child, replacing any other group element if found."""
        ...

    @property
    def pattFill(self) -> CT_PatternFillProperties:
        """``<a:pattFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_pattFill(self) -> CT_PatternFillProperties:
        """Return the ``<a:pattFill>`` child, replacing any other group element if found."""
        ...

    @property
    def eg_lineFillProperties(
        self,
    ) -> (
        CT_NoFillProperties | CT_SolidColorFillProperties | CT_GradientFillProperties | CT_PatternFillProperties | None
    ):
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...

    @property
    def prstDash(self) -> CT_PresetLineDashProperties | None:
        """``<a:prstDash>`` child element or |None| if not present."""
        ...

    def get_or_add_prstDash(self) -> CT_PresetLineDashProperties:
        """Return the ``<a:prstDash>`` child element, newly added if not present."""
        ...

    @property
    def custDash(self) -> _Element | None:
        """``<a:custDash>`` child element or |None| if not present."""
        ...

    def get_or_add_custDash(self) -> _Element:
        """Return the ``<a:custDash>`` child element, newly added if not present."""
        ...

    @property
    def w(self) -> Length:
        """ST_LineWidth type-converted value of ``w`` attribute, or |Length(0)| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @w.setter
    def w(self, value: Length) -> None: ...
    @property
    def eg_fillProperties(
        self,
    ) -> (
        CT_NoFillProperties | CT_SolidColorFillProperties | CT_GradientFillProperties | CT_PatternFillProperties | None
    ): ...
    @property
    def prstDash_val(self) -> MSO_LINE_DASH_STYLE | None:
        """Return value of `val` attribute of `a:prstDash` child.

        Return |None| if not present.
        """
        ...

    @prstDash_val.setter
    def prstDash_val(self, val: MSO_LINE_DASH_STYLE) -> None: ...

class CT_NonVisualDrawingProps(BaseOxmlElement):
    @property
    def hlinkClick(self) -> CT_Hyperlink | None:
        """``<a:hlinkClick>`` child element or |None| if not present."""
        ...

    def get_or_add_hlinkClick(self) -> CT_Hyperlink:
        """Return the ``<a:hlinkClick>`` child element, newly added if not present."""
        ...

    @property
    def hlinkHover(self) -> CT_Hyperlink | None:
        """``<a:hlinkHover>`` child element or |None| if not present."""
        ...

    def get_or_add_hlinkHover(self) -> CT_Hyperlink:
        """Return the ``<a:hlinkHover>`` child element, newly added if not present."""
        ...

    @property
    def id(self) -> int:
        """ST_DrawingElementId type-converted value of ``id`` attribute."""
        ...

    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def name(self) -> str:
        """XsdString type-converted value of ``name`` attribute."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

class CT_Placeholder(BaseOxmlElement):
    @property
    def type(self) -> PP_PLACEHOLDER_TYPE:
        """PP_PLACEHOLDER_TYPE type-converted value of ``type`` attribute, or |PP_PLACEHOLDER_TYPE.OBJECT| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @type.setter
    def type(self, value: PP_PLACEHOLDER_TYPE) -> None: ...
    @property
    def orient(self) -> str:
        """ST_Direction type-converted value of ``orient`` attribute, or |horz| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @orient.setter
    def orient(self, value: str) -> None: ...
    @property
    def sz(self) -> str:
        """ST_PlaceholderSize type-converted value of ``sz`` attribute, or |full| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @sz.setter
    def sz(self, value: str) -> None: ...
    @property
    def idx(self) -> int:
        """XsdUnsignedInt type-converted value of ``idx`` attribute, or |0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @idx.setter
    def idx(self, value: int) -> None: ...

class CT_Point2D(BaseOxmlElement):
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

class CT_PositiveSize2D(BaseOxmlElement):
    @property
    def cx(self) -> Length:
        """ST_PositiveCoordinate type-converted value of ``cx`` attribute."""
        ...

    @cx.setter
    def cx(self, value: Length) -> None: ...
    @property
    def cy(self) -> Length:
        """ST_PositiveCoordinate type-converted value of ``cy`` attribute."""
        ...

    @cy.setter
    def cy(self, value: Length) -> None: ...

class CT_ShapeProperties(BaseOxmlElement):
    @property
    def xfrm(self) -> CT_Transform2D | None:
        """``<a:xfrm>`` child element or |None| if not present."""
        ...

    def get_or_add_xfrm(self) -> CT_Transform2D:
        """Return the ``<a:xfrm>`` child element, newly added if not present."""
        ...

    @property
    def custGeom(self) -> CT_CustomGeometry2D | None:
        """``<a:custGeom>`` child element or |None| if not present."""
        ...

    def get_or_add_custGeom(self) -> CT_CustomGeometry2D:
        """Return the ``<a:custGeom>`` child element, newly added if not present."""
        ...

    @property
    def prstGeom(self) -> CT_PresetGeometry2D | None:
        """``<a:prstGeom>`` child element or |None| if not present."""
        ...

    def get_or_add_prstGeom(self) -> CT_PresetGeometry2D:
        """Return the ``<a:prstGeom>`` child element, newly added if not present."""
        ...

    @property
    def noFill(self) -> CT_NoFillProperties:
        """``<a:noFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_noFill(self) -> CT_NoFillProperties:
        """Return the ``<a:noFill>`` child, replacing any other group element if found."""
        ...

    @property
    def solidFill(self) -> CT_SolidColorFillProperties:
        """``<a:solidFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_solidFill(self) -> CT_SolidColorFillProperties:
        """Return the ``<a:solidFill>`` child, replacing any other group element if found."""
        ...

    @property
    def gradFill(self) -> CT_GradientFillProperties:
        """``<a:gradFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_gradFill(self) -> CT_GradientFillProperties:
        """Return the ``<a:gradFill>`` child, replacing any other group element if found."""
        ...

    @property
    def blipFill(self) -> CT_BlipFillProperties:
        """``<a:blipFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_blipFill(self) -> CT_BlipFillProperties:
        """Return the ``<a:blipFill>`` child, replacing any other group element if found."""
        ...

    @property
    def pattFill(self) -> CT_PatternFillProperties:
        """``<a:pattFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_pattFill(self) -> CT_PatternFillProperties:
        """Return the ``<a:pattFill>`` child, replacing any other group element if found."""
        ...

    @property
    def grpFill(self) -> CT_GroupFillProperties:
        """``<a:grpFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_grpFill(self) -> CT_GroupFillProperties:
        """Return the ``<a:grpFill>`` child, replacing any other group element if found."""
        ...

    @property
    def eg_fillProperties(
        self,
    ) -> FillProperty | None:
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...

    @property
    def ln(self) -> CT_LineProperties | None:
        """``<a:ln>`` child element or |None| if not present."""
        ...

    def get_or_add_ln(self) -> CT_LineProperties:
        """Return the ``<a:ln>`` child element, newly added if not present."""
        ...

    @property
    def effectLst(self) -> _Element | None:
        """``<a:effectLst>`` child element or |None| if not present."""
        ...

    def get_or_add_effectLst(self) -> _Element:
        """Return the ``<a:effectLst>`` child element, newly added if not present."""
        ...

    @property
    def cx(self) -> Length | None: ...
    @property
    def cy(self) -> Length | None: ...
    @property
    def x(self) -> Length | None: ...
    @property
    def y(self) -> Length | None: ...

class CT_Transform2D(BaseOxmlElement):
    @property
    def off(self) -> CT_Point2D | None:
        """``<a:off>`` child element or |None| if not present."""
        ...

    def get_or_add_off(self) -> CT_Point2D:
        """Return the ``<a:off>`` child element, newly added if not present."""
        ...

    @property
    def ext(self) -> CT_PositiveSize2D | None:
        """``<a:ext>`` child element or |None| if not present."""
        ...

    def get_or_add_ext(self) -> CT_PositiveSize2D:
        """Return the ``<a:ext>`` child element, newly added if not present."""
        ...

    @property
    def chOff(self) -> CT_Point2D | None:
        """``<a:chOff>`` child element or |None| if not present."""
        ...

    def get_or_add_chOff(self) -> CT_Point2D:
        """Return the ``<a:chOff>`` child element, newly added if not present."""
        ...

    @property
    def chExt(self) -> CT_PositiveSize2D | None:
        """``<a:chExt>`` child element or |None| if not present."""
        ...

    def get_or_add_chExt(self) -> CT_PositiveSize2D:
        """Return the ``<a:chExt>`` child element, newly added if not present."""
        ...

    @property
    def rot(self) -> float:
        """ST_Angle type-converted value of ``rot`` attribute, or |0.0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @rot.setter
    def rot(self, value: float) -> None: ...
    @property
    def flipH(self) -> bool:
        """XsdBoolean type-converted value of ``flipH`` attribute, or |False| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @flipH.setter
    def flipH(self, value: bool) -> None: ...
    @property
    def flipV(self) -> bool:
        """XsdBoolean type-converted value of ``flipV`` attribute, or |False| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @flipV.setter
    def flipV(self, value: bool) -> None: ...
    @property
    def x(self) -> Length | None: ...
    @x.setter
    def x(self, value: Length) -> None: ...
    @property
    def y(self) -> Length | None: ...
    @y.setter
    def y(self, value: Length) -> None: ...
    @property
    def cx(self) -> Length | None: ...
    @cx.setter
    def cx(self, value: Length) -> None: ...
    @property
    def cy(self: Length) -> None: ...
    @cy.setter
    def cy(self, value: Length) -> None: ...
