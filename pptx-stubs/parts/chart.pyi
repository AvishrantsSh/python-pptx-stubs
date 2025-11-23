from typing import Self

from pptx.chart.chart import Chart
from pptx.chart.data import ChartData
from pptx.chart.plot import _BasePlot
from pptx.chart.series import _BaseSeries
from pptx.enum.chart import XL_CHART_TYPE
from pptx.opc.package import XmlPart
from pptx.oxml.chart.chart import CT_ChartSpace
from pptx.package import Package
from pptx.parts.embeddedpackage import EmbeddedXlsxPart
from pptx.util import lazyproperty

class ChartPart[SeriesType: _BaseSeries, PlotType: _BasePlot](XmlPart):
    partname_template: str = ...
    @classmethod
    def new(cls, chart_type: XL_CHART_TYPE, chart_data: ChartData, package: Package) -> Self: ...
    @lazyproperty
    def chart(self) -> Chart[SeriesType, PlotType]: ...
    @lazyproperty
    def chart_workbook(self) -> ChartWorkbook: ...

class ChartWorkbook[SeriesType: _BaseSeries, PlotType: _BasePlot]:
    def __init__(self, chartSpace: CT_ChartSpace, chart_part: ChartPart[SeriesType, PlotType]) -> None: ...
    def update_from_xlsx_blob(self, xlsx_blob: bytes) -> None: ...
    @property
    def xlsx_part(self) -> EmbeddedXlsxPart | None: ...
    @xlsx_part.setter
    def xlsx_part(self, xlsx_part: EmbeddedXlsxPart) -> None: ...
