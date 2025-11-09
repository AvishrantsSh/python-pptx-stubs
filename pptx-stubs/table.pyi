from collections.abc import Iterator

from pptx.dml.fill import FillFormat
from pptx.enum.text import MSO_VERTICAL_ANCHOR
from pptx.oxml.table import CT_Table, CT_TableCell, CT_TableCol, CT_TableRow
from pptx.parts.slide import BaseSlidePart
from pptx.shapes import Subshape
from pptx.shapes.graphfrm import GraphicFrame
from pptx.text.text import TextFrame
from pptx.types import ProvidesPart
from pptx.util import Length, lazyproperty

class Table:
    """A DrawingML table object.

    Not intended to be constructed directly, use
    :meth:`.Slide.shapes.add_table` to add a table to a slide.
    """
    def __init__(self, tbl: CT_Table, graphic_frame: GraphicFrame) -> None: ...
    def cell(self, row_idx: int, col_idx: int) -> _Cell:
        """Return cell at `row_idx`, `col_idx`.

        Return value is an instance of |_Cell|. `row_idx` and `col_idx` are zero-based, e.g.
        cell(0, 0) is the top, left cell in the table.
        """
        ...

    @lazyproperty
    def columns(self) -> _ColumnCollection:
        """|_ColumnCollection| instance for this table.

        Provides access to |_Column| objects representing the table's columns. |_Column| objects
        are accessed using list notation, e.g. `col = tbl.columns[0]`.
        """
        ...

    @property
    def first_col(self) -> bool:
        """When `True`, indicates first column should have distinct formatting.

        Read/write. Distinct formatting is used, for example, when the first column contains row
        headings (is a side-heading column).
        """
        ...

    @first_col.setter
    def first_col(self, value: bool) -> None: ...
    @property
    def first_row(self) -> bool:
        """When `True`, indicates first row should have distinct formatting.

        Read/write. Distinct formatting is used, for example, when the first row contains column
        headings.
        """
        ...

    @first_row.setter
    def first_row(self, value: bool) -> None: ...
    @property
    def horz_banding(self) -> bool:
        """When `True`, indicates rows should have alternating shading.

        Read/write. Used to allow rows to be traversed more easily without losing track of which
        row is being read.
        """
        ...

    @horz_banding.setter
    def horz_banding(self, value: bool) -> None: ...
    def iter_cells(self) -> Iterator[_Cell]:
        """Generate _Cell object for each cell in this table.

        Each grid cell is generated in left-to-right, top-to-bottom order.
        """
        ...

    @property
    def last_col(self) -> bool:
        """When `True`, indicates the rightmost column should have distinct formatting.

        Read/write. Used, for example, when a row totals column appears at the far right of the
        table.
        """
        ...

    @last_col.setter
    def last_col(self, value: bool) -> None: ...
    @property
    def last_row(self) -> bool:
        """When `True`, indicates the bottom row should have distinct formatting.

        Read/write. Used, for example, when a totals row appears as the bottom row.
        """
        ...

    @last_row.setter
    def last_row(self, value: bool) -> None: ...
    def notify_height_changed(self) -> None:
        """Called by a row when its height changes.

        Triggers the graphic frame to recalculate its total height (as the sum of the row
        heights).
        """
        ...

    def notify_width_changed(self) -> None:
        """Called by a column when its width changes.

        Triggers the graphic frame to recalculate its total width (as the sum of the column
        widths).
        """
        ...

    @property
    def part(self) -> BaseSlidePart:
        """The package part containing this table."""
        ...

    @lazyproperty
    def rows(self) -> _RowCollection:
        """|_RowCollection| instance for this table.

        Provides access to |_Row| objects representing the table's rows. |_Row| objects are
        accessed using list notation, e.g. `col = tbl.rows[0]`.
        """
        ...

    @property
    def vert_banding(self) -> bool:
        """When `True`, indicates columns should have alternating shading.

        Read/write. Used to allow columns to be traversed more easily without losing track of
        which column is being read.
        """
        ...

    @vert_banding.setter
    def vert_banding(self, value: bool) -> None: ...

