from typing import Literal

from pptx.dml.chtfmt import ChartFormat
from pptx.enum.chart import XL_AXIS_CROSSES, XL_CATEGORY_TYPE, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.oxml.chart.axis import BaseAxisElement
from pptx.oxml.chart.shared import CT_Title
from pptx.shared import ElementProxy
from pptx.text.text import Font, TextFrame
from pptx.util import lazyproperty

class _BaseAxis:
    """Base class for chart axis objects. All axis objects share these properties."""
    def __init__(self, xAx: BaseAxisElement) -> None: ...
    @property
    def axis_title(self) -> AxisTitle:
        """An |AxisTitle| object providing access to title properties.

        Calling this property is destructive in the sense that it adds an
        axis title element (`c:title`) to the axis XML if one is not already
        present. Use :attr:`has_title` to test for presence of axis title
        non-destructively.
        """
        ...

    @lazyproperty
    def format(self) -> ChartFormat:
        """
        The |ChartFormat| object providing access to the shape formatting
        properties of this axis, such as its line color and fill.
        """
        ...

    @property
    def has_major_gridlines(self) -> bool:
        """
        Read/write boolean value specifying whether this axis has gridlines
        at its major tick mark locations. Assigning |True| to this property
        causes major gridlines to be displayed. Assigning |False| causes them
        to be removed.
        """
        ...

    @has_major_gridlines.setter
    def has_major_gridlines(self, value: bool) -> None: ...
    @property
    def has_minor_gridlines(self) -> bool:
        """
        Read/write boolean value specifying whether this axis has gridlines
        at its minor tick mark locations. Assigning |True| to this property
        causes minor gridlines to be displayed. Assigning |False| causes them
        to be removed.
        """
        ...

    @has_minor_gridlines.setter
    def has_minor_gridlines(self, value: bool) -> None: ...
    @property
    def has_title(self) -> bool:
        """Read/write boolean specifying whether this axis has a title.

        |True| if this axis has a title, |False| otherwise. Assigning |True|
        causes an axis title to be added if not already present. Assigning
        |False| causes any existing title to be deleted.
        """
        ...

    @has_title.setter
    def has_title(self, value: bool) -> None: ...
    @lazyproperty
    def major_gridlines(self) -> MajorGridlines:
        """
        The |MajorGridlines| object representing the major gridlines for
        this axis.
        """
        ...

    @property
    def major_tick_mark(self) -> XL_TICK_MARK:
        """
        Read/write :ref:`XlTickMark` value specifying the type of major tick
        mark to display on this axis.
        """
        ...

    @major_tick_mark.setter
    def major_tick_mark(self, value: XL_TICK_MARK) -> None: ...
    @property
    def maximum_scale(self: float | None):
        """
        Read/write float value specifying the upper limit of the value range
        for this axis, the number at the top or right of the vertical or
        horizontal value scale, respectively. The value |None| indicates the
        upper limit should be determined automatically based on the range of
        data point values associated with the axis.
        """
        ...

    @maximum_scale.setter
    def maximum_scale(self, value: float | None) -> None: ...
    @property
    def minimum_scale(self) -> float | None:
        """
        Read/write float value specifying lower limit of value range, the
        number at the bottom or left of the value scale. |None| if no minimum
        scale has been set. The value |None| indicates the lower limit should
        be determined automatically based on the range of data point values
        associated with the axis.
        """
        ...

    @minimum_scale.setter
    def minimum_scale(self, value: float | None) -> None: ...
    @property
    def minor_tick_mark(self) -> XL_TICK_MARK:
        """
        Read/write :ref:`XlTickMark` value specifying the type of minor tick
        mark for this axis.
        """
        ...

    @minor_tick_mark.setter
    def minor_tick_mark(self, value: XL_TICK_MARK) -> None: ...
    @property
    def reverse_order(self):
        """Read/write bool value specifying whether to reverse plotting order for axis.

        For a category axis, this reverses the order in which the categories are
        displayed. This may be desired, for example, on a (horizontal) bar-chart where
        by default the first category appears at the bottom. Since we read from
        top-to-bottom, many viewers may find it most natural for the first category to
        appear on top.

        For a value axis, it reverses the direction of increasing value from
        bottom-to-top to top-to-bottom.
        """
        ...

    @reverse_order.setter
    def reverse_order(self, value: bool) -> None: ...
    @lazyproperty
    def tick_labels(self) -> TickLabels:
        """
        The |TickLabels| instance providing access to axis tick label
        formatting properties. Tick labels are the numbers appearing on
        a value axis or the category names appearing on a category axis.
        """
        ...

    @property
    def tick_label_position(self) -> XL_TICK_LABEL_POSITION:
        """
        Read/write :ref:`XlTickLabelPosition` value specifying where the tick
        labels for this axis should appear.
        """
        ...

    @tick_label_position.setter
    def tick_label_position(self, value: XL_TICK_LABEL_POSITION | None) -> None: ...
    @property
    def visible(self) -> bool:
        """
        Read/write. |True| if axis is visible, |False| otherwise.
        """
        ...

    @visible.setter
    def visible(self, value: bool) -> None: ...

