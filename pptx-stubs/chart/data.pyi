import sys
from collections.abc import Generator, Iterable, Sequence
from typing import Any, Generic, TypeVar

if sys.version_info >= (3, 13):
    _ChartDataType = TypeVar("_SeriesDataType", bound="_BaseChartData", default=_BaseChartData)
    _SeriesDataType = TypeVar("_SeriesDataType", bound="_BaseSeriesData", default=_BaseSeriesData)
    _DataPointType = TypeVar("_DataPointType", bound="_BaseDataPoint", default=_BaseSeriesData)
else:
    _ChartDataType = TypeVar("_SeriesDataType", bound="_BaseChartData")
    _SeriesDataType = TypeVar("_SeriesDataType", bound="_BaseSeriesData")
    _DataPointType = TypeVar("_DataPointType", bound="_BaseDataPoint")

class _BaseChartData(Sequence[_SeriesDataType]):
    """Base class providing common members for chart data objects.

    A chart data object serves as a proxy for the chart data table that will be written to an
    Excel worksheet; operating as a sequence of series as well as providing access to chart-level
    attributes. A chart data object is used as a parameter in :meth:`shapes.add_chart` and
    :meth:`Chart.replace_data`. The data structure varies between major chart categories such as
    category charts and XY charts.
    """
    def __init__(self, number_format: str = ...) -> None: ...
    def __getitem__(self, index: int) -> _SeriesDataType: ...
    def __len__(self) -> int: ...
    def append(self, series: _SeriesDataType) -> None: ...
    def data_point_offset(self, series: _SeriesDataType) -> int:
        """
        The total integer number of data points appearing in the series of
        this chart that are prior to *series* in this sequence.
        """
        ...

    @property
    def number_format(self) -> str:
        """
        The formatting template string, e.g. '#,##0.0', that determines how
        X and Y values are formatted in this chart and in the Excel
        spreadsheet. A number format specified on a series will override this
        value for that series. Likewise, a distinct number format can be
        specified for a particular data point within a series.
        """
        ...

    def series_index(self, series) -> int:
        """
        Return the integer index of *series* in this sequence.
        """
        ...

    def series_name_ref(self, series) -> str:
        """
        Return the Excel worksheet reference to the cell containing the name
        for *series*.
        """
        ...

    def x_values_ref(self, series) -> str:
        """
        The Excel worksheet reference to the X values for *series* (not
        including the column label).
        """
        ...

    @property
    def xlsx_blob(self) -> bytes:
        """
        Return a blob containing an Excel workbook file populated with the
        contents of this chart data object.
        """
        ...

    def xml_bytes(self, chart_type) -> bytes:
        """
        Return a blob containing the XML for a chart of *chart_type*
        containing the series in this chart data object, as bytes suitable
        for writing directly to a file.
        """
        ...

    def y_values_ref(self, series) -> str:
        """
        The Excel worksheet reference to the Y values for *series* (not
        including the column label).
        """
        ...

class _BaseSeriesData(Sequence[_DataPointType], Generic[_ChartDataType, _DataPointType]):
    """
    Base class providing common members for series data objects. A series
    data object serves as proxy for a series data column in the Excel
    worksheet. It operates as a sequence of data points, as well as providing
    access to series-level attributes like the series label.
    """
    def __init__(self, chart_data: _ChartDataType, name: str | None, number_format: str | None) -> None: ...
    def __getitem__(self, index: int) -> _DataPointType: ...
    def __len__(self) -> int: ...
    def append(self, data_point: _DataPointType) -> None: ...
    @property
    def data_point_offset(self) -> int:
        """
        The integer count of data points that appear in all chart series
        prior to this one.
        """
        ...

    @property
    def index(self) -> int:
        """
        Zero-based integer indicating the sequence position of this series in
        its chart. For example, the second of three series would return `1`.
        """
        ...

    @property
    def name(self) -> str:
        """
        The name of this series, e.g. 'Series 1'. This name is used as the
        column heading for the y-values of this series and may also appear in
        the chart legend and perhaps other chart locations.
        """
        ...

    @property
    def name_ref(self) -> str:
        """
        The Excel worksheet reference to the cell containing the name for
        this series.
        """
        ...

    @property
    def number_format(self) -> str:
        """
        The formatting template string that determines how a number in this
        series is formatted, both in the chart and in the Excel spreadsheet;
        for example '#,##0.0'. If not specified for this series, it is
        inherited from the parent chart data object.
        """
        ...

    @property
    def x_values(self) -> list[Any]:
        """
        A sequence containing the X value of each datapoint in this series,
        in data point order.
        """
        ...

    @property
    def x_values_ref(self) -> str:
        """
        The Excel worksheet reference to the X values for this chart (not
        including the column heading).
        """
        ...

    @property
    def y_values(self) -> list[Any]:
        """
        A sequence containing the Y value of each datapoint in this series,
        in data point order.
        """
        ...

    @property
    def y_values_ref(self) -> str:
        """
        The Excel worksheet reference to the Y values for this chart (not
        including the column heading).
        """
        ...

