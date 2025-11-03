from collections.abc import Sequence

from pptx.chart.datalabel import DataLabel
from pptx.chart.marker import Marker
from pptx.dml.chtfmt import ChartFormat
from pptx.oxml.chart.series import CT_SeriesComposite
from pptx.util import lazyproperty

class _BasePoints(Sequence[Point]):
    """
    Sequence providing access to the individual data points in a series.
    """
    def __init__(self, ser: CT_SeriesComposite) -> None: ...
    def __getitem__(self, idx: int) -> Point: ...

class BubblePoints(_BasePoints):
    """
    Sequence providing access to the individual data points in
    a |BubbleSeries| object.
    """
    def __len__(self) -> int: ...

class CategoryPoints(_BasePoints):
    """
    Sequence providing access to individual |Point| objects, each
    representing the visual properties of a data point in the specified
    category series.
    """
    def __len__(self) -> int: ...

class Point:
    """
    Provides access to the properties of an individual data point in
    a series, such as the visual properties of its marker and the text and
    font of its data label.
    """
    def __init__(self, ser: CT_SeriesComposite, idx: int) -> None: ...
    @lazyproperty
    def data_label(self) -> DataLabel:
        """
        The |DataLabel| object representing the label on this data point.
        """
        ...

    @lazyproperty
    def format(self) -> ChartFormat:
        """
        The |ChartFormat| object providing access to the shape formatting
        properties of this data point, such as line and fill.
        """
        ...

    @lazyproperty
    def marker(self) -> Marker:
        """
        The |Marker| instance for this point, providing access to the visual
        properties of the data point marker, such as fill and line. Setting
        these properties overrides any value set at the series level.
        """
        ...

class XyPoints(_BasePoints):
    """
    Sequence providing access to the individual data points in an |XySeries|
    object.
    """
    def __len__(self) -> int: ...
