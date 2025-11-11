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
    def __init__(self, xChart: XChartType, chart: Chart[SeriesType, Self]) -> None: ...
    @lazyproperty
    def categories(self) -> Categories: ...
    @property
    def chart(self) -> Chart[SeriesType, Self]: ...
    @property
    def data_labels(self) -> DataLabels: ...
    @property
    def has_data_labels(self) -> bool: ...
    @has_data_labels.setter
    def has_data_labels(self, value: bool) -> None: ...
    @lazyproperty
    def series(self) -> SeriesCollection[SeriesType]: ...
    @property
    def vary_by_categories(self) -> bool: ...
    @vary_by_categories.setter
    def vary_by_categories(self, value: bool) -> None: ...

class AreaPlot(_BasePlot[CT_AreaChart, AreaSeries]): ...
class Area3DPlot(CT_Area3DChart, _BasePlot): ...

class BarPlot(_BasePlot[CT_BarChart, BarSeries]):
    @property
    def gap_width(self) -> int: ...
    @gap_width.setter
    def gap_width(self, value: int) -> None: ...
    @property
    def overlap(self) -> int: ...
    @overlap.setter
    def overlap(self, value: int) -> None: ...

class BubblePlot(_BasePlot[CT_BubbleChart, BubbleSeries]):
    @property
    def bubble_scale(self) -> int: ...
    @bubble_scale.setter
    def bubble_scale(self, value: int | None) -> None: ...

class DoughnutPlot(_BasePlot[CT_DoughnutChart, PieSeries]): ...
class LinePlot(_BasePlot[CT_LineChart, LineSeries]): ...
class PiePlot(_BasePlot[CT_PieChart, PieSeries]): ...
class RadarPlot(_BasePlot[CT_RadarChart, RadarSeries]): ...
class XyPlot(_BasePlot[CT_ScatterChart, XySeries]): ...

def PlotFactory(xChart: BaseChartElement, chart: Chart) -> _BasePlot: ...

class PlotTypeInspector:
    @classmethod
    def chart_type(cls, plot: _BasePlot) -> XL_CHART_TYPE: ...