class _BaseDataPoint:
    """
    Base class providing common members for data point objects.
    """
    def __init__(self, series_data: _BaseSeriesData, number_format: str | None) -> None: ...
    @property
    def number_format(self) -> str:
        """
        The formatting template string that determines how the value of this
        data point is formatted, both in the chart and in the Excel
        spreadsheet; for example '#,##0.0'. If not specified for this data
        point, it is inherited from the parent series data object.
        """
        ...

class CategoryChartData(_BaseChartData[CategorySeriesData]):
    """
    Accumulates data specifying the categories and series values for a chart
    and acts as a proxy for the chart data table that will be written to an
    Excel worksheet. Used as a parameter in :meth:`shapes.add_chart` and
    :meth:`Chart.replace_data`.

    This object is suitable for use with category charts, i.e. all those
    having a discrete set of label values (categories) as the range of their
    independent variable (X-axis) values. Unlike the ChartData types for
    charts supporting a continuous range of independent variable values (such
    as XyChartData), CategoryChartData has a single collection of category
    (X) values and each data point in its series specifies only the Y value.
    The corresponding X value is inferred by its position in the sequence.
    """
    def add_category(self, label: str | None) -> Category:
        """
        Return a newly created |data.Category| object having *label* and
        appended to the end of the category collection for this chart.
        *label* can be a string, a number, a datetime.date, or
        datetime.datetime object. All category labels in a chart must be the
        same type. All category labels in a chart having multi-level
        categories must be strings.
        """
        ...

    def add_series(
        self, name: str, values: Iterable[float] = ..., number_format: str | None = ...
    ) -> CategorySeriesData:
        """
        Add a series to this data set entitled *name* and having the data
        points specified by *values*, an iterable of numeric values.
        *number_format* specifies how the series values will be displayed,
        and may be a string, e.g. '#,##0' corresponding to an Excel number
        format.
        """
        ...

    @property
    def categories(self) -> Categories:
        """|data.Categories| object providing access to category-object hierarchy.

        Assigning an iterable of category labels (strings, numbers, or dates) replaces
        the |data.Categories| object with a new one containing a category for each label
        in the sequence.

        Creating a chart from chart data having date categories will cause the chart to
        have a |DateAxis| for its category axis.
        """
        ...

    @categories.setter
    def categories(self, category_labels: Iterable[str]) -> None: ...
    @property
    def categories_ref(self) -> str:
        """
        The Excel worksheet reference to the categories for this chart (not
        including the column heading).
        """
        ...

    def values_ref(self, series) -> str:
        """
        The Excel worksheet reference to the values for *series* (not
        including the column heading).
        """
        ...

