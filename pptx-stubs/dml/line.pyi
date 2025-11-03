from pptx.dml.color import ColorFormat
from pptx.dml.fill import FillFormat
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.util import Length, lazyproperty

class LineFormat:
    """Provides access to line properties such as color, style, and width.

    A LineFormat object is typically accessed via the ``.line`` property of
    a shape such as |Shape| or |Picture|.
    """
    def __init__(self, parent) -> None: ...
    @lazyproperty
    def color(self) -> ColorFormat:
        """
        The |ColorFormat| instance that provides access to the color settings
        for this line. Essentially a shortcut for ``line.fill.fore_color``.
        As a side-effect, accessing this property causes the line fill type
        to be set to ``MSO_FILL.SOLID``. If this sounds risky for your use
        case, use ``line.fill.type`` to non-destructively discover the
        existing fill type.
        """
        ...

    @property
    def dash_style(self) -> MSO_LINE_DASH_STYLE | None:
        """Return value indicating line style.

        Returns a member of :ref:`MsoLineDashStyle` indicating line style, or
        |None| if no explicit value has been set. When no explicit value has
        been set, the line dash style is inherited from the style hierarchy.

        Assigning |None| removes any existing explicitly-defined dash style.
        """
        ...

    @dash_style.setter
    def dash_style(self, dash_style: MSO_LINE_DASH_STYLE | None) -> None: ...
    @lazyproperty
    def fill(self) -> FillFormat:
        """
        |FillFormat| instance for this line, providing access to fill
        properties such as foreground color.
        """
        ...

    @property
    def width(self) -> Length:
        """
        The width of the line expressed as an integer number of :ref:`English
        Metric Units <EMU>`. The returned value is an instance of |Length|,
        a value class having properties such as `.inches`, `.cm`, and `.pt`
        for converting the value into convenient units.
        """
        ...

    @width.setter
    def width(self, emu: Length) -> None: ...
