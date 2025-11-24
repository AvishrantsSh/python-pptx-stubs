from collections.abc import Callable, Generator, Iterable, Iterator
from typing import IO, Literal, overload

from pptx.chart.data import BubbleChartData, CategoryChartData, XyChartData, _BaseChartData
from pptx.chart.plot import (
    AreaPlot,
    BarPlot,
    BubblePlot,
    DoughnutPlot,
    LinePlot,
    PiePlot,
    RadarPlot,
    XyPlot,
    _BasePlot,
)
from pptx.chart.series import (
    AreaSeries,
    BarSeries,
    BubbleSeries,
    LineSeries,
    PieSeries,
    RadarSeries,
    XySeries,
    _BaseCategorySeries,
    _BaseSeries,
)
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_SHAPE, PP_PLACEHOLDER, PROG_ID
from pptx.oxml.chart.plot import BaseChartElement
from pptx.oxml.shapes import ShapeElement
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectFrame
from pptx.oxml.shapes.groupshape import CT_GroupShape
from pptx.oxml.shapes.picture import CT_Picture
from pptx.parts.slide import SlidePart
from pptx.shapes.autoshape import Shape
from pptx.shapes.base import BaseShape
from pptx.shapes.freeform import FreeformBuilder
from pptx.shapes.graphfrm import GraphicFrame
from pptx.shapes.group import GroupShape
from pptx.shapes.picture import Picture
from pptx.shapes.placeholder import LayoutPlaceholder, MasterPlaceholder, NotesSlidePlaceholder
from pptx.shared import ParentedElementProxy
from pptx.slide import Slide, SlideLayout
from pptx.types import ProvidesPart
from pptx.util import Length

class _BaseShapes(ParentedElementProxy):
    _element: CT_GroupShape
    _spTree: CT_GroupShape
    _cached_max_shape_id: int | None
    def __init__(self, spTree: CT_GroupShape, parent: ProvidesPart) -> None: ...
    def __getitem__(self, idx: int) -> BaseShape: ...
    def __iter__(self) -> Iterator[BaseShape]: ...
    def __len__(self) -> int: ...
    def clone_placeholder(self, placeholder: LayoutPlaceholder) -> None: ...
    def ph_basename(self, ph_type: PP_PLACEHOLDER) -> str: ...
    @property
    def element(self) -> CT_GroupShape: ...
    @property
    def turbo_add_enabled(self) -> bool: ...
    @turbo_add_enabled.setter
    def turbo_add_enabled(self, value: bool) -> None: ...

