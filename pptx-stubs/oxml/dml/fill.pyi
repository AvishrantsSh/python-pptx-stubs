from pptx.enum.dml import MSO_PATTERN_TYPE
from pptx.oxml.dml.color import (
    ColorChoice,
    CT_Color,
    CT_HslColor,
    CT_PresetColor,
    CT_SchemeColor,
    CT_ScRgbColor,
    CT_SRgbColor,
    CT_SystemColor,
)
from pptx.oxml.shapes.autoshape import CT_Path2D
from pptx.oxml.xmlchemy import BaseOxmlElement

type FillProperty = (
    CT_NoFillProperties
    | "CT_SolidColorFillProperties"
    | "CT_GradientFillProperties"
    | "CT_BlipFillProperties"
    | "CT_PatternFillProperties"
    | "CT_GroupFillProperties"
)

class CT_Blip(BaseOxmlElement):
    @property
    def rEmbed(self) -> str | None:
        """ST_RelationshipId type-converted value of ``r:embed`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @rEmbed.setter
    def rEmbed(self, value: str | None) -> None: ...

class CT_BlipFillProperties(BaseOxmlElement):
    @property
    def blip(self) -> CT_Blip | None:
        """``<a:blip>`` child element or |None| if not present."""
        ...

    def get_or_add_blip(self) -> CT_Blip:
        """Return the ``<a:blip>`` child element, newly added if not present."""
        ...

    @property
    def srcRect(self) -> CT_RelativeRect | None:
        """``<a:srcRect>`` child element or |None| if not present."""
        ...

    def get_or_add_srcRect(self) -> CT_RelativeRect:
        """Return the ``<a:srcRect>`` child element, newly added if not present."""
        ...

    def crop(self, cropping: tuple[float, float, float, float]) -> None: ...

class CT_GradientFillProperties(BaseOxmlElement):
    @property
    def gsLst(self) -> CT_GradientStopList | None:
        """``<a:gsLst>`` child element or |None| if not present."""
        ...

    def get_or_add_gsLst(self) -> CT_GradientStopList:
        """Return the ``<a:gsLst>`` child element, newly added if not present."""
        ...

    @property
    def lin(self) -> CT_LinearShadeProperties | None:
        """``<a:lin>`` child element or |None| if not present."""
        ...

    def get_or_add_lin(self) -> CT_LinearShadeProperties:
        """Return the ``<a:lin>`` child element, newly added if not present."""
        ...

    @property
    def path(self) -> CT_Path2D | None:
        """``<a:path>`` child element or |None| if not present."""
        ...

    def get_or_add_path(self) -> CT_Path2D:
        """Return the ``<a:path>`` child element, newly added if not present."""
        ...

    @classmethod
    def new_gradFill(cls) -> CT_GradientFillProperties:
        """Return newly-created "loose" default gradient subtree."""
        ...

class CT_GradientStop(BaseOxmlElement):
    @property
    def scrgbClr(self) -> CT_ScRgbColor:
        """``<a:scrgbClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_scrgbClr(self) -> CT_ScRgbColor:
        """Return the ``<a:scrgbClr>`` child, replacing any other group element if found."""
        ...

    @property
    def srgbClr(self) -> CT_SRgbColor:
        """``<a:srgbClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_srgbClr(self) -> CT_SRgbColor:
        """Return the ``<a:srgbClr>`` child, replacing any other group element if found."""
        ...

    @property
    def hslClr(self) -> CT_HslColor:
        """``<a:hslClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_hslClr(self) -> CT_HslColor:
        """Return the ``<a:hslClr>`` child, replacing any other group element if found."""
        ...

    @property
    def sysClr(self) -> CT_SystemColor:
        """``<a:sysClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_sysClr(self) -> CT_SystemColor:
        """Return the ``<a:sysClr>`` child, replacing any other group element if found."""
        ...

    @property
    def schemeClr(self) -> CT_SchemeColor:
        """``<a:schemeClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_schemeClr(self) -> CT_SchemeColor:
        """Return the ``<a:schemeClr>`` child, replacing any other group element if found."""
        ...

    @property
    def prstClr(self) -> CT_PresetColor:
        """``<a:prstClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_prstClr(self) -> CT_PresetColor:
        """Return the ``<a:prstClr>`` child, replacing any other group element if found."""
        ...

    @property
    def eg_colorChoice(self) -> ColorChoice | None:
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...

    @property
    def pos(self) -> float:
        """ST_PositiveFixedPercentage type-converted value of ``pos`` attribute."""
        ...

    @pos.setter
    def pos(self, value: float) -> None: ...

class CT_GradientStopList(BaseOxmlElement):
    @property
    def gs_lst(self) -> list[CT_GradientStop]:
        """A list containing each of the ``<a:gs>`` child elements, in the order they appear."""
        ...

    def add_gs(self) -> CT_GradientStop:
        """Add a new ``<a:gs>`` child element unconditionally, inserted in the correct sequence."""
        ...

    @classmethod
    def new_gsLst(cls) -> CT_GradientStopList: ...

class CT_GroupFillProperties(BaseOxmlElement): ...

class CT_LinearShadeProperties(BaseOxmlElement):
    @property
    def ang(self) -> float | None:
        """ST_PositiveFixedAngle type-converted value of ``ang`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @ang.setter
    def ang(self, value: float | None) -> None: ...

class CT_NoFillProperties(BaseOxmlElement): ...

class CT_PatternFillProperties(BaseOxmlElement):
    @property
    def fgClr(self) -> CT_Color | None:
        """``<a:fgClr>`` child element or |None| if not present."""
        ...

    def get_or_add_fgClr(self) -> CT_Color:
        """Return the ``<a:fgClr>`` child element, newly added if not present."""
        ...

    @property
    def bgClr(self) -> CT_Color | None:
        """``<a:bgClr>`` child element or |None| if not present."""
        ...

    def get_or_add_bgClr(self) -> CT_Color:
        """Return the ``<a:bgClr>`` child element, newly added if not present."""
        ...

    @property
    def prst(self) -> MSO_PATTERN_TYPE | None:
        """MSO_PATTERN_TYPE type-converted value of ``prst`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @prst.setter
    def prst(self, value: MSO_PATTERN_TYPE | None) -> None: ...

