from collections.abc import Generator

from pptx.oxml.chart.axis import CT_CatAx, CT_DateAx, CT_ValAx
from pptx.oxml.chart.legend import CT_Legend
from pptx.oxml.chart.plot import BaseChartElement
from pptx.oxml.chart.series import CT_SeriesComposite
from pptx.oxml.chart.shared import CT_Boolean, CT_Boolean_Explicit, CT_Title
from pptx.oxml.text import CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Chart(BaseOxmlElement):
    @property
    def title(self) -> CT_Title | None:
        """``<c:title>`` child element or |None| if not present."""
        ...

    def get_or_add_title(self) -> CT_Title:
        """Return the ``<c:title>`` child element, newly added if not present."""
        ...

    @property
    def autoTitleDeleted(self) -> CT_Boolean_Explicit | None:
        """``<c:autoTitleDeleted>`` child element or |None| if not present."""
        ...

    def get_or_add_autoTitleDeleted(self) -> CT_Boolean_Explicit:
        """Return the ``<c:autoTitleDeleted>`` child element, newly added if not present."""
        ...

    @property
    def plotArea(self) -> CT_PlotArea:
        """Required ``<c:plotArea>`` child element."""
        ...

    @property
    def legend(self) -> CT_Legend | None:
        """``<c:legend>`` child element or |None| if not present."""
        ...

    def get_or_add_legend(self) -> CT_Legend:
        """Return the ``<c:legend>`` child element, newly added if not present."""
        ...

    @property
    def rId(self) -> str:
        """XsdString type-converted value of ``r:id`` attribute."""
        ...

    @rId.setter
    def rId(self, value: str) -> None: ...
    @property
    def has_legend(self) -> bool: ...
    @has_legend.setter
    def has_legend(self, bool_value: bool) -> None: ...
    @staticmethod
    def new_chart(rId: str) -> CT_Chart: ...

class CT_ChartSpace(BaseOxmlElement):
    """`c:chartSpace` root element of a chart part."""

    @property
    def date1904(self) -> CT_Boolean | None:
        """``<c:date1904>`` child element or |None| if not present."""
        ...

    def get_or_add_date1904(self) -> CT_Boolean:
        """Return the ``<c:date1904>`` child element, newly added if not present."""
        ...

    @property
    def style(self) -> CT_Style | None:
        """``<c:style>`` child element or |None| if not present."""
        ...

    def get_or_add_style(self) -> CT_Style:
        """Return the ``<c:style>`` child element, newly added if not present."""
        ...

    @property
    def chart(self) -> CT_Chart:
        """Required ``<c:chart>`` child element."""
        ...

    @property
    def txPr(self) -> CT_TextBody | None:
        """``<c:txPr>`` child element or |None| if not present."""
        ...

    def get_or_add_txPr(self) -> CT_TextBody:
        """Return the ``<c:txPr>`` child element, newly added if not present."""
        ...

    @property
    def externalData(self) -> CT_ExternalData | None:
        """``<c:externalData>`` child element or |None| if not present."""
        ...

    def get_or_add_externalData(self) -> CT_ExternalData:
        """Return the ``<c:externalData>`` child element, newly added if not present."""
        ...

    @property
    def catAx_lst(self) -> list[CT_CatAx]: ...
    @property
    def date_1904(self) -> bool: ...
    @property
    def dateAx_lst(self) -> list[CT_DateAx]: ...
    def get_or_add_title(self) -> CT_Title: ...
    @property
    def plotArea(self) -> CT_PlotArea: ...
    @property
    def valAx_lst(self) -> list[CT_ValAx]: ...
    @property
    def xlsx_part_rId(self) -> str | None: ...

class CT_ExternalData(BaseOxmlElement):
    @property
    def autoUpdate(self) -> CT_Boolean | None:
        """``<c:autoUpdate>`` child element or |None| if not present."""
        ...

    def get_or_add_autoUpdate(self) -> CT_Boolean:
        """Return the ``<c:autoUpdate>`` child element, newly added if not present."""
        ...

    @property
    def rId(self) -> str:
        """XsdString type-converted value of ``r:id`` attribute."""
        ...

    @rId.setter
    def rId(self, value: str) -> None: ...

class CT_PlotArea(BaseOxmlElement):
    @property
    def catAx_lst(self) -> list[CT_CatAx]:
        """A list containing each of the ``<c:catAx>`` child elements, in the order they appear."""
        ...

    @property
    def valAx_lst(self) -> list[CT_ValAx]:
        """A list containing each of the ``<c:valAx>`` child elements, in the order they appear."""
        ...

    def iter_sers(self) -> Generator[CT_SeriesComposite]: ...
    def iter_xCharts(self) -> Generator[BaseChartElement]: ...
    @property
    def last_ser(self) -> CT_SeriesComposite | None: ...
    @property
    def next_idx(self) -> int: ...
    @property
    def next_order(self) -> int: ...
    @property
    def sers(self) -> tuple[CT_SeriesComposite, ...]: ...
    @property
    def xCharts(self) -> tuple[BaseChartElement, ...]: ...

class CT_Style(BaseOxmlElement):
    @property
    def val(self) -> int:
        """ST_Style type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...