class Categories(Sequence[Category]):
    """
    A sequence of |data.Category| objects, also having certain hierarchical
    graph behaviors for support of multi-level (nested) categories.
    """
    def __init__(self) -> None: ...
    def __getitem__(self, idx: int) -> Category: ...
    def __len__(self) -> int:
        """
        Return the count of the highest level of category in this sequence.
        If it contains hierarchical (multi-level) categories, this number
        will differ from :attr:`category_count`, which is the number of leaf
        nodes.
        """
        ...

    def add_category(self, label: str | None) -> Category:
        """
        Return a newly created |data.Category| object having *label* and
        appended to the end of this category sequence. *label* can be
        a string, a number, a datetime.date, or datetime.datetime object. All
        category labels in a chart must be the same type. All category labels
        in a chart having multi-level categories must be strings.

        Creating a chart from chart data having date categories will cause
        the chart to have a |DateAxis| for its category axis.
        """
        ...

    @property
    def are_dates(self) -> bool:
        """
        Return |True| if the first category in this collection has a date
        label (as opposed to str or numeric). A date label is one of type
        datetime.date or datetime.datetime. Returns |False| otherwise,
        including when this category collection is empty. It also returns
        False when this category collection is hierarchical, because
        hierarchical categories can only be written as string labels.
        """
        ...

    @property
    def are_numeric(self) -> bool:
        """
        Return |True| if the first category in this collection has a numeric
        label (as opposed to a string label), including if that value is
        a datetime.date or datetime.datetime object (as those are converted
        to integers for storage in Excel). Returns |False| otherwise,
        including when this category collection is empty. It also returns
        False when this category collection is hierarchical, because
        hierarchical categories can only be written as string labels.
        """
        ...

    @property
    def depth(self) -> int:
        """
        The number of hierarchy levels in this category graph. Returns 0 if
        it contains no categories.
        """
        ...

    def index(self, category) -> int:
        """
        The offset of *category* in the overall sequence of leaf categories.
        A non-leaf category gets the index of its first sub-category.
        """
        ...

    @property
    def leaf_count(self) -> int:
        """
        The number of leaf-level categories in this hierarchy. The return
        value is the same as that of `len()` only when the hierarchy is
        single level.
        """
        ...

    @property
    def levels(self) -> Generator[list[tuple[Any, Any]], Any, None]:
        """
        A generator of (idx, label) sequences representing the category
        hierarchy from the bottom up. The first level contains all leaf
        categories, and each subsequent is the next level up.
        """
        ...

    @property
    def number_format(self) -> str:
        """
        Read/write. Return a string representing the number format used in
        Excel to format these category values, e.g. '0.0' or 'mm/dd/yyyy'.
        This string is only relevant when the categories are numeric or date
        type, although it returns 'General' without error when the categories
        are string labels. Assigning |None| causes the default number format
        to be used, based on the type of the category labels.
        """
        ...

    @number_format.setter
    def number_format(self, value: str) -> None: ...

class Category:
    """
    A chart category, primarily having a label to be displayed on the
    category axis, but also able to be configured in a hierarchy for support
    of multi-level category charts.
    """
    def __init__(self, label: str | None, parent: Category) -> None: ...
    def add_sub_category(self, label: str | None) -> Category:
        """
        Return a newly created |data.Category| object having *label* and
        appended to the end of the sub-category sequence for this category.
        """
        ...

    @property
    def depth(self) -> int:
        """
        The number of hierarchy levels rooted at this category node. Returns
        1 if this category has no sub-categories.
        """
        ...

    @property
    def idx(self) -> int:
        """
        The offset of this category in the overall sequence of leaf
        categories. A non-leaf category gets the index of its first
        sub-category.
        """
        ...

    def index(self, sub_category: Category) -> int:
        """
        The offset of *sub_category* in the overall sequence of leaf
        categories.
        """
        ...

    @property
    def leaf_count(self) -> int:
        """
        The number of leaf category nodes under this category. Returns
        1 if this category has no sub-categories.
        """
        ...

    @property
    def label(self) -> int:
        """
        The value that appears on the axis for this category. The label can
        be a string, a number, or a datetime.date or datetime.datetime
        object.
        """
        ...

    def numeric_str_val(self, date_1904: bool = ...) -> str:
        """
        The string representation of the numeric (or date) label of this
        category, suitable for use in the XML `c:pt` element for this
        category. The optional *date_1904* parameter specifies the epoch used
        for calculating Excel date numbers.
        """
        ...

    @property
    def sub_categories(self) -> list[Category]:
        """
        The sequence of child categories for this category.
        """
        ...

class ChartData(CategoryChartData):
    """
    |ChartData| is simply an alias for |CategoryChartData| and may be removed
    in a future release. All new development should use |CategoryChartData|
    for creating or replacing the data in chart types other than XY and
    Bubble.
    """

    ...

class CategorySeriesData(_BaseSeriesData[CategoryChartData, CategoryDataPoint]):
    """
    The data specific to a particular category chart series. It provides
    access to the series label, the series data points, and an optional
    number format to be applied to each data point not having a specified
    number format.
    """
    def add_data_point(self, value, number_format: str | None = ...) -> CategoryDataPoint:
        """
        Return a CategoryDataPoint object newly created with value *value*,
        an optional *number_format*, and appended to this sequence.
        """
        ...

    @property
    def categories(self) -> Categories:
        """
        The |data.Categories| object that provides access to the category
        objects for this series.
        """
        ...

    @property
    def categories_ref(self) -> str:
        """
        The Excel worksheet reference to the categories for this chart (not
        including the column heading).
        """
        ...

    @property
    def values(self) -> list[Any]:
        """
        A sequence containing the (Y) value of each datapoint in this series,
        in data point order.
        """
        ...

    @property
    def values_ref(self) -> str:
        """
        The Excel worksheet reference to the (Y) values for this series (not
        including the column heading).
        """
        ...

