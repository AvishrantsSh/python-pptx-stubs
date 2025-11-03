from pptx.enum.chart import XL_DATA_LABEL_POSITION
from pptx.oxml.chart.datalabel import CT_DLbls
from pptx.oxml.chart.series import CT_SeriesComposite
from pptx.text.text import Font, TextFrame
from pptx.util import lazyproperty

class DataLabels:
    """Provides access to properties of data labels for a plot or a series.

    This is not a collection and does not provide access to individual data
    labels. Access to individual labels is via the |Point| object. The
    properties this object provides control formatting of *all* the data
    labels in its scope.
    """
    def __init__(self, dLbls: CT_DLbls) -> None: ...
    @lazyproperty
    def font(self) -> Font:
        """
        The |Font| object that provides access to the text properties for
        these data labels, such as bold, italic, etc.
        """
        ...

    @property
    def number_format(self) -> str:
        """
        Read/write string specifying the format for the numbers on this set
        of data labels. Returns 'General' if no number format has been set.
        Note that this format string has no effect on rendered data labels
        when :meth:`number_format_is_linked` is |True|. Assigning a format
        string to this property automatically sets
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
    def position(self) -> XL_DATA_LABEL_POSITION | None:
        """
        Read/write :ref:`XlDataLabelPosition` enumeration value specifying
        the position of the data labels with respect to their data point, or
        |None| if no position is specified. Assigning |None| causes
        PowerPoint to choose the default position, which varies by chart
        type.
        """
        ...

    @position.setter
    def position(self, value: XL_DATA_LABEL_POSITION | None) -> None: ...
    @property
    def show_category_name(self) -> bool:
        """Read/write. True when name of category should appear in label."""
        ...

    @show_category_name.setter
    def show_category_name(self, value: bool) -> None: ...
    @property
    def show_legend_key(self) -> bool:
        """Read/write. True when data label displays legend-color swatch."""
        ...

    @show_legend_key.setter
    def show_legend_key(self, value: bool) -> None: ...
    @property
    def show_percentage(self) -> bool:
        """Read/write. True when data label displays percentage.

        This option is not operative on all chart types. Percentage appears
        on polar charts such as pie and donut.
        """
        ...

    @show_percentage.setter
    def show_percentage(self, value: bool) -> None: ...
    @property
    def show_series_name(self) -> bool:
        """Read/write. True when data label displays series name."""
        ...

    @show_series_name.setter
    def show_series_name(self, value: bool) -> None: ...
    @property
    def show_value(self) -> bool:
        """Read/write. True when label displays numeric value of datapoint."""
        ...

    @show_value.setter
    def show_value(self, value: bool) -> None: ...

class DataLabel:
    """
    The data label associated with an individual data point.
    """
    def __init__(self, ser: CT_SeriesComposite, idx: int) -> None: ...
    @lazyproperty
    def font(self) -> Font:
        """The |Font| object providing text formatting for this data label.

        This font object is used to customize the appearance of automatically
        inserted text, such as the data point value. The font applies to the
        entire data label. More granular control of the appearance of custom
        data label text is controlled by a font object on runs in the text
        frame.
        """
        ...

    @property
    def has_text_frame(self) -> bool:
        """
        Return |True| if this data label has a text frame (implying it has
        custom data label text), and |False| otherwise. Assigning |True|
        causes a text frame to be added if not already present. Assigning
        |False| causes any existing text frame to be removed along with any
        text contained in the text frame.
        """
        ...

    @has_text_frame.setter
    def has_text_frame(self, value: bool) -> None: ...
    @property
    def position(self) -> XL_DATA_LABEL_POSITION | None:
        """
        Read/write :ref:`XlDataLabelPosition` member specifying the position
        of this data label with respect to its data point, or |None| if no
        position is specified. Assigning |None| causes PowerPoint to choose
        the default position, which varies by chart type.
        """
        ...

    @position.setter
    def position(self, value: XL_DATA_LABEL_POSITION | None) -> None: ...
    @property
    def text_frame(self) -> TextFrame:
        """
        |TextFrame| instance for this data label, containing the text of the
        data label and providing access to its text formatting properties.
        """
        ...
