from typing import Self

from pptx.enum.dml import MSO_THEME_COLOR
from pptx.oxml.xmlchemy import BaseOxmlElement

type ColorChoice = CT_ScRgbColor | CT_SRgbColor | CT_HslColor | CT_SystemColor | CT_SchemeColor | CT_PresetColor

class _BaseColorElement(BaseOxmlElement):
    @property
    def lumMod(self) -> CT_Percentage | None:
        """``<a:lumMod>`` child element or |None| if not present."""
        ...

    def get_or_add_lumMod(self) -> CT_Percentage:
        """Return the ``<a:lumMod>`` child element, newly added if not present."""
        ...

    @property
    def lumOff(self) -> CT_Percentage | None:
        """``<a:lumOff>`` child element or |None| if not present."""
        ...

    def get_or_add_lumOff(self) -> CT_Percentage:
        """Return the ``<a:lumOff>`` child element, newly added if not present."""
        ...

    def add_lumMod(self, value: float) -> CT_Percentage: ...
    def add_lumOff(self, value: float) -> CT_Percentage: ...
    def clear_lum(self) -> Self: ...

class CT_Color(BaseOxmlElement):
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

class CT_HslColor(_BaseColorElement): ...

class CT_Percentage(BaseOxmlElement):
    @property
    def val(self) -> float:
        """ST_Percentage type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: float) -> None: ...

class CT_PresetColor(_BaseColorElement): ...

class CT_SchemeColor(_BaseColorElement):
    @property
    def val(self) -> MSO_THEME_COLOR:
        """MSO_THEME_COLOR_INDEX type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: MSO_THEME_COLOR) -> None: ...

class CT_ScRgbColor(_BaseColorElement): ...

class CT_SRgbColor(_BaseColorElement):
    @property
    def val(self) -> str:
        """ST_HexColorRGB type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: str) -> None: ...

class CT_SystemColor(_BaseColorElement): ...
