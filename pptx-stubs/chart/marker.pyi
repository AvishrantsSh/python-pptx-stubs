from pptx.dml.chtfmt import ChartFormat
from pptx.enum.chart import XL_MARKER_STYLE
from pptx.shared import ElementProxy
from pptx.util import lazyproperty

class Marker(ElementProxy):
    """
    Represents a data point marker, such as a diamond or circle, on
    a line-type chart.
    """
    @lazyproperty
    def format(self) -> ChartFormat:
        """
        The |ChartFormat| instance for this marker, providing access to shape
        properties such as fill and line.
        """
        ...

    @property
    def size(self) -> int | None:
        """
        An integer between 2 and 72 inclusive indicating the size of this
        marker in points. A value of |None| indicates no explicit value is
        set and the size is inherited from a higher-level setting or the
        PowerPoint default (which may be 9). Assigning |None| removes any
        explicitly assigned size, causing this value to be inherited.
        """
        ...

    @size.setter
    def size(self, value: int | None) -> None: ...
    @property
    def style(self) -> XL_MARKER_STYLE | None:
        """
        A member of the :ref:`XlMarkerStyle` enumeration indicating the shape
        of this marker. Returns |None| if no explicit style has been set,
        which corresponds to the "Automatic" option in the PowerPoint UI.
        """
        ...

    @style.setter
    def style(self, value: XL_MARKER_STYLE | None) -> None: ...
