from pptx.enum.chart import XL_LEGEND_POSITION
from pptx.text.text import Font
from pptx.util import lazyproperty

class Legend:
    """
    Represents the legend in a chart. A chart can have at most one legend.
    """
    def __init__(self, legend_elm) -> None: ...
    @lazyproperty
    def font(self) -> Font:
        """
        The |Font| object that provides access to the text properties for
        this legend, such as bold, italic, etc.
        """
        ...

    @property
    def horz_offset(self) -> float | None:
        """
        Adjustment of the x position of the legend from its default.
        Expressed as a float between -1.0 and 1.0 representing a fraction of
        the chart width. Negative values move the legend left, positive
        values move it to the right. |None| if no setting is specified.
        """
        ...

    @horz_offset.setter
    def horz_offset(self, value: float | None) -> None: ...
    @property
    def include_in_layout(self) -> bool:
        """|True| if legend should be located inside plot area.

        Read/write boolean specifying whether legend should be placed inside
        the plot area. In many cases this will cause it to be superimposed on
        the chart itself. Assigning |None| to this property causes any
        `c:overlay` element to be removed, which is interpreted the same as
        |True|. This use case should rarely be required and assigning
        a boolean value is recommended.
        """
        ...

    @include_in_layout.setter
    def include_in_layout(self, value: bool | None) -> None: ...
    @property
    def position(self) -> XL_LEGEND_POSITION:
        """
        Read/write :ref:`XlLegendPosition` enumeration value specifying the
        general region of the chart in which to place the legend.
        """
        ...

    @position.setter
    def position(self, position: XL_LEGEND_POSITION) -> None: ...