class CT_RelativeRect(BaseOxmlElement):
    @property
    def l(self) -> float:
        """ST_Percentage type-converted value of ``l`` attribute, or |0.0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @l.setter
    def l(self, value: float) -> None: ...
    @property
    def t(self) -> float:
        """ST_Percentage type-converted value of ``t`` attribute, or |0.0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @t.setter
    def t(self, value: float) -> None: ...
    @property
    def r(self) -> float:
        """ST_Percentage type-converted value of ``r`` attribute, or |0.0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def b(self) -> float:
        """ST_Percentage type-converted value of ``b`` attribute, or |0.0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @b.setter
    def b(self, value: float) -> None: ...

class CT_SolidColorFillProperties(BaseOxmlElement):
    @property
    def scrgbClr(self) -> CT_ScRgbColor:
        """``<a:scrgbClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_scrgbClr(self) -> CT_ScRgbColor:
        """Return the ``<a:scrgbClr>`` child, replacing any other group element if found."""
        ...

    @property
    def srgbClr(self) -> CT_SRgbColor:
        """``<a:srgbClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_srgbClr(self) -> CT_SRgbColor:
        """Return the ``<a:srgbClr>`` child, replacing any other group element if found."""
        ...

    @property
    def hslClr(self) -> CT_HslColor:
        """``<a:hslClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_hslClr(self) -> CT_HslColor:
        """Return the ``<a:hslClr>`` child, replacing any other group element if found."""
        ...

    @property
    def sysClr(self) -> CT_SystemColor:
        """``<a:sysClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_sysClr(self) -> CT_SystemColor:
        """Return the ``<a:sysClr>`` child, replacing any other group element if found."""
        ...

    @property
    def schemeClr(self) -> CT_SchemeColor:
        """``<a:schemeClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_schemeClr(self) -> CT_SchemeColor:
        """Return the ``<a:schemeClr>`` child, replacing any other group element if found."""
        ...

    @property
    def prstClr(self) -> CT_PresetColor:
        """``<a:prstClr>`` child element or |None| if not present."""
        ...

    def get_or_change_to_prstClr(self) -> CT_PresetColor:
        """Return the ``<a:prstClr>`` child, replacing any other group element if found."""
        ...

    @property
    def eg_colorChoice(self) -> ColorChoice | None:
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...
