from collections.abc import Callable
from typing import Literal

from lxml.etree import _Element
from pptx.enum.lang import MSO_LANGUAGE_ID
from pptx.enum.text import MSO_AUTO_SIZE, MSO_TEXT_UNDERLINE_TYPE, MSO_VERTICAL_ANCHOR, PP_PARAGRAPH_ALIGNMENT
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
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.util import Length

type AutoFitType = Literal[MSO_AUTO_SIZE.NONE, MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE, MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT]

class CT_RegularTextRun(BaseOxmlElement):
    @property
    def rPr(self) -> CT_TextCharacterProperties | None:
        """``<a:rPr>`` child element or |None| if not present."""
        ...

    def get_or_add_rPr(self) -> CT_TextCharacterProperties:
        """Return the ``<a:rPr>`` child element, newly added if not present."""
        ...

    @property
    def t(self) -> _Element:
        """Required ``<a:t>`` child element."""
        ...

    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...

class CT_TextBody(BaseOxmlElement):
    @property
    def bodyPr(self) -> CT_TextBodyProperties:
        """Required ``<a:bodyPr>`` child element."""
        ...

    @property
    def p_lst(self) -> list[CT_TextParagraph]:
        """A list containing each of the ``<a:p>`` child elements, in the order they appear."""
        ...

    def add_p(self) -> CT_TextParagraph:
        """Add a new ``<a:p>`` child element unconditionally, inserted in the correct sequence."""
        ...

    def clear_content(self) -> None: ...
    @property
    def defRPr(self) -> CT_TextCharacterProperties: ...
    @property
    def is_empty(self) -> bool:
        """True if only a single empty `a:p` element is present."""
        ...

    @classmethod
    def new(cls) -> CT_TextBody: ...
    @classmethod
    def new_a_txBody(cls) -> CT_TextBody: ...
    @classmethod
    def new_p_txBody(cls) -> CT_TextBody: ...
    @classmethod
    def new_txPr(cls) -> CT_TextBody: ...
    def unclear_content(self) -> None: ...