class XyChartData(_BaseChartData[XySeriesData]):
    """
    A specialized ChartData object suitable for use with an XY (aka. scatter)
    chart. Unlike ChartData, it has no category sequence. Rather, each data
    point of each series specifies both an X and a Y value.
    """
    def add_series(self, name: str, number_format: str | None = ...) -> XySeriesData:
        """
        Return an |XySeriesData| object newly created and added at the end of
        this sequence, identified by *name* and values formatted with
        *number_format*.
        """
        ...

# BubbleChartData actually inherits from XyChartData in the original codebase
# A simplification is taken in the stubs package for BubbleSeriesData typehints.
class BubbleChartData(_BaseChartData[BubbleSeriesData]):
    """
    A specialized ChartData object suitable for use with a bubble chart.
    A bubble chart is essentially an XY chart where the markers are scaled to
    provide a third quantitative dimension to the exhibit.
    """
    def add_series(self, name: str, number_format: str | None = ...) -> BubbleSeriesData:
        """
        Return a |BubbleSeriesData| object newly created and added at the end
        of this sequence, and having series named *name* and values formatted
        with *number_format*.
        """
        ...

    def bubble_sizes_ref(self, series) -> str:
        """
        The Excel worksheet reference for the range containing the bubble
        sizes for *series*.
        """
        ...

class XySeriesData(_BaseSeriesData[XyChartData, XyDataPoint]):
    """
    The data specific to a particular XY chart series. It provides access to
    the series label, the series data points, and an optional number format
    to be applied to each data point not having a specified number format.

    The sequence of data points in an XY series is significant; lines are
    plotted following the sequence of points, even if that causes a line
    segment to "travel backward" (implying a multi-valued function). The data
    points are not automatically sorted into increasing order by X value.
    """
    def add_data_point(self, x, y, number_format=...) -> XyDataPoint:
        """
        Return an XyDataPoint object newly created with values *x* and *y*,
        and appended to this sequence.
        """
        ...

class BubbleSeriesData(XySeriesData[BubbleChartData, BubbleDataPoint]):
    """
    The data specific to a particular Bubble chart series. It provides access
    to the series label, the series data points, and an optional number
    format to be applied to each data point not having a specified number
    format.

    The sequence of data points in a bubble chart series is maintained
    throughout the chart building process because a data point has no unique
    identifier and can only be retrieved by index.
    """
    def add_data_point(self, x, y, size, number_format=...) -> BubbleDataPoint:
        """
        Append a new BubbleDataPoint object having the values *x*, *y*, and
        *size*. The optional *number_format* is used to format the Y value.
        If not provided, the number format is inherited from the series data.
        """
        ...

    @property
    def bubble_sizes(self) -> list[Any]:
        """
        A sequence containing the bubble size for each datapoint in this
        series, in data point order.
        """
        ...

    @property
    def bubble_sizes_ref(self) -> str:
        """
        The Excel worksheet reference for the range containing the bubble
        sizes for this series.
        """
        ...

class CategoryDataPoint(_BaseDataPoint):
    """
    A data point in a category chart series. Provides access to the value of
    the datapoint and the number format with which it should appear in the
    Excel file.
    """
    def __init__(self, series_data: CategorySeriesData, value, number_format: str | None) -> None: ...
    @property
    def value(self) -> Any:
        """
        The (Y) value for this category data point.
        """
        ...

class XyDataPoint(_BaseDataPoint):
    """
    A data point in an XY chart series. Provides access to the x and y values
    of the datapoint.
    """
    def __init__(self, series_data: XySeriesData, x, y, number_format: str | None) -> None: ...
    @property
    def x(self) -> Any:
        """
        The X value for this XY data point.
        """
        ...

    @property
    def y(self) -> Any:
        """
        The Y value for this XY data point.
        """
        ...

class BubbleDataPoint(XyDataPoint):
    """
    A data point in a bubble chart series. Provides access to the x, y, and
    size values of the datapoint.
    """
    def __init__(self, series_data: BubbleSeriesData, x, y, size, number_format: str | None) -> None: ...
    @property
    def bubble_size(self) -> Any:
        """
        The value representing the size of the bubble for this data point.
        """
        ...
