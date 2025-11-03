from pptx.dml.fill import FillFormat
from pptx.dml.line import LineFormat
from pptx.shared import ElementProxy
from pptx.util import lazyproperty

class ChartFormat(ElementProxy):
    """
    The |ChartFormat| object provides access to visual shape properties for
    chart elements like |Axis|, |Series|, and |MajorGridlines|. It has two
    properties, :attr:`fill` and :attr:`line`, which return a |FillFormat|
    and |LineFormat| object respectively. The |ChartFormat| object is
    provided by the :attr:`format` property on the target axis, series, etc.
    """
    @lazyproperty
    def fill(self) -> FillFormat:
        """
        |FillFormat| instance for this object, providing access to fill
        properties such as fill color.
        """
        ...

    @lazyproperty
    def line(self) -> LineFormat:
        """
        The |LineFormat| object providing access to the visual properties of
        this object, such as line color and line style.
        """
        ...
