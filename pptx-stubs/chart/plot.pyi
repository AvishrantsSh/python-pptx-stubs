from typing import Self

from pptx.chart.category import Categories
from pptx.chart.chart import Chart
from pptx.chart.datalabel import DataLabels
from pptx.chart.series import (
    AreaSeries,
    BarSeries,
    BubbleSeries,
    LineSeries,
    PieSeries,
    RadarSeries,
    SeriesCollection,
    XySeries,
    _BaseSeries,
)
from pptx.enum.chart import XL_CHART_TYPE
from pptx.oxml.chart.plot import (
    BaseChartElement,
    CT_Area3DChart,
    CT_AreaChart,
    CT_BarChart,
    CT_BubbleChart,
    CT_DoughnutChart,
    CT_LineChart,
    CT_PieChart,
    CT_RadarChart,
    CT_ScatterChart,
)
from pptx.util import lazyproperty

class _BasePlot[XChartType: BaseChartElement, SeriesType: _BaseSeries]:
    """
    A distinct plot that appears in the plot area of a chart. A chart may
    have more than one plot, in which case they appear as superimposed
    layers, such as a line plot appearing on top of a bar chart.
    """
    def __init__(self, xChart: XChartType, chart: Chart[SeriesType, Self]) -> None: ...
    @lazyproperty
    def categories(self) -> Categories:
        """
        Returns a |category.Categories| sequence object containing
        a |category.Category| object for each of the category labels
        associated with this plot. The |category.Category| class derives from
        ``str``, so the returned value can be treated as a simple sequence of
        strings for the common case where all you need is the labels in the
        order they appear on the chart. |category.Categories| provides
        additional properties for dealing with hierarchical categories when
        required.
        """
        ...

    @property
    def chart(self) -> Chart[SeriesType, Self]:
        """
        The |Chart| object containing this plot.
        """
        ...

    @property
    def data_labels(self) -> DataLabels:
        """
        |DataLabels| instance providing properties and methods on the
        collection of data labels associated with this plot.
        """
        ...

    @property
    def has_data_labels(self) -> bool:
        """
        Read/write boolean, |True| if the series has data labels. Assigning
        |True| causes data labels to be added to the plot. Assigning False
        removes any existing data labels.
        """
        ...

    @has_data_labels.setter
    def has_data_labels(self, value: bool) -> None:
        """
        Add, remove, or leave alone the ``<c:dLbls>`` child element depending
        on current state and assigned *value*. If *value* is |True| and no
        ``<c:dLbls>`` element is present, a new default element is added with
        default child elements and settings. When |False|, any existing dLbls
        element is removed.
        """
        ...

    @lazyproperty
    def series(self) -> SeriesCollection[SeriesType]:
        """
        A sequence of |Series| objects representing the series in this plot,
        in the order they appear in the plot.
        """
        ...

    @property
    def vary_by_categories(self) -> bool:
        """
        Read/write boolean value specifying whether to use a different color
        for each of the points in this plot. Only effective when there is
        a single series; PowerPoint automatically varies color by series when
        more than one series is present.
        """
        ...

    @vary_by_categories.setter
    def vary_by_categories(self, value: bool) -> None: ...

class AreaPlot(_BasePlot[CT_AreaChart, AreaSeries]):
    """
    An area plot.
    """

    ...

class Area3DPlot(CT_Area3DChart, _BasePlot):
    """
    A 3-dimensional area plot.
    """

    ...

class BarPlot(_BasePlot[CT_BarChart, BarSeries]):
    """
    A bar chart-style plot.
    """
    @property
    def gap_width(self) -> int:
        """
        Width of gap between bar(s) of each category, as an integer
        percentage of the bar width. The default value for a new bar chart is
        150, representing 150% or 1.5 times the width of a single bar.
        """
        ...

    @gap_width.setter
    def gap_width(self, value: int) -> None: ...
    @property
    def overlap(self) -> int:
        """
        Read/write int value in range -100..100 specifying a percentage of
        the bar width by which to overlap adjacent bars in a multi-series bar
        chart. Default is 0. A setting of -100 creates a gap of a full bar
        width and a setting of 100 causes all the bars in a category to be
        superimposed. A stacked bar plot has overlap of 100 by default.
        """
        ...

    @overlap.setter
    def overlap(self, value: int) -> None:
        """
        Set the value of the ``<c:overlap>`` child element to *int_value*,
        or remove the overlap element if *int_value* is 0.
        """
        ...

class BubblePlot(_BasePlot[CT_BubbleChart, BubbleSeries]):
    """
    A bubble chart plot.
    """
    @property
    def bubble_scale(self) -> int:
        """
        An integer between 0 and 300 inclusive indicating the percentage of
        the default size at which bubbles should be displayed. Assigning
        |None| produces the same behavior as assigning `100`.
        """
        ...

    @bubble_scale.setter
    def bubble_scale(self, value: int | None) -> None: ...

class DoughnutPlot(_BasePlot[CT_DoughnutChart, PieSeries]):
    """
    An doughnut plot.
    """

    ...

class LinePlot(_BasePlot[CT_LineChart, LineSeries]):
    """
    A line chart-style plot.
    """

    ...

class PiePlot(_BasePlot[CT_PieChart, PieSeries]):
    """
    A pie chart-style plot.
    """

    ...

class RadarPlot(_BasePlot[CT_RadarChart, RadarSeries]):
    """
    A radar-style plot.
    """

    ...

class XyPlot(_BasePlot[CT_ScatterChart, XySeries]):
    """
    An XY (scatter) plot.
    """

    ...

def PlotFactory(xChart: BaseChartElement, chart: Chart) -> _BasePlot:
    """
    Return an instance of the appropriate subclass of _BasePlot based on the
    tagname of *xChart*.
    """
    ...

class PlotTypeInspector:
    """
    "One-shot" service object that knows how to identify the type of a plot
    as a member of the XL_CHART_TYPE enumeration.
    """
    @classmethod
    def chart_type(cls, plot: _BasePlot) -> XL_CHART_TYPE:
        """
        Return the member of :ref:`XlChartType` that corresponds to the chart
        type of *plot*.
        """
        ...
