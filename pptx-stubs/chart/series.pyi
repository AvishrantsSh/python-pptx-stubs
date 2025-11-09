from collections.abc import Generator, Sequence
from typing import Any

from pptx.chart.datalabel import DataLabels
from pptx.chart.marker import Marker
from pptx.chart.point import BubblePoints, CategoryPoints, XyPoints
from pptx.dml.chtfmt import ChartFormat
from pptx.oxml.chart.chart import CT_PlotArea
from pptx.oxml.chart.plot import BaseChartElement
from pptx.oxml.chart.series import CT_SeriesComposite
from pptx.util import lazyproperty

class _BaseSeries:
    """
    Base class for |BarSeries| and other series classes.
    """
    def __init__(self, ser: CT_SeriesComposite) -> None: ...
    @lazyproperty
    def format(self) -> ChartFormat:
        """
        The |ChartFormat| instance for this series, providing access to shape
        properties such as fill and line.
        """
        ...

    @property
    def index(self) -> int:
        """
        The zero-based integer index of this series as reported in its
        `c:ser/c:idx` element.
        """
        ...

    @property
    def name(self) -> str:
        """
        The string label given to this series, appears as the title of the
        column for this series in the Excel worksheet. It also appears as the
        label for this series in the legend.
        """
        ...

class _BaseCategorySeries(_BaseSeries):
    """Base class for |BarSeries| and other category chart series classes."""
    @lazyproperty
    def data_labels(self) -> DataLabels:
        """|DataLabels| object controlling data labels for this series."""
        ...

    @lazyproperty
    def points(self) -> CategoryPoints:
        """
        The |CategoryPoints| object providing access to individual data
        points in this series.
        """
        ...

    @property
    def values(self) -> tuple[float, ...]:
        """
        Read-only. A sequence containing the float values for this series, in
        the order they appear on the chart.
        """
        ...

class _MarkerMixin:
    """
    Mixin class providing `.marker` property for line-type chart series. The
    line-type charts are Line, XY, and Radar.
    """
    @lazyproperty
    def marker(self) -> Marker:
        """
        The |Marker| instance for this series, providing access to data point
        marker properties such as fill and line. Setting these properties
        determines the appearance of markers for all points in this series
        that are not overridden by settings at the point level.
        """
        ...

class AreaSeries(_BaseCategorySeries):
    """
    A data point series belonging to an area plot.
    """

    ...

class BarSeries(_BaseCategorySeries):
    """A data point series belonging to a bar plot."""
    @property
    def invert_if_negative(self) -> bool:
        """
        |True| if a point having a value less than zero should appear with a
        fill different than those with a positive value. |False| if the fill
        should be the same regardless of the bar's value. When |True|, a bar
        with a solid fill appears with white fill; in a bar with gradient
        fill, the direction of the gradient is reversed, e.g. dark -> light
        instead of light -> dark. The term "invert" here should be understood
        to mean "invert the *direction* of the *fill gradient*".
        """
        ...

    @invert_if_negative.setter
    def invert_if_negative(self, value: bool) -> None: ...

class LineSeries(_BaseCategorySeries, _MarkerMixin):
    """
    A data point series belonging to a line plot.
    """
    @property
    def smooth(self) -> bool:
        """
        Read/write boolean specifying whether to use curve smoothing to
        form the line connecting the data points in this series into
        a continuous curve. If |False|, a series of straight line segments
        are used to connect the points.
        """
        ...

    @smooth.setter
    def smooth(self, value: bool) -> None: ...

class PieSeries(_BaseCategorySeries):
    """
    A data point series belonging to a pie plot.
    """

    ...

class RadarSeries(_BaseCategorySeries, _MarkerMixin):
    """
    A data point series belonging to a radar plot.
    """

    ...

class XySeries(_BaseSeries, _MarkerMixin):
    """
    A data point series belonging to an XY (scatter) plot.
    """
    def iter_values(self) -> Generator[float, Any, None]:
        """
        Generate each float Y value in this series, in the order they appear
        on the chart. A value of `None` represents a missing Y value
        (corresponding to a blank Excel cell).
        """
        ...

    @lazyproperty
    def points(self) -> XyPoints:
        """
        The |XyPoints| object providing access to individual data points in
        this series.
        """
        ...

    @property
    def values(self) -> tuple[float, ...]:
        """
        Read-only. A sequence containing the float values for this series, in
        the order they appear on the chart.
        """
        ...

class BubbleSeries(XySeries):
    """
    A data point series belonging to a bubble plot.
    """
    @lazyproperty
    def points(self) -> BubblePoints:
        """
        The |BubblePoints| object providing access to individual data point
        objects used to discover and adjust the formatting and data labels of
        a data point.
        """
        ...

class SeriesCollection[SeriesType: "_BaseSeries"](Sequence[SeriesType]):
    """
    A sequence of |Series| objects.
    """
    def __init__(self, parent_elm: CT_PlotArea | BaseChartElement) -> None: ...
    def __getitem__(self, index: int) -> SeriesType: ...
    def __len__(self) -> int: ...
