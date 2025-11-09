from collections.abc import Sequence
from typing import Literal, Self

from pptx.dml.color import ColorFormat
from pptx.enum.dml import MSO_FILL_TYPE, MSO_PATTERN_TYPE
from pptx.oxml.dml.fill import (
    CT_BlipFillProperties,
    CT_GradientFillProperties,
    CT_GradientStop,
    CT_GroupFillProperties,
    CT_NoFillProperties,
    CT_PatternFillProperties,
    CT_SolidColorFillProperties,
)
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.shared import ElementProxy
from pptx.util import lazyproperty

class FillFormat:
    """Provides access to the current fill properties.

    Also provides methods to change the fill type.
    """
    def __init__(self, eg_fill_properties_parent: BaseOxmlElement, fill_obj: _Fill) -> None: ...
    @classmethod
    def from_fill_parent(cls, eg_fillProperties_parent: BaseOxmlElement) -> FillFormat:
        """
        Return a |FillFormat| instance initialized to the settings contained
        in *eg_fillProperties_parent*, which must be an element having
        EG_FillProperties in its child element sequence in the XML schema.
        """
        ...

    @property
    def back_color(self) -> ColorFormat:
        """Return a |ColorFormat| object representing background color.

        This property is only applicable to pattern fills and lines.
        """
        ...

    def background(self) -> None:
        """
        Sets the fill type to noFill, i.e. transparent.
        """
        ...

    @property
    def fore_color(self) -> ColorFormat:
        """
        Return a |ColorFormat| instance representing the foreground color of
        this fill.
        """
        ...

    def gradient(self) -> None:
        """Sets the fill type to gradient.

        If the fill is not already a gradient, a default gradient is added.
        The default gradient corresponds to the default in the built-in
        PowerPoint "White" template. This gradient is linear at angle
        90-degrees (upward), with two stops. The first stop is Accent-1 with
        tint 100%, shade 100%, and satMod 130%. The second stop is Accent-1
        with tint 50%, shade 100%, and satMod 350%.
        """
        ...

    @property
    def gradient_angle(self) -> float | None:
        """Angle in float degrees of line of a linear gradient.

        Read/Write. May be |None|, indicating the angle should be inherited
        from the style hierarchy. An angle of 0.0 corresponds to
        a left-to-right gradient. Increasing angles represent
        counter-clockwise rotation of the line, for example 90.0 represents
        a bottom-to-top gradient. Raises |TypeError| when the fill type is
        not MSO_FILL_TYPE.GRADIENT. Raises |ValueError| for a non-linear
        gradient (e.g. a radial gradient).
        """
        ...

    @gradient_angle.setter
    def gradient_angle(self, value) -> None: ...
    @property
    def gradient_stops(self) -> _GradientStops:
        """|GradientStops| object providing access to stops of this gradient.

        Raises |TypeError| when fill is not gradient (call `fill.gradient()`
        first). Each stop represents a color between which the gradient
        smoothly transitions.
        """
        ...

    @property
    def pattern(self):
        """Return member of :ref:`MsoPatternType` indicating fill pattern.

        Raises |TypeError| when fill is not patterned (call
        `fill.patterned()` first). Returns |None| if no pattern has been set;
        PowerPoint may display the default `PERCENT_5` pattern in this case.
        Assigning |None| will remove any explicit pattern setting, although
        relying on the default behavior is discouraged and may produce
        rendering differences across client applications.
        """
        ...

    @pattern.setter
    def pattern(self, pattern_type) -> None: ...
    def patterned(self) -> None:
        """Selects the pattern fill type.

        Note that calling this method does not by itself set a foreground or
        background color of the pattern. Rather it enables subsequent
        assignments to properties like fore_color to set the pattern and
        colors.
        """
        ...

    def solid(self) -> None:
        """
        Sets the fill type to solid, i.e. a solid color. Note that calling
        this method does not set a color or by itself cause the shape to
        appear with a solid color fill; rather it enables subsequent
        assignments to properties like fore_color to set the color.
        """
        ...

    @property
    def type(self) -> MSO_FILL_TYPE:
        """The type of this fill, e.g. `MSO_FILL_TYPE.SOLID`."""
        ...

class _Fill[FillElementType: (BaseOxmlElement)]:
    """
    Object factory for fill object of class matching fill element, such as
    _SolidFill for ``<a:solidFill>``; also serves as the base class for all
    fill classes
    """
    def __new__(cls, xFill: FillElementType | BaseOxmlElement) -> Self: ...
    @property
    def back_color(self) -> ColorFormat:
        """Raise TypeError for types that do not override this property."""
        ...

    @property
    def fore_color(self) -> ColorFormat:
        """Raise TypeError for types that do not override this property."""
        ...

    @property
    def pattern(self) -> MSO_PATTERN_TYPE | None:
        """Raise TypeError for fills that do not override this property."""
        ...

    @property
    def type(self) -> MSO_FILL_TYPE | None: ...