class _BaseGroupShapes(_BaseShapes):
    _element: CT_GroupShape
    _part: SlidePart
    @overload
    def add_chart(
        self,
        chart_type: Literal[XL_CHART_TYPE.AREA, XL_CHART_TYPE.AREA_STACKED, XL_CHART_TYPE.AREA_STACKED_100],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[AreaSeries, AreaPlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[XL_CHART_TYPE.BAR_CLUSTERED, XL_CHART_TYPE.BAR_STACKED, XL_CHART_TYPE.BAR_STACKED_100],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[BarSeries, BarPlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[XL_CHART_TYPE.BUBBLE, XL_CHART_TYPE.BUBBLE_THREE_D_EFFECT],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: BubbleChartData | XyChartData,
    ) -> GraphicFrame[BubbleSeries, BubblePlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[
            XL_CHART_TYPE.COLUMN_CLUSTERED, XL_CHART_TYPE.COLUMN_STACKED, XL_CHART_TYPE.COLUMN_STACKED_100
        ],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[BarSeries, BarPlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[XL_CHART_TYPE.DOUGHNUT, XL_CHART_TYPE.DOUGHNUT_EXPLODED],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[PieSeries, DoughnutPlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[
            XL_CHART_TYPE.LINE,
            XL_CHART_TYPE.LINE_MARKERS,
            XL_CHART_TYPE.LINE_MARKERS_STACKED,
            XL_CHART_TYPE.LINE_MARKERS_STACKED_100,
            XL_CHART_TYPE.LINE_STACKED,
            XL_CHART_TYPE.LINE_STACKED_100,
        ],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[LineSeries, LinePlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[XL_CHART_TYPE.PIE, XL_CHART_TYPE.PIE_EXPLODED],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[PieSeries, PiePlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[XL_CHART_TYPE.RADAR, XL_CHART_TYPE.RADAR_FILLED, XL_CHART_TYPE.RADAR_MARKERS],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[RadarSeries, RadarPlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: Literal[
            XL_CHART_TYPE.XY_SCATTER,
            XL_CHART_TYPE.XY_SCATTER_LINES,
            XL_CHART_TYPE.XY_SCATTER_LINES_NO_MARKERS,
            XL_CHART_TYPE.XY_SCATTER_SMOOTH,
            XL_CHART_TYPE.XY_SCATTER_SMOOTH_NO_MARKERS,
        ],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: XyChartData,
    ) -> GraphicFrame[XySeries, XyPlot]: ...
    @overload
    def add_chart(
        self,
        chart_type: XL_CHART_TYPE,
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: CategoryChartData,
    ) -> GraphicFrame[_BaseCategorySeries, _BasePlot[BaseChartElement, _BaseCategorySeries]]: ...
    @overload
    def add_chart(
        self,
        chart_type: XL_CHART_TYPE,
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: _BaseChartData,
    ) -> GraphicFrame[_BaseSeries, _BasePlot[BaseChartElement, _BaseSeries]]: ...
    def add_chart(
        self,
        chart_type: XL_CHART_TYPE,
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        chart_data: _BaseChartData,
    ) -> GraphicFrame:
        # The base package provides inaccurate return type annotation for this method.
        # The types have been corrected here for accurate static analysis.
        ...

    def add_group_shape(self, shapes: Iterable[BaseShape] = ...) -> GroupShape: ...
    def add_ole_object(
        self,
        object_file: str | IO[bytes],
        prog_id: str,
        left: Length,
        top: Length,
        width: Length | None = ...,
        height: Length | None = ...,
        icon_file: str | IO[bytes] | None = ...,
        icon_width: Length | None = ...,
        icon_height: Length | None = ...,
    ) -> GraphicFrame: ...
    def add_picture(
        self,
        image_file: str | IO[bytes],
        left: Length,
        top: Length,
        width: Length | None = ...,
        height: Length | None = ...,
    ) -> Picture: ...
    def add_shape(
        self, autoshape_type_id: MSO_SHAPE, left: Length, top: Length, width: Length, height: Length
    ) -> Shape: ...
    def add_textbox(self, left: Length, top: Length, width: Length, height: Length) -> Shape: ...
    def build_freeform(
        self, start_x: float = ..., start_y: float = ..., scale: tuple[float, float] | float = ...
    ) -> FreeformBuilder: ...
    def index(self, shape: BaseShape) -> int: ...
    @property
    def element(self) -> CT_GroupShape: ...
    @property
    def part(self) -> SlidePart: ...
    def __init__(self, grpSp: CT_GroupShape, parent: ProvidesPart) -> None: ...

class GroupShapes(_BaseGroupShapes): ...

class SlideShapes(_BaseGroupShapes):
    _parent: Slide
    def add_movie(
        self,
        movie_file: str | IO[bytes],
        left: Length,
        top: Length,
        width: Length,
        height: Length,
        poster_frame_image: str | IO[bytes] | None = ...,
        mime_type: str = ...,
    ) -> GraphicFrame: ...
    def add_table(
        self, rows: int, cols: int, left: Length, top: Length, width: Length, height: Length
    ) -> GraphicFrame: ...
    def clone_layout_placeholders(self, slide_layout: SlideLayout) -> None: ...
    @property
    def parent(self) -> Slide: ...
    @property
    def placeholders(self) -> SlidePlaceholders: ...
    @property
    def title(self) -> Shape | None: ...

class LayoutShapes(_BaseShapes): ...
class MasterShapes(_BaseShapes): ...

class NotesSlideShapes(_BaseShapes):
    def ph_basename(self, ph_type: PP_PLACEHOLDER) -> str: ...

class BasePlaceholders(_BaseShapes): ...

class LayoutPlaceholders(BasePlaceholders):
    __iter__: Callable[[], Iterator[LayoutPlaceholder]]

    def get(self, idx: int, default: LayoutPlaceholder | None = ...) -> LayoutPlaceholder | None: ...

class MasterPlaceholders(BasePlaceholders):
    __iter__: Callable[[], Iterator[MasterPlaceholder]]
    def get(self, ph_type: PP_PLACEHOLDER, default: MasterPlaceholder | None = ...) -> MasterPlaceholder | None: ...

class NotesSlidePlaceholders(MasterPlaceholders):
    __iter__: Callable[[], Iterator[NotesSlidePlaceholder]]
    ...

class SlidePlaceholders(ParentedElementProxy):
    _element: CT_GroupShape
    def __getitem__(self, idx: int) -> BaseShape: ...
    def __iter__(self) -> Generator[BaseShape]: ...
    def __len__(self) -> int: ...
    @property
    def element(self) -> CT_GroupShape: ...

def BaseShapeFactory(shape_elm: ShapeElement, parent: ProvidesPart) -> BaseShape: ...
def SlideShapeFactory(shape_elm: ShapeElement, parent: ProvidesPart) -> BaseShape: ...

class _MoviePicElementCreator:
    def __init__(
        self,
        shapes: SlideShapes,
        shape_id: int,
        movie_file: str | IO[bytes],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        poster_frame_file: str | IO[bytes] | None,
        mime_type: str | None,
    ) -> None: ...
    @classmethod
    def new_movie_pic(
        cls,
        shapes: SlideShapes,
        shape_id: int,
        movie_file: str | IO[bytes],
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
        poster_frame_image: str | IO[bytes] | None,
        mime_type: str | None,
    ) -> CT_Picture: ...

class _OleObjectElementCreator:
    def __init__(
        self,
        shapes: _BaseGroupShapes,
        shape_id: int,
        ole_object_file: str | IO[bytes],
        prog_id: PROG_ID | str,
        x: Length,
        y: Length,
        cx: Length | None,
        cy: Length | None,
        icon_file: str | IO[bytes] | None,
        icon_width: Length | None,
        icon_height: Length | None,
    ) -> None: ...
    @classmethod
    def graphicFrame(
        cls,
        shapes: _BaseGroupShapes,
        shape_id: int,
        ole_object_file: str | IO[bytes],
        prog_id: PROG_ID | str,
        x: Length,
        y: Length,
        cx: Length | None,
        cy: Length | None,
        icon_file: str | IO[bytes] | None,
        icon_width: Length | None,
        icon_height: Length | None,
    ) -> CT_GraphicalObjectFrame: ...
