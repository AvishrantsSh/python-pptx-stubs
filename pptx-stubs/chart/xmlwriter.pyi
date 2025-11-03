from collections.abc import Iterable

from pptx.chart.data import _BaseChartData
from pptx.chart.series import _BaseSeries
from pptx.enum.chart import XL_CHART_TYPE
from pptx.oxml.chart.chart import CT_ChartSpace
from pptx.oxml.chart.series import CT_AxDataSource, CT_NumDataSource
from pptx.oxml.chart.shared import CT_Tx

def ChartXmlWriter(chart_type: XL_CHART_TYPE, chart_data: _BaseChartData):
    """
    Factory function returning appropriate XML writer object for
    *chart_type*, loaded with *chart_type* and *chart_data*.
    """
    ...

def SeriesXmlRewriterFactory(chart_type: XL_CHART_TYPE, chart_data: _BaseChartData):
    """
    Return a |_BaseSeriesXmlRewriter| subclass appropriate to *chart_type*.
    """
    ...

class _BaseChartXmlWriter:
    """
    Generates XML text (unicode) for a default chart, like the one added by
    PowerPoint when you click the *Add Column Chart* button on the ribbon.
    Differentiated XML for different chart types is provided by subclasses.
    """
    def __init__(self, chart_type: XL_CHART_TYPE, series_seq: Iterable[_BaseSeries]) -> None: ...
    @property
    def xml(self):
        """
        The full XML stream for the chart specified by this chart builder, as
        unicode text. This method must be overridden by each subclass.
        """
        ...

class _BaseSeriesXmlWriter:
    """
    Provides shared members for series XML writers.
    """
    def __init__(self, series: _BaseSeries, date_1904: bool = ...) -> None: ...
    @property
    def name(self) -> str:
        """
        The XML-escaped name for this series.
        """
        ...

    def numRef_xml(self, wksht_ref, number_format, values) -> str:
        """
        Return the ``<c:numRef>`` element specified by the parameters as
        unicode text.
        """
        ...

    def pt_xml(self, values) -> str:
        """
        Return the ``<c:ptCount>`` and sequence of ``<c:pt>`` elements
        corresponding to *values* as a single unicode text string.
        `c:ptCount` refers to the number of `c:pt` elements in this sequence.
        The `idx` attribute value for `c:pt` elements locates the data point
        in the overall data point sequence of the chart and is started at
        *offset*.
        """
        ...

    @property
    def tx(self) -> CT_Tx:
        """
        Return a ``<c:tx>`` oxml element for this series, containing the
        series name.
        """
        ...

    @property
    def tx_xml(self) -> str:
        """
        Return the ``<c:tx>`` (tx is short for 'text') element for this
        series as unicode text. This element contains the series name.
        """
        ...

class _BaseSeriesXmlRewriter:
    """
    Base class for series XML rewriters.
    """
    def __init__(self, chart_data: _BaseChartData) -> None: ...
    def replace_series_data(self, chartSpace: CT_ChartSpace) -> None:
        """
        Rewrite the series data under *chartSpace* using the chart data
        contents. All series-level formatting is left undisturbed. If
        the chart data contains fewer series than *chartSpace*, the extra
        series in *chartSpace* are deleted. If *chart_data* contains more
        series than the *chartSpace* element, new series are added to the
        last plot in the chart and series formatting is "cloned" from the
        last series in that plot.
        """
        ...

class _AreaChartXmlWriter(_BaseChartXmlWriter):
    """
    Provides specialized methods particular to the ``<c:areaChart>`` element.
    """
    @property
    def xml(self) -> str: ...

class _BarChartXmlWriter(_BaseChartXmlWriter):
    """
    Provides specialized methods particular to the ``<c:barChart>`` element.
    """
    @property
    def xml(self) -> str: ...

