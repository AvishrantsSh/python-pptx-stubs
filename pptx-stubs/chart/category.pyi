from collections.abc import Generator, Iterable, Sequence
from typing import Any, Self

from pptx.oxml.chart.plot import BaseChartElement
from pptx.oxml.chart.series import CT_Lvl, CT_StrVal_NumVal_Composite

class Categories(Sequence):
    """
    A sequence of |category.Category| objects, each representing a category
    label on the chart. Provides properties for dealing with hierarchical
    categories.
    """
    def __init__(self, xChart: BaseChartElement) -> None: ...
    def __getitem__(self, idx) -> Category: ...
    def __iter__(self) -> Generator[Category, Any, None]: ...
    def __len__(self) -> int: ...
    @property
    def depth(self) -> int:
        """
        Return an integer representing the number of hierarchical levels in
        this category collection. Returns 1 for non-hierarchical categories
        and 0 if no categories are present (generally meaning no series are
        present).
        """
        ...

    @property
    def flattened_labels(self) -> Iterable[tuple[str, ...]]:
        """
        Return a sequence of tuples, each containing the flattened hierarchy
        of category labels for a leaf category. Each tuple is in parent ->
        child order, e.g. ``('US', 'CA', 'San Francisco')``, with the leaf
        category appearing last. If this categories collection is
        non-hierarchical, each tuple will contain only a leaf category label.
        If the plot has no series (and therefore no categories), an empty
        tuple is returned.
        """
        ...

    @property
    def levels(self) -> list[CategoryLevel]:
        """
        Return a sequence of |CategoryLevel| objects representing the
        hierarchy of this category collection. The sequence is empty when the
        category collection is not hierarchical, that is, contains only
        leaf-level categories. The levels are ordered from the leaf level to
        the root level; so the first level will contain the same categories
        as this category collection.
        """
        ...

class Category(str):
    """
    An extension of `str` that provides the category label as its string
    value, and additional attributes representing other aspects of the
    category.
    """
    def __new__(cls, pt: CT_StrVal_NumVal_Composite | None, *args) -> Self: ...
    def __init__(self, pt: CT_StrVal_NumVal_Composite | None, idx: int | None = ...) -> None:
        """
        *idx* is a required attribute of a c:pt element, but must be
        specified when pt is None, as when a "placeholder" category is
        created to represent a missing c:pt element.
        """
        ...

    @property
    def idx(self) -> int:
        """
        Return an integer representing the index reference of this category.
        For a leaf node, the index identifies the category. For a parent (or
        other ancestor) category, the index specifies the first leaf category
        that ancestor encloses.
        """
        ...

    @property
    def label(self) -> str:
        """
        Return the label of this category as a string.
        """
        ...

class CategoryLevel(Sequence):
    """
    A sequence of |category.Category| objects representing a single level in
    a hierarchical category collection. This object is only used when the
    categories are hierarchical, meaning they have more than one level and
    higher level categories group those at lower levels.
    """
    def __init__(self, lvl: CT_Lvl) -> None: ...
    def __getitem__(self, offset: int) -> Category: ...
    def __len__(self) -> int: ...