class CT_TextBodyProperties(BaseOxmlElement):
    _add_noAutofit: Callable[[], _Element]
    _add_normAutofit: Callable[[], CT_TextNormalAutofit]
    _add_spAutoFit: Callable[[], _Element]
    _remove_eg_textAutoFit: Callable[[], None]

    @property
    def noAutofit(self) -> _Element:
        """``<a:noAutofit>`` child element or |None| if not present."""
        ...

    def get_or_change_to_noAutofit(self) -> _Element:
        """Return the ``<a:noAutofit>`` child, replacing any other group element if found."""
        ...

    @property
    def normAutofit(self) -> CT_TextNormalAutofit:
        """``<a:normAutofit>`` child element or |None| if not present."""
        ...

    def get_or_change_to_normAutofit(self) -> CT_TextNormalAutofit:
        """Return the ``<a:normAutofit>`` child, replacing any other group element if found."""
        ...

    @property
    def spAutoFit(self) -> _Element:
        """``<a:spAutoFit>`` child element or |None| if not present."""
        ...

    def get_or_change_to_spAutoFit(self) -> _Element:
        """Return the ``<a:spAutoFit>`` child, replacing any other group element if found."""
        ...

    @property
    def eg_textAutoFit(self) -> _Element | CT_TextNormalAutofit | _Element | None:
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...

    @property
    def lIns(self) -> Length:
        """ST_Coordinate32 type-converted value of ``lIns`` attribute, or |91440| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @lIns.setter
    def lIns(self, value: Length) -> None: ...
    @property
    def tIns(self) -> Length:
        """ST_Coordinate32 type-converted value of ``tIns`` attribute, or |45720| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @tIns.setter
    def tIns(self, value: Length) -> None: ...
    @property
    def rIns(self) -> Length:
        """ST_Coordinate32 type-converted value of ``rIns`` attribute, or |91440| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @rIns.setter
    def rIns(self, value: Length) -> None: ...
    @property
    def bIns(self) -> Length:
        """ST_Coordinate32 type-converted value of ``bIns`` attribute, or |45720| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @bIns.setter
    def bIns(self, value: Length) -> None: ...
    @property
    def anchor(self) -> MSO_VERTICAL_ANCHOR | None:
        """MSO_VERTICAL_ANCHOR type-converted value of ``anchor`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @anchor.setter
    def anchor(self, value: MSO_VERTICAL_ANCHOR | None) -> None: ...
    @property
    def wrap(self) -> str | None:
        """ST_TextWrappingType type-converted value of ``wrap`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @wrap.setter
    def wrap(self, value: str | None) -> None: ...
    @property
    def autofit(self) -> AutoFitType | None: ...
    @autofit.setter
    def autofit(self, value: AutoFitType | None) -> None: ...

class CT_TextCharacterProperties(BaseOxmlElement):
    _remove_latin: Callable[[], None]
    _remove_hlinkClick: Callable[[], None]
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
    def eg_fillProperties(self) -> FillProperty | None:
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...

    @property
    def latin(self) -> CT_TextFont | None:
        """``<a:latin>`` child element or |None| if not present."""
        ...

    def get_or_add_latin(self) -> CT_TextFont:
        """Return the ``<a:latin>`` child element, newly added if not present."""
        ...

    @property
    def hlinkClick(self) -> CT_Hyperlink | None:
        """``<a:hlinkClick>`` child element or |None| if not present."""
        ...

    def get_or_add_hlinkClick(self) -> CT_Hyperlink:
        """Return the ``<a:hlinkClick>`` child element, newly added if not present."""
        ...

    @property
    def lang(self) -> MSO_LANGUAGE_ID | None:
        """MSO_LANGUAGE_ID type-converted value of ``lang`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @lang.setter
    def lang(self, value: MSO_LANGUAGE_ID | None) -> None: ...
    @property
    def sz(self) -> int | None:
        """ST_TextFontSize type-converted value of ``sz`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @sz.setter
    def sz(self, value: int | None) -> None: ...
    @property
    def b(self) -> bool | None:
        """XsdBoolean type-converted value of ``b`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @b.setter
    def b(self, value: bool | None) -> None: ...
    @property
    def i(self) -> bool | None:
        """XsdBoolean type-converted value of ``i`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @i.setter
    def i(self, value: bool | None) -> None: ...
    @property
    def u(self) -> MSO_TEXT_UNDERLINE_TYPE | None:
        """MSO_TEXT_UNDERLINE_TYPE type-converted value of ``u`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @u.setter
    def u(self, value: MSO_TEXT_UNDERLINE_TYPE | None) -> None: ...
    def add_hlinkClick(self, rId: str) -> CT_Hyperlink: ...

class CT_TextField(BaseOxmlElement):
    @property
    def rPr(self) -> CT_TextCharacterProperties | None:
        """``<a:rPr>`` child element or |None| if not present."""
        ...

    def get_or_add_rPr(self) -> CT_TextCharacterProperties:
        """Return the ``<a:rPr>`` child element, newly added if not present."""
        ...

    @property
    def t(self) -> _Element | None:
        """``<a:t>`` child element or |None| if not present."""
        ...

    def get_or_add_t(self) -> _Element:
        """Return the ``<a:t>`` child element, newly added if not present."""
        ...

    @property
    def text(self) -> str:
        """The text of the `a:t` child element."""
        ...

class CT_TextFont(BaseOxmlElement):
    @property
    def typeface(self) -> str:
        """ST_TextTypeface type-converted value of ``typeface`` attribute."""
        ...

    @typeface.setter
    def typeface(self, value: str) -> None: ...

class CT_TextLineBreak(BaseOxmlElement):
    @property
    def rPr(self) -> CT_TextCharacterProperties | None:
        """``<a:rPr>`` child element or |None| if not present."""
        ...

    def get_or_add_rPr(self) -> CT_TextCharacterProperties:
        """Return the ``<a:rPr>`` child element, newly added if not present."""
        ...

    @property
    def text(self) -> Literal["\v"]: ...

class CT_TextNormalAutofit(BaseOxmlElement):
    @property
    def fontScale(self) -> float:
        """ST_TextFontScalePercentOrPercentString type-converted value of ``fontScale`` attribute, or |100.0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @fontScale.setter
    def fontScale(self, value: float) -> None: ...