class AxisTitle(ElementProxy):
    """Provides properties for manipulating axis title."""
    def __init__(self, title: CT_Title) -> None: ...
    @lazyproperty
    def format(self) -> ChartFormat:
        """|ChartFormat| object providing access to shape formatting.

        Return the |ChartFormat| object providing shape formatting properties
        for this axis title, such as its line color and fill.
        """
        ...

    @property
    def has_text_frame(self) -> bool:
        """Read/write Boolean specifying presence of a text frame.

        Return |True| if this axis title has a text frame, and |False|
        otherwise. Assigning |True| causes a text frame to be added if not
        already present. Assigning |False| causes any existing text frame to
        be removed along with any text contained in the text frame.
        """
        ...

    @has_text_frame.setter
    def has_text_frame(self, value: bool) -> None: ...
    @property
    def text_frame(self) -> TextFrame:
        """|TextFrame| instance for this axis title.

        Return a |TextFrame| instance allowing read/write access to the text
        of this axis title and its text formatting properties. Accessing this
        property is destructive as it adds a new text frame if not already
        present.
        """
        ...

class CategoryAxis(_BaseAxis):
    """A category axis of a chart."""
    @property
    def category_type(self) -> Literal[XL_CATEGORY_TYPE.CATEGORY_SCALE]:
        """
        A member of :ref:`XlCategoryType` specifying the scale type of this
        axis. Unconditionally ``CATEGORY_SCALE`` for a |CategoryAxis| object.
        """
        ...

class DateAxis(_BaseAxis):
    """A category axis with dates as its category labels.

    This axis-type has some special display behaviors such as making length of equal
    periods equal and normalizing month start dates despite unequal month lengths.
    """
    @property
    def category_type(self) -> Literal[XL_CATEGORY_TYPE.TIME_SCALE]:
        """
        A member of :ref:`XlCategoryType` specifying the scale type of this
        axis. Unconditionally ``TIME_SCALE`` for a |DateAxis| object.
        """
        ...

class MajorGridlines(ElementProxy):
    """Provides access to the properties of the major gridlines appearing on an axis."""
    def __init__(self, xAx: BaseAxisElement) -> None: ...
    @lazyproperty
    def format(self) -> ChartFormat:
        """
        The |ChartFormat| object providing access to the shape formatting
        properties of this data point, such as line and fill.
        """
        ...

class TickLabels:
    """A service class providing access to formatting of axis tick mark labels."""
    def __init__(self, xAx_elm: BaseAxisElement) -> None: ...
    @lazyproperty
    def font(self) -> Font:
        """
        The |Font| object that provides access to the text properties for
        these tick labels, such as bold, italic, etc.
        """
        ...

    @property
    def number_format(self) -> str:
        """
        Read/write string (e.g. "$#,##0.00") specifying the format for the
        numbers on this axis. The syntax for these strings is the same as it
        appears in the PowerPoint or Excel UI. Returns 'General' if no number
        format has been set. Note that this format string has no effect on
        rendered tick labels when :meth:`number_format_is_linked` is |True|.
        Assigning a format string to this property automatically sets
        :meth:`number_format_is_linked` to |False|.
        """
        ...

    @number_format.setter
    def number_format(self, value: str) -> None: ...
    @property
    def number_format_is_linked(self) -> bool:
        """
        Read/write boolean specifying whether number formatting should be
        taken from the source spreadsheet rather than the value of
        :meth:`number_format`.
        """
        ...

    @number_format_is_linked.setter
    def number_format_is_linked(self, value: bool) -> None: ...
    @property
    def offset(self) -> int:
        """
        Read/write int value in range 0-1000 specifying the spacing between
        the tick mark labels and the axis as a percentange of the default
        value. 100 if no label offset setting is present.
        """
        ...

    @offset.setter
    def offset(self, value: int) -> None: ...

class ValueAxis(_BaseAxis):
    """An axis having continuous (as opposed to discrete) values.

    The vertical axis is generally a value axis, however both axes of an XY-type chart
    are value axes.
    """
    @property
    def crosses(self) -> XL_AXIS_CROSSES:
        """
        Member of :ref:`XlAxisCrosses` enumeration specifying the point on
        this axis where the other axis crosses, such as auto/zero, minimum,
        or maximum. Returns `XL_AXIS_CROSSES.CUSTOM` when a specific numeric
        crossing point (e.g. 1.5) is defined.
        """
        ...

    @crosses.setter
    def crosses(self, value: XL_AXIS_CROSSES) -> None: ...
    @property
    def crosses_at(self) -> float | None:
        """
        Numeric value on this axis at which the perpendicular axis crosses.
        Returns |None| if no crossing value is set.
        """
        ...

    @crosses_at.setter
    def crosses_at(self, value: float | None) -> None: ...
    @property
    def major_unit(self) -> float | None:
        """
        The float number of units between major tick marks on this value
        axis. |None| corresponds to the 'Auto' setting in the UI, and
        specifies the value should be calculated by PowerPoint based on the
        underlying chart data.
        """
        ...

    @major_unit.setter
    def major_unit(self, value: float | None) -> None: ...
    @property
    def minor_unit(self) -> float | None:
        """
        The float number of units between minor tick marks on this value
        axis. |None| corresponds to the 'Auto' setting in the UI, and
        specifies the value should be calculated by PowerPoint based on the
        underlying chart data.
        """
        ...

    @minor_unit.setter
    def minor_unit(self, value: float | None) -> None: ...