class _Cell(Subshape):
    """Table cell"""
    def __init__(self, tc: CT_TableCell, parent: ProvidesPart) -> None: ...
    def __eq__(self, other: object) -> bool:
        """|True| if this object proxies the same element as `other`.

        Equality for proxy objects is defined as referring to the same XML element, whether or not
        they are the same proxy object instance.
        """
        ...

    def __ne__(self, other: object) -> bool: ...
    @lazyproperty
    def fill(self) -> FillFormat:
        """|FillFormat| instance for this cell.

        Provides access to fill properties such as foreground color.
        """
        ...

    @property
    def is_merge_origin(self) -> bool:
        """True if this cell is the top-left grid cell in a merged cell."""
        ...

    @property
    def is_spanned(self) -> bool:
        """True if this cell is spanned by a merge-origin cell.

        A merge-origin cell "spans" the other grid cells in its merge range, consuming their area
        and "shadowing" the spanned grid cells.

        Note this value is |False| for a merge-origin cell. A merge-origin cell spans other grid
        cells, but is not itself a spanned cell.
        """
        ...

    @property
    def margin_left(self) -> Length:
        """Left margin of cells.

        Read/write. If assigned |None|, the default value is used, 0.1 inches for left and right
        margins and 0.05 inches for top and bottom.
        """
        ...

    @margin_left.setter
    def margin_left(self, margin_left: Length | None) -> None: ...
    @property
    def margin_right(self) -> Length:
        """Right margin of cell."""
        ...

    @margin_right.setter
    def margin_right(self, margin_right: Length | None) -> None: ...
    @property
    def margin_top(self) -> Length:
        """Top margin of cell."""
        ...

    @margin_top.setter
    def margin_top(self, margin_top: Length | None) -> None: ...
    @property
    def margin_bottom(self) -> Length:
        """Bottom margin of cell."""
        ...

    @margin_bottom.setter
    def margin_bottom(self, margin_bottom: Length | None) -> None: ...
    def merge(self, other_cell: _Cell) -> None:
        """Create merged cell from this cell to `other_cell`.

        This cell and `other_cell` specify opposite corners of the merged cell range. Either
        diagonal of the cell region may be specified in either order, e.g. self=bottom-right,
        other_cell=top-left, etc.

        Raises |ValueError| if the specified range already contains merged cells anywhere within
        its extents or if `other_cell` is not in the same table as `self`.
        """
        ...

    @property
    def span_height(self) -> int:
        """int count of rows spanned by this cell.

        The value of this property may be misleading (often 1) on cells where `.is_merge_origin`
        is not |True|, since only a merge-origin cell contains complete span information. This
        property is only intended for use on cells known to be a merge origin by testing
        `.is_merge_origin`.
        """
        ...

    @property
    def span_width(self) -> int:
        """int count of columns spanned by this cell.

        The value of this property may be misleading (often 1) on cells where `.is_merge_origin`
        is not |True|, since only a merge-origin cell contains complete span information. This
        property is only intended for use on cells known to be a merge origin by testing
        `.is_merge_origin`.
        """
        ...

    def split(self) -> None:
        """Remove merge from this (merge-origin) cell.

        The merged cell represented by this object will be "unmerged", yielding a separate
        unmerged cell for each grid cell previously spanned by this merge.

        Raises |ValueError| when this cell is not a merge-origin cell. Test with
        `.is_merge_origin` before calling.
        """
        ...

    @property
    def text(self) -> str:
        """Textual content of cell as a single string.

        The returned string will contain a newline character (`"\\n"`) separating each paragraph
        and a vertical-tab (`"\\v"`) character for each line break (soft carriage return) in the
        cell's text.

        Assignment to `text` replaces all text currently contained in the cell. A newline
        character (`"\\n"`) in the assigned text causes a new paragraph to be started. A
        vertical-tab (`"\\v"`) character in the assigned text causes a line-break (soft
        carriage-return) to be inserted. (The vertical-tab character appears in clipboard text
        copied from PowerPoint as its encoding of line-breaks.)
        """
        ...

    @text.setter
    def text(self, text: str) -> None: ...
    @property
    def text_frame(self) -> TextFrame:
        """|TextFrame| containing the text that appears in the cell."""
        ...

    @property
    def vertical_anchor(self) -> MSO_VERTICAL_ANCHOR | None:
        """Vertical alignment of this cell.

        This value is a member of the :ref:`MsoVerticalAnchor` enumeration or |None|. A value of
        |None| indicates the cell has no explicitly applied vertical anchor setting and its
        effective value is inherited from its style-hierarchy ancestors.

        Assigning |None| to this property causes any explicitly applied vertical anchor setting to
        be cleared and inheritance of its effective value to be restored.
        """
        ...

    @vertical_anchor.setter
    def vertical_anchor(self, mso_anchor_idx: MSO_VERTICAL_ANCHOR | None) -> None: ...

class _Column(Subshape):
    """Table column"""
    def __init__(self, gridCol: CT_TableCol, parent: _ColumnCollection) -> None: ...
    @property
    def width(self) -> Length:
        """Width of column in EMU."""
        ...

    @width.setter
    def width(self, width: Length) -> None: ...

class _Row(Subshape):
    """Table row"""
    def __init__(self, tr: CT_TableRow, parent: _RowCollection) -> None: ...
    @property
    def cells(self) -> _CellCollection:
        """Read-only reference to collection of cells in row.

        An individual cell is referenced using list notation, e.g. `cell = row.cells[0]`.
        """
        ...

    @property
    def height(self) -> Length:
        """Height of row in EMU."""
        ...

    @height.setter
    def height(self, height: Length) -> None: ...

class _CellCollection(Subshape):
    """Horizontal sequence of row cells"""
    def __init__(self, tr: CT_TableRow, parent: _Row) -> None: ...
    def __getitem__(self, idx: int) -> _Cell:
        """Provides indexed access, (e.g. 'cells[0]')."""
        ...

    def __iter__(self) -> Iterator[_Cell]:
        """Provides iterability."""
        ...

    def __len__(self) -> int:
        """Supports len() function (e.g. 'len(cells) == 1')."""
        ...

class _ColumnCollection(Subshape):
    """Sequence of table columns."""
    def __init__(self, tbl: CT_Table, parent: Table) -> None: ...
    def __getitem__(self, idx: int) -> _Column:
        """Provides indexed access, (e.g. 'columns[0]')."""
        ...

    def __len__(self) -> int:
        """Supports len() function (e.g. 'len(columns) == 1')."""
        ...

    def notify_width_changed(self) -> None:
        """Called by a column when its width changes. Pass along to parent."""
        ...

class _RowCollection(Subshape):
    """Sequence of table rows"""
    def __init__(self, tbl: CT_Table, parent: Table) -> None: ...
    def __getitem__(self, idx: int) -> _Row:
        """Provides indexed access, (e.g. 'rows[0]')."""
        ...

    def __len__(self) -> int:
        """Supports len() function (e.g. 'len(rows) == 1')."""
        ...

    def notify_height_changed(self) -> None:
        """Called by a row when its height changes. Pass along to parent."""
        ...