class _BlipFill(_Fill[CT_BlipFillProperties]):
    @property
    def type(self) -> Literal[MSO_FILL_TYPE.PICTURE]: ...

class _GradFill(_Fill[CT_GradientFillProperties]):
    """Proxies an `a:gradFill` element."""
    def __init__(self, gradFill: CT_GradientFillProperties) -> None: ...
    @property
    def gradient_angle(self) -> float | None:
        """Angle in float degrees of line of a linear gradient.

        Read/Write. May be |None|, indicating the angle is inherited from the
        style hierarchy. An angle of 0.0 corresponds to a left-to-right
        gradient. Increasing angles represent clockwise rotation of the line,
        for example 90.0 represents a top-to-bottom gradient. Raises
        |TypeError| when the fill type is not MSO_FILL_TYPE.GRADIENT. Raises
        |ValueError| for a non-linear gradient (e.g. a radial gradient).
        """
        ...

    @gradient_angle.setter
    def gradient_angle(self, value: float) -> None: ...
    @lazyproperty
    def gradient_stops(self) -> _GradientStops:
        """|_GradientStops| object providing access to gradient colors.

        Each stop represents a color between which the gradient smoothly
        transitions.
        """
        ...

    @property
    def type(self) -> Literal[MSO_FILL_TYPE.GRADIENT]: ...

class _GrpFill(_Fill[CT_GroupFillProperties]):
    @property
    def type(self) -> Literal[MSO_FILL_TYPE.GROUP]: ...

class _NoFill(_Fill[CT_NoFillProperties]):
    @property
    def type(self) -> Literal[MSO_FILL_TYPE.BACKGROUND]: ...

class _NoneFill(_Fill[BaseOxmlElement]):
    @property
    def type(self) -> None: ...

class _PattFill(_Fill[CT_PatternFillProperties]):
    """Provides access to patterned fill properties."""
    def __init__(self, pattFill: CT_PatternFillProperties) -> None: ...
    @lazyproperty
    def back_color(self) -> ColorFormat:
        """Return |ColorFormat| object that controls background color."""
        ...

    @lazyproperty
    def fore_color(self) -> ColorFormat:
        """Return |ColorFormat| object that controls foreground color."""
        ...

    @property
    def pattern(self) -> MSO_PATTERN_TYPE | None:
        """Return member of :ref:`MsoPatternType` indicating fill pattern.

        Returns |None| if no pattern has been set; PowerPoint may display the
        default `PERCENT_5` pattern in this case. Assigning |None| will
        remove any explicit pattern setting.
        """
        ...

    @pattern.setter
    def pattern(self, pattern_type: MSO_PATTERN_TYPE | None) -> None: ...
    @property
    def type(self) -> Literal[MSO_FILL_TYPE.PATTERNED]: ...

class _SolidFill(_Fill[CT_SolidColorFillProperties]):
    """Provides access to fill properties such as color for solid fills."""
    def __init__(self, solidFill: CT_SolidColorFillProperties) -> None: ...
    @lazyproperty
    def fore_color(self) -> ColorFormat:
        """Return |ColorFormat| object controlling fill color."""
        ...

    @property
    def type(self) -> Literal[MSO_FILL_TYPE.SOLID]: ...

class _GradientStops(Sequence[_GradientStop]):
    """Collection of |GradientStop| objects defining gradient colors.

    A gradient must have a minimum of two stops, but can have as many more
    than that as required to achieve the desired effect (three is perhaps
    most common). Stops are sequenced in the order they are transitioned
    through.
    """
    def __init__(self, gsLst: list[CT_GradientStop]) -> None: ...
    def __getitem__(self, idx: int) -> _GradientStop: ...
    def __len__(self) -> int: ...

class _GradientStop(ElementProxy):
    """A single gradient stop.

    A gradient stop defines a color and a position.
    """
    def __init__(self, gs: CT_GradientStop) -> None: ...
    @lazyproperty
    def color(self) -> ColorFormat:
        """Return |ColorFormat| object controlling stop color."""
        ...

    @property
    def position(self) -> float:
        """Location of stop in gradient path as float between 0.0 and 1.0.

        The value represents a percentage, where 0.0 (0%) represents the
        start of the path and 1.0 (100%) represents the end of the path. For
        a linear gradient, these would represent opposing extents of the
        filled area.
        """
        ...

    @position.setter
    def position(self, value: float) -> None: ...