class CT_TextParagraph(BaseOxmlElement):
    _add_br: Callable[[], CT_TextLineBreak]
    _add_r: Callable[[], CT_RegularTextRun]
    @property
    def pPr(self) -> CT_TextParagraphProperties | None:
        """``<a:pPr>`` child element or |None| if not present."""
        ...

    def get_or_add_pPr(self) -> CT_TextParagraphProperties:
        """Return the ``<a:pPr>`` child element, newly added if not present."""
        ...

    @property
    def r_lst(self) -> list[CT_RegularTextRun]:
        """A list containing each of the ``<a:r>`` child elements, in the order they appear."""
        ...

    @property
    def br_lst(self) -> list[CT_TextLineBreak]:
        """A list containing each of the ``<a:br>`` child elements, in the order they appear."""
        ...

    @property
    def endParaRPr(self) -> CT_TextCharacterProperties | None:
        """``<a:endParaRPr>`` child element or |None| if not present."""
        ...

    def get_or_add_endParaRPr(self) -> CT_TextCharacterProperties:
        """Return the ``<a:endParaRPr>`` child element, newly added if not present."""
        ...

    def add_br(self) -> CT_TextLineBreak: ...
    def add_r(self, text: str | None = ...) -> CT_RegularTextRun: ...
    def append_text(self, text: str) -> None: ...
    @property
    def content_children(self) -> tuple[CT_RegularTextRun | CT_TextLineBreak | CT_TextField, ...]: ...
    @property
    def text(self) -> str: ...

class CT_TextParagraphProperties(BaseOxmlElement):
    _add_lnSpc: Callable[[], CT_TextSpacing]
    _add_spcAft: Callable[[], CT_TextSpacing]
    _add_spcBef: Callable[[], CT_TextSpacing]
    _remove_lnSpc: Callable[[], None]
    _remove_spcAft: Callable[[], None]
    _remove_spcBef: Callable[[], None]
    _tag_seq = ...
    @property
    def lnSpc(self) -> CT_TextSpacing | None:
        """``<a:lnSpc>`` child element or |None| if not present."""
        ...

    def get_or_add_lnSpc(self) -> CT_TextSpacing:
        """Return the ``<a:lnSpc>`` child element, newly added if not present."""
        ...

    @property
    def spcBef(self) -> CT_TextSpacing | None:
        """``<a:spcBef>`` child element or |None| if not present."""
        ...

    def get_or_add_spcBef(self) -> CT_TextSpacing:
        """Return the ``<a:spcBef>`` child element, newly added if not present."""
        ...

    @property
    def spcAft(self) -> CT_TextSpacing | None:
        """``<a:spcAft>`` child element or |None| if not present."""
        ...

    def get_or_add_spcAft(self) -> CT_TextSpacing:
        """Return the ``<a:spcAft>`` child element, newly added if not present."""
        ...

    @property
    def defRPr(self) -> CT_TextCharacterProperties | None:
        """``<a:defRPr>`` child element or |None| if not present."""
        ...

    def get_or_add_defRPr(self) -> CT_TextCharacterProperties:
        """Return the ``<a:defRPr>`` child element, newly added if not present."""
        ...

    @property
    def lvl(self) -> int | None:
        """ST_TextIndentLevelType type-converted value of ``lvl`` attribute, or |-| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @lvl.setter
    def lvl(self, value: int | None) -> None: ...
    @property
    def algn(self) -> PP_PARAGRAPH_ALIGNMENT | None:
        """PP_PARAGRAPH_ALIGNMENT type-converted value of ``algn`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @algn.setter
    def algn(self, value: PP_PARAGRAPH_ALIGNMENT | None) -> None: ...
    @property
    def line_spacing(self) -> float | Length | None: ...
    @line_spacing.setter
    def line_spacing(self, value: float | Length | None) -> None: ...
    @property
    def space_after(self) -> Length | None: ...
    @space_after.setter
    def space_after(self, value: Length | None) -> None: ...
    @property
    def space_before(self) -> Length | None: ...
    @space_before.setter
    def space_before(self, value: Length | None) -> None: ...

class CT_TextSpacing(BaseOxmlElement):
    _remove_spcPct: Callable[[], None]
    _remove_spcPts: Callable[[], None]
    @property
    def spcPct(self) -> CT_TextSpacingPercent | None:
        """``<a:spcPct>`` child element or |None| if not present."""
        ...

    def get_or_add_spcPct(self) -> CT_TextSpacingPercent:
        """Return the ``<a:spcPct>`` child element, newly added if not present."""
        ...

    @property
    def spcPts(self) -> CT_TextSpacingPoint | None:
        """``<a:spcPts>`` child element or |None| if not present."""
        ...

    def get_or_add_spcPts(self) -> CT_TextSpacingPoint:
        """Return the ``<a:spcPts>`` child element, newly added if not present."""
        ...

    def set_spcPct(self, value: float) -> None: ...
    def set_spcPts(self, value: Length) -> None: ...

class CT_TextSpacingPercent(BaseOxmlElement):
    @property
    def val(self) -> float:
        """ST_TextSpacingPercentOrPercentString type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: float) -> None: ...

class CT_TextSpacingPoint(BaseOxmlElement):
    @property
    def val(self) -> int:
        """ST_TextSpacingPoint type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...
