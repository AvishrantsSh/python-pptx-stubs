from collections.abc import Sequence

from pptx.chart.axis import CategoryAxis, DateAxis, ValueAxis
from pptx.chart.legend import Legend
from pptx.chart.plot import _BasePlot
from pptx.chart.series import SeriesCollection, _BaseSeries
from pptx.dml.chtfmt import ChartFormat
from pptx.enum.chart import XL_CHART_TYPE
from pptx.oxml.chart.chart import CT_ChartSpace, CT_PlotArea
from pptx.oxml.chart.shared import CT_Title
from pptx.parts.chart import ChartPart
from pptx.shared import ElementProxy, PartElementProxy
from pptx.text.text import Font, TextFrame
from pptx.util import lazyproperty

class Chart[SeriesType: _BaseSeries, PlotType: _BasePlot](PartElementProxy):
    """A chart object."""
    def __init__(self, chartSpace: CT_ChartSpace, chart_part: ChartPart) -> None: ...
    @property
    def category_axis(self) -> CategoryAxis | DateAxis | ValueAxis:
        """
        The category axis of this chart. In the case of an XY or Bubble
        chart, this is the X axis. Raises |ValueError| if no category
        axis is defined (as is the case for a pie chart, for example).
        """
        ...

    @property
    def chart_style(self) -> int | None:
        """
        Read/write integer index of chart style used to format this chart.
        Range is from 1 to 48. Value is |None| if no explicit style has been
        assigned, in which case the default chart style is used. Assigning
        |None| causes any explicit setting to be removed. The integer index
        corresponds to the style's position in the chart style gallery in the
        PowerPoint UI.
        """
        ...

    @chart_style.setter
    def chart_style(self, value: int | None) -> None: ...
    @property
    def chart_title(self) -> ChartTitle:
        """A |ChartTitle| object providing access to title properties.

        Calling this property is destructive in the sense it adds a chart
        title element (`c:title`) to the chart XML if one is not already
        present. Use :attr:`has_title` to test for presence of a chart title
        non-destructively.
        """
        ...

    @property
    def chart_type(self) -> XL_CHART_TYPE:
        """Member of :ref:`XlChartType` enumeration specifying type of this chart.

        If the chart has two plots, for example, a line plot overlayed on a bar plot,
        the type reported is for the first (back-most) plot. Read-only.
        """
        ...

    @lazyproperty
    def font(self) -> Font:
        """Font object controlling text format defaults for this chart."""
        ...

    @property
    def has_legend(self) -> bool:
        """
        Read/write boolean, |True| if the chart has a legend. Assigning
        |True| causes a legend to be added to the chart if it doesn't already
        have one. Assigning False removes any existing legend definition
        along with any existing legend settings.
        """
        ...

    @has_legend.setter
    def has_legend(self, value: bool) -> None: ...
    @property
    def has_title(self) -> bool:
        """Read/write boolean, specifying whether this chart has a title.

        Assigning |True| causes a title to be added if not already present.
        Assigning |False| removes any existing title along with its text and
        settings.
        """
        ...

    @has_title.setter
    def has_title(self, value: bool) -> None: ...
    @property
    def legend(self) -> Legend | None:
        """
        A |Legend| object providing access to the properties of the legend
        for this chart.
        """
        ...

    @lazyproperty
    def plots(self) -> _Plots[PlotType]:
        """
        The sequence of plots in this chart. A plot, called a *chart group*
        in the Microsoft API, is a distinct sequence of one or more series
        depicted in a particular charting type. For example, a chart having
        a series plotted as a line overlaid on three series plotted as
        columns would have two plots; the first corresponding to the three
        column series and the second to the line series. Plots are sequenced
        in the order drawn, i.e. back-most to front-most. Supports *len()*,
        membership (e.g. ``p in plots``), iteration, slicing, and indexed
        access (e.g. ``plot = plots[i]``).
        """
        ...

    def replace_data(self, chart_data) -> None:
        """
        Use the categories and series values in the |ChartData| object
        *chart_data* to replace those in the XML and Excel worksheet for this
        chart.
        """
        ...

    @lazyproperty
    def series(self) -> SeriesCollection[SeriesType]:
        """
        A |SeriesCollection| object containing all the series in this
        chart. When the chart has multiple plots, all the series for the
        first plot appear before all those for the second, and so on. Series
        within a plot have an explicit ordering and appear in that sequence.
        """
        ...

    @property
    def value_axis(self) -> ValueAxis:
        """
        The |ValueAxis| object providing access to properties of the value
        axis of this chart. Raises |ValueError| if the chart has no value
        axis.
        """
        ...

class ChartTitle(ElementProxy):
    """Provides properties for manipulating a chart title."""
    def __init__(self, title: CT_Title) -> None: ...
    @lazyproperty
    def format(self) -> ChartFormat:
        """|ChartFormat| object providing access to line and fill formatting.

        Return the |ChartFormat| object providing shape formatting properties
        for this chart title, such as its line color and fill.
        """
        ...

    @property
    def has_text_frame(self) -> bool:
        """Read/write Boolean specifying whether this title has a text frame.

        Return |True| if this chart title has a text frame, and |False|
        otherwise. Assigning |True| causes a text frame to be added if not
        already present. Assigning |False| causes any existing text frame to
        be removed along with its text and formatting.
        """
        ...

    @has_text_frame.setter
    def has_text_frame(self, value: bool) -> None: ...
    @property
    def text_frame(self) -> TextFrame:
        """|TextFrame| instance for this chart title.

        Return a |TextFrame| instance allowing read/write access to the text
        of this chart title and its text formatting properties. Accessing this
        property is destructive in the sense it adds a text frame if one is
        not present. Use :attr:`has_text_frame` to test for the presence of
        a text frame non-destructively.
        """
        ...

class _Plots[PlotType: _BasePlot](Sequence[PlotType]):
    """
    The sequence of plots in a chart, such as a bar plot or a line plot. Most
    charts have only a single plot. The concept is necessary when two chart
    types are displayed in a single set of axes, like a bar plot with
    a superimposed line plot.
    """
    def __init__(self, plotArea: CT_PlotArea, chart: Chart) -> None: ...
    def __getitem__(self, index: slice | int) -> PlotType: ...
    def __len__(self) -> int: ...
