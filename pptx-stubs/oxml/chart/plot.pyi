from collections.abc import Generator

from pptx.oxml.chart.datalabel import CT_DLbls
from pptx.oxml.chart.series import CT_AxDataSource, CT_SeriesComposite, CT_StrVal_NumVal_Composite
from pptx.oxml.chart.shared import CT_Boolean
from pptx.oxml.simpletypes import ST_Grouping
from pptx.oxml.xmlchemy import BaseOxmlElement

class BaseChartElement(BaseOxmlElement):
    @property
    def cat(self) -> CT_AxDataSource | None: ...
    @property
    def cat_pt_count(self) -> int: ...
    @property
    def cat_pts(self) -> list[CT_StrVal_NumVal_Composite | None]: ...
    @property
    def grouping_val(self) -> ST_Grouping: ...
    def iter_sers(self) -> Generator[CT_SeriesComposite]: ...
    @property
    def sers(self) -> tuple[CT_SeriesComposite, ...]: ...

class CT_Area3DChart(BaseChartElement):
    @property
    def grouping(self) -> CT_Grouping | None:
        """``<c:grouping>`` child element or |None| if not present."""
        ...

    def get_or_add_grouping(self) -> CT_Grouping:
        """Return the ``<c:grouping>`` child element, newly added if not present."""
        ...

class CT_AreaChart(BaseChartElement):
    @property
    def grouping(self) -> CT_Grouping | None:
        """``<c:grouping>`` child element or |None| if not present."""
        ...

    def get_or_add_grouping(self) -> CT_Grouping:
        """Return the ``<c:grouping>`` child element, newly added if not present."""
        ...

    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

class CT_BarChart(BaseChartElement):
    @property
    def barDir(self) -> CT_BarDir:
        """Required ``<c:barDir>`` child element."""
        ...

    @property
    def grouping(self) -> CT_Grouping | None:
        """``<c:grouping>`` child element or |None| if not present."""
        ...

    def get_or_add_grouping(self) -> CT_Grouping:
        """Return the ``<c:grouping>`` child element, newly added if not present."""
        ...

    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

    @property
    def gapWidth(self) -> CT_GapAmount | None:
        """``<c:gapWidth>`` child element or |None| if not present."""
        ...

    def get_or_add_gapWidth(self) -> CT_GapAmount:
        """Return the ``<c:gapWidth>`` child element, newly added if not present."""
        ...

    @property
    def overlap(self) -> CT_Overlap | None:
        """``<c:overlap>`` child element or |None| if not present."""
        ...

    def get_or_add_overlap(self) -> CT_Overlap:
        """Return the ``<c:overlap>`` child element, newly added if not present."""
        ...

    @property
    def grouping_val(self) -> ST_Grouping: ...

class CT_BarDir(BaseOxmlElement):
    @property
    def val(self) -> str:
        """ST_BarDir type-converted value of ``val`` attribute, or |ST_BarDir.COL| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: str) -> None: ...

class CT_BubbleChart(BaseChartElement):
    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

    @property
    def bubble3D(self) -> CT_Boolean | None:
        """``<c:bubble3D>`` child element or |None| if not present."""
        ...

    def get_or_add_bubble3D(self) -> CT_Boolean:
        """Return the ``<c:bubble3D>`` child element, newly added if not present."""
        ...

    @property
    def bubbleScale(self) -> CT_BubbleScale | None:
        """``<c:bubbleScale>`` child element or |None| if not present."""
        ...

    def get_or_add_bubbleScale(self) -> CT_BubbleScale:
        """Return the ``<c:bubbleScale>`` child element, newly added if not present."""
        ...

class CT_BubbleScale(BaseChartElement):
    @property
    def val(self) -> int:
        """ST_BubbleScale type-converted value of ``val`` attribute, or |100| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...

class CT_DoughnutChart(BaseChartElement):
    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

class CT_GapAmount(BaseOxmlElement):
    @property
    def val(self) -> int:
        """ST_GapAmount type-converted value of ``val`` attribute, or |150| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...

class CT_Grouping(BaseOxmlElement):
    @property
    def val(self) -> str | None:
        """ST_Grouping type-converted value of ``val`` attribute, or |None|]. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: str | None) -> None: ...

class CT_LineChart(BaseChartElement):
    @property
    def grouping(self) -> CT_Grouping | None:
        """``<c:grouping>`` child element or |None| if not present."""
        ...

    def get_or_add_grouping(self) -> CT_Grouping:
        """Return the ``<c:grouping>`` child element, newly added if not present."""
        ...

    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

class CT_Overlap(BaseOxmlElement):
    @property
    def val(self) -> int:
        """ST_Overlap type-converted value of ``val`` attribute, or |0| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...

class CT_PieChart(BaseChartElement):
    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

class CT_RadarChart(BaseChartElement):
    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...

    @property
    def dLbls(self) -> CT_DLbls | None:
        """``<c:dLbls>`` child element or |None| if not present."""
        ...

    def get_or_add_dLbls(self) -> CT_DLbls:
        """Return the ``<c:dLbls>`` child element, newly added if not present."""
        ...

class CT_ScatterChart(BaseChartElement):
    @property
    def varyColors(self) -> CT_Boolean | None:
        """``<c:varyColors>`` child element or |None| if not present."""
        ...

    def get_or_add_varyColors(self) -> CT_Boolean:
        """Return the ``<c:varyColors>`` child element, newly added if not present."""
        ...

    @property
    def ser_lst(self) -> list[CT_SeriesComposite]:
        """A list containing each of the ``<c:ser>`` child elements, in the order they appear."""
        ...
