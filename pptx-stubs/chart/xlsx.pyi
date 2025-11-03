from typing import str

from pptx.chart.data import BubbleChartData, CategoryChartData, XyChartData, _BaseChartData

class _BaseWorkbookWriter:
    """Base class for workbook writers, providing shared members."""
    def __init__(self, chart_data: _BaseChartData) -> None: ...
    @property
    def xlsx_blob(self) -> bytes:
        """bytes for Excel file containing chart_data."""
        ...

class CategoryWorkbookWriter(_BaseWorkbookWriter):
    """
    Determines Excel worksheet layout and can write an Excel workbook from
    a CategoryChartData object. Serves as the authority for Excel worksheet
    ranges.
    """
    # These stubs refine type annotations for certain inherited methods, including some that
    # are not explicitly defined in the subclass, to more accurately represent runtime behavior.
    def __init__(self, chart_data: CategoryChartData) -> None: ...
    @property
    def categories_ref(self) -> str:
        """
        The Excel worksheet reference to the categories for this chart (not
        including the column heading).
        """
        ...

    def series_name_ref(self, series) -> str:
        """
        Return the Excel worksheet reference to the cell containing the name
        for *series*. This also serves as the column heading for the series
        values.
        """
        ...

    def values_ref(self, series) -> str:
        """
        The Excel worksheet reference to the values for this series (not
        including the column heading).
        """
        ...

class XyWorkbookWriter(_BaseWorkbookWriter):
    """
    Determines Excel worksheet layout and can write an Excel workbook from XY
    chart data. Serves as the authority for Excel worksheet ranges.
    """
    # These stubs refine type annotations for certain inherited methods, including some that
    # are not explicitly defined in the subclass, to more accurately represent runtime behavior.
    def __init__(self, chart_data: XyChartData) -> None: ...
    def series_name_ref(self, series) -> str:
        """
        Return the Excel worksheet reference to the cell containing the name
        for *series*. This also serves as the column heading for the series
        Y values.
        """
        ...

    def series_table_row_offset(self, series) -> int:
        """
        Return the number of rows preceding the data table for *series* in
        the Excel worksheet.
        """
        ...

    def x_values_ref(self, series) -> str:
        """
        The Excel worksheet reference to the X values for this chart (not
        including the column label).
        """
        ...

    def y_values_ref(self, series) -> str:
        """
        The Excel worksheet reference to the Y values for this chart (not
        including the column label).
        """
        ...

class BubbleWorkbookWriter(XyWorkbookWriter):
    """
    Service object that knows how to write an Excel workbook from bubble
    chart data.
    """
    # These stubs refine type annotations for certain inherited methods, including some that
    # are not explicitly defined in the subclass, to more accurately represent runtime behavior.
    def __init__(self, chart_data: BubbleChartData) -> None: ...
    def bubble_sizes_ref(self, series) -> str:
        """
        The Excel worksheet reference to the range containing the bubble
        sizes for *series* (not including the column heading cell).
        """
        ...
