from pptx.chart.chart import Chart
from pptx.chart.plot import _BasePlot
from pptx.chart.series import _BaseSeries
from pptx.dml.effect import ShadowFormat
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectData, CT_GraphicalObjectFrame
from pptx.parts.chart import ChartPart
from pptx.parts.slide import BaseSlidePart
from pptx.shapes.base import BaseShape
from pptx.shared import ParentedElementProxy
from pptx.table import Table
from pptx.types import ProvidesPart
from pptx.util import lazyproperty

class GraphicFrame[SeriesType: _BaseSeries, PlotType: _BasePlot](BaseShape):
    _element: CT_GraphicalObjectFrame
    _graphicFrame: CT_GraphicalObjectFrame
    def __init__(self, graphicFrame: CT_GraphicalObjectFrame, parent: ProvidesPart) -> None: ...
    @property
    def chart(self) -> Chart[SeriesType, PlotType]: ...
    @property
    def chart_part(self) -> ChartPart[SeriesType, PlotType]: ...
    @property
    def has_chart(self) -> bool: ...
    @property
    def has_table(self) -> bool: ...
    @property
    def ole_format(self) -> _OleFormat: ...
    @lazyproperty
    def shadow(self) -> ShadowFormat: ...
    @property
    def shape_type(self) -> MSO_SHAPE_TYPE: ...
    @property
    def table(self) -> Table: ...

class _OleFormat(ParentedElementProxy):
    part: BaseSlidePart
    def __init__(self, graphicData: CT_GraphicalObjectData, parent: ProvidesPart) -> None: ...
    @property
    def blob(self) -> bytes | None: ...
    @property
    def prog_id(self) -> str | None: ...
    @property
    def show_as_icon(self) -> bool | None: ...
