from typing import Literal, Self

from pptx.enum.dml import MSO_COLOR_TYPE, MSO_THEME_COLOR, MSO_THEME_COLOR_INDEX
from pptx.oxml.dml.color import CT_Color, CT_SRgbColor, _BaseColorElement

class ColorFormat:
    """
    Provides access to color settings such as RGB color, theme color, and
    luminance adjustments.
    """
    def __init__(self, eg_colorChoice_parent: CT_Color, color: _Color) -> None: ...
    @property
    def brightness(self) -> float:
        """
        Read/write float value between -1.0 and 1.0 indicating the brightness
        adjustment for this color, e.g. -0.25 is 25% darker and 0.4 is 40%
        lighter. 0 means no brightness adjustment.
        """
        ...

    @brightness.setter
    def brightness(self, value: float) -> None: ...
    @classmethod
    def from_colorchoice_parent(cls, eg_colorChoice_parent: CT_Color) -> Self: ...
    @property
    def rgb(self) -> RGBColor:
        """
        |RGBColor| value of this color, or None if no RGB color is explicitly
        defined for this font. Setting this value to an |RGBColor| instance
        causes its type to change to MSO_COLOR_TYPE.RGB. If the color was a
        theme color with a brightness adjustment, the brightness adjustment
        is removed when changing it to an RGB color.
        """
        ...

    @rgb.setter
    def rgb(self, rgb: RGBColor) -> None: ...
    @property
    def theme_color(self) -> MSO_THEME_COLOR_INDEX:
        """Theme color value of this color.

        Value is a member of :ref:`MsoThemeColorIndex`, e.g.
        ``MSO_THEME_COLOR.ACCENT_1``. Raises AttributeError on access if the
        color is not type ``MSO_COLOR_TYPE.SCHEME``. Assigning a member of
        :ref:`MsoThemeColorIndex` causes the color's type to change to
        ``MSO_COLOR_TYPE.SCHEME``.
        """
        ...

    @theme_color.setter
    def theme_color(self, mso_theme_color_idx: MSO_THEME_COLOR_INDEX) -> None: ...
    @property
    def type(self) -> MSO_COLOR_TYPE:
        """
        Read-only. A value from :ref:`MsoColorType`, either RGB or SCHEME,
        corresponding to the way this color is defined, or None if no color
        is defined at the level of this font.
        """
        ...

class _Color:
    """
    Object factory for color object of the appropriate type, also the base
    class for all color type classes such as SRgbColor.
    """
    def __new__(cls, xClr: _BaseColorElement | None) -> Self: ...
    def __init__(self, xClr: _BaseColorElement | None) -> None: ...
    @property
    def brightness(self) -> float: ...
    @brightness.setter
    def brightness(self, value: float) -> None: ...
    @property
    def color_type(self) -> MSO_COLOR_TYPE: ...
    @property
    def rgb(self) -> RGBColor:
        """
        Raises TypeError on access unless overridden by subclass.
        """
        ...

    @property
    def theme_color(self) -> Literal[MSO_THEME_COLOR_INDEX.NOT_THEME_COLOR]:
        """
        Raises TypeError on access unless overridden by subclass.
        """
        ...

class _HslColor(_Color):
    @property
    def color_type(self) -> Literal[MSO_COLOR_TYPE.HSL]: ...

class _NoneColor(_Color):
    @property
    def color_type(self) -> None: ...
    @property
    def theme_color(self):
        """
        Raise TypeError on attempt to access .theme_color when no color
        choice is present.
        """
        ...

class _PrstColor(_Color):
    @property
    def color_type(self) -> Literal[MSO_COLOR_TYPE.PRESET]: ...

class _SchemeColor(_Color):
    def __init__(self, schemeClr) -> None: ...
    @property
    def color_type(self) -> Literal[MSO_COLOR_TYPE.SCHEME]: ...
    @property
    def theme_color(self) -> MSO_THEME_COLOR | None:
        """
        Theme color value of this color, one of those defined in the
        MSO_THEME_COLOR enumeration, e.g. MSO_THEME_COLOR.ACCENT_1. None if
        no theme color is explicitly defined for this font. Setting this to a
        value in MSO_THEME_COLOR causes the color's type to change to
        ``MSO_COLOR_TYPE.SCHEME``.
        """
        ...

    @theme_color.setter
    def theme_color(self, mso_theme_color_idx: MSO_THEME_COLOR) -> None: ...

class _ScRgbColor(_Color):
    @property
    def color_type(self) -> Literal[MSO_COLOR_TYPE.SCRGB]: ...

class _SRgbColor(_Color):
    def __init__(self, srgbClr: CT_SRgbColor) -> None: ...
    @property
    def color_type(self) -> Literal[MSO_COLOR_TYPE.RGB]: ...
    @property
    def rgb(self) -> RGBColor:
        """
        |RGBColor| value of this color, corresponding to the value in the
        required ``val`` attribute of the ``<a:srgbColr>`` element.
        """
        ...

    @rgb.setter
    def rgb(self, rgb) -> None: ...

class _SysColor(_Color):
    @property
    def color_type(self) -> Literal[MSO_COLOR_TYPE.SYSTEM]: ...

class RGBColor(tuple[int, int, int]):
    """
    Immutable value object defining a particular RGB color.
    """
    def __new__(cls, r: int, g: int, b: int) -> Self: ...
    def __str__(self) -> str:
        """
        Return a hex string rgb value, like '3C2F80'
        """
        ...

    @classmethod
    def from_string(cls, rgb_hex_str: str) -> Self:
        """
        Return a new instance from an RGB color hex string like ``'3C2F80'``.
        """
        ...