class _DoughnutChartXmlWriter(_BaseChartXmlWriter):
    """
    Provides specialized methods particular to the ``<c:doughnutChart>``
    element.
    """
    @property
    def xml(self) -> str: ...

class _LineChartXmlWriter(_BaseChartXmlWriter):
    """
    Provides specialized methods particular to the ``<c:lineChart>`` element.
    """
    @property
    def xml(self) -> str: ...

class _PieChartXmlWriter(_BaseChartXmlWriter):
    """
    Provides specialized methods particular to the ``<c:pieChart>`` element.
    """
    @property
    def xml(self) -> str: ...

class _RadarChartXmlWriter(_BaseChartXmlWriter):
    """
    Generates XML for the ``<c:radarChart>`` element.
    """
    @property
    def xml(self) -> str: ...

class _XyChartXmlWriter(_BaseChartXmlWriter):
    """
    Generates XML for the ``<c:scatterChart>`` element.
    """
    @property
    def xml(self) -> str: ...

class _BubbleChartXmlWriter(_XyChartXmlWriter):
    """
    Provides specialized methods particular to the ``<c:bubbleChart>``
    element.
    """
    @property
    def xml(self) -> str: ...

class _CategorySeriesXmlWriter(_BaseSeriesXmlWriter):
    """
    Generates XML snippets particular to a category chart series.
    """
    @property
    def cat(self) -> CT_AxDataSource:
        """
        Return the ``<c:cat>`` element XML for this series, as an oxml
        element.
        """
        ...

    @property
    def cat_xml(self) -> str:
        """
        The unicode XML snippet for the ``<c:cat>`` element for this series,
        containing the category labels and spreadsheet reference.
        """
        ...

    @property
    def val(self) -> CT_NumDataSource:
        """
        The ``<c:val>`` XML for this series, as an oxml element.
        """
        ...

    @property
    def val_xml(self) -> str:
        """
        Return the unicode XML snippet for the ``<c:val>`` element describing
        this series, containing the series values and their spreadsheet range
        reference.
        """
        ...

class _XySeriesXmlWriter(_BaseSeriesXmlWriter):
    """
    Generates XML snippets particular to an XY series.
    """
    @property
    def xVal(self) -> CT_NumDataSource:
        """
        Return the ``<c:xVal>`` element for this series as an oxml element.
        This element contains the X values for this series.
        """
        ...

    @property
    def xVal_xml(self) -> str:
        """
        Return the ``<c:xVal>`` element for this series as unicode text. This
        element contains the X values for this series.
        """
        ...

    @property
    def yVal(self) -> CT_NumDataSource:
        """
        Return the ``<c:yVal>`` element for this series as an oxml element.
        This element contains the Y values for this series.
        """
        ...

    @property
    def yVal_xml(self) -> str:
        """
        Return the ``<c:yVal>`` element for this series as unicode text. This
        element contains the Y values for this series.
        """
        ...

class _BubbleSeriesXmlWriter(_XySeriesXmlWriter):
    """
    Generates XML snippets particular to a bubble chart series.
    """
    @property
    def bubbleSize(self) -> CT_NumDataSource:
        """
        Return the ``<c:bubbleSize>`` element for this series as an oxml
        element. This element contains the bubble size values for this
        series.
        """
        ...

    @property
    def bubbleSize_xml(self) -> str:
        """
        Return the ``<c:bubbleSize>`` element for this series as unicode
        text. This element contains the bubble size values for all the
        data points in the chart.
        """
        ...

class _BubbleSeriesXmlRewriter(_BaseSeriesXmlRewriter):
    """
    A series rewriter suitable for bubble charts.
    """

    ...

class _CategorySeriesXmlRewriter(_BaseSeriesXmlRewriter):
    """
    A series rewriter suitable for category charts.
    """

    ...

class _XySeriesXmlRewriter(_BaseSeriesXmlRewriter):
    """
    A series rewriter suitable for XY (aka. scatter) charts.
    """

    ...
