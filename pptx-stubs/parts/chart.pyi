from typing import Generic, Self

from pptx.chart.chart import Chart
from pptx.chart.data import ChartData
from pptx.chart.plot import _PlotType
from pptx.chart.series import _SeriesType
from pptx.enum.chart import XL_CHART_TYPE
from pptx.opc.package import XmlPart
from pptx.oxml.chart.chart import CT_ChartSpace
from pptx.package import Package
from pptx.parts.embeddedpackage import EmbeddedXlsxPart
from pptx.util import lazyproperty

class ChartPart(XmlPart, Generic[_SeriesType, _PlotType]):
    """A chart part.

    Corresponds to parts having partnames matching ppt/charts/chart[1-9][0-9]*.xml
    """

    partname_template: str = ...
    @classmethod
    def new(cls, chart_type: XL_CHART_TYPE, chart_data: ChartData, package: Package) -> Self:
        """Return new |ChartPart| instance added to `package`.

        Returned chart-part contains a chart of `chart_type` depicting `chart_data`.
        """
        ...

    @lazyproperty
    def chart(self) -> Chart[_SeriesType, _PlotType]:
        """|Chart| object representing the chart in this part."""
        ...

    @lazyproperty
    def chart_workbook(self) -> ChartWorkbook:
        """
        The |ChartWorkbook| object providing access to the external chart
        data in a linked or embedded Excel workbook.
        """
        ...

class ChartWorkbook(Generic[_SeriesType, _PlotType]):
    """Provides access to external chart data in a linked or embedded Excel workbook."""
    def __init__(self, chartSpace: CT_ChartSpace, chart_part: ChartPart[_SeriesType, _PlotType]) -> None: ...
    def update_from_xlsx_blob(self, xlsx_blob: bytes) -> None:
        """
        Replace the Excel spreadsheet in the related |EmbeddedXlsxPart| with
        the Excel binary in *xlsx_blob*, adding a new |EmbeddedXlsxPart| if
        there isn't one.
        """
        ...

    @property
    def xlsx_part(self) -> EmbeddedXlsxPart | None:
        """Optional |EmbeddedXlsxPart| object containing data for this chart.

        This related part has its rId at `c:chartSpace/c:externalData/@rId`. This value
        is |None| if there is no `<c:externalData>` element.
        """
        ...

    @xlsx_part.setter
    def xlsx_part(self, xlsx_part: EmbeddedXlsxPart) -> None:
        """
        Set the related |EmbeddedXlsxPart| to *xlsx_part*. Assume one does
        not already exist.
        """
        ...
