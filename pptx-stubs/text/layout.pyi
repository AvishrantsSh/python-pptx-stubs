from collections.abc import Callable, Generator, Iterable
from os import PathLike
from typing import Any, Self

from PIL import ImageFont
from pptx.util import Length

class TextFitter(tuple):
    """Value object that knows how to fit text into given rectangular extents."""
    def __new__(cls, line_source: _LineSource, extents: tuple[Length, Length], font_file: str) -> Self: ...
    @classmethod
    def best_fit_font_size(cls, text: str, extents: tuple[Length, Length], max_size: int, font_file: str) -> int:
        """Return whole-number best fit point size less than or equal to `max_size`.

        The return value is the largest whole-number point size less than or equal to
        `max_size` that allows `text` to fit completely within `extents` when rendered
        using font defined in `font_file`.
        """
        ...

class _BinarySearchTree:
    """
    A node in a binary search tree. Uniform for root, subtree root, and leaf
    nodes.
    """

    _lesser: Self
    _greater: Self

    def __init__(self, value) -> None: ...
    def find_max(self, predicate: Callable[[Any], bool], max_: Any = ...) -> Any | None:
        """
        Return the largest item in or under this node that satisfies
        *predicate*.
        """
        ...

    @classmethod
    def from_ordered_sequence(cls, iseq: Iterable[Any]) -> Self:
        """
        Return the root of a balanced binary search tree populated with the
        values in iterable *iseq*.
        """
        ...

    def insert(self, value: Any) -> None:
        """
        Insert a new node containing *value* into this tree such that its
        structure as a binary search tree is preserved.
        """
        ...

    def tree(self, level: int = ..., prefix: str = ...) -> str:
        """
        A string representation of the tree rooted in this node, useful for
        debugging purposes.
        """
        ...

    @property
    def value(self) -> Any:
        """
        The value object contained in this node.
        """
        ...

class _LineSource:
    """
    Generates all the possible even-word line breaks in a string of text,
    each in the form of a (line, remainder) 2-tuple where *line* contains the
    text before the break and *remainder* the text after as a |_LineSource|
    object. Its boolean value is |True| when it contains text, |False| when
    its text is the empty string or whitespace only.
    """
    def __init__(self, text) -> None: ...
    def __bool__(self):
        """
        Gives this object boolean behaviors (in Python 3). bool(line_source)
        is False if it contains the empty string or whitespace only.
        """
        ...

    def __eq__(self, other) -> bool: ...
    def __iter__(self) -> Generator[_Line, Any, None]:
        """
        Generate a (text, remainder) pair for each possible even-word line
        break in this line source, where *text* is a str value and remainder
        is a |_LineSource| value.
        """
        ...

    def __nonzero__(self):
        """
        Gives this object boolean behaviors (in Python 2). bool(line_source)
        is False if it contains the empty string or whitespace only.
        """
        ...

    def __repr__(self) -> str: ...

class _Line(tuple):
    """
    A candidate line broken at an even word boundary from a string of text,
    and a |_LineSource| value containing the text that remains after the line
    is broken at this spot.
    """
    def __new__(cls, text: str, remainder) -> Self: ...
    def __gt__(self, other: Self) -> bool: ...
    def __lt__(self, other: Self) -> bool: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    @property
    def remainder(self): ...
    @property
    def text(self): ...

class _Fonts:
    """
    A memoizing cache for ImageFont objects.
    """

    fonts: dict[tuple[PathLike | str, float], ImageFont.FreeTypeFont] = ...
    @classmethod
    def font(cls, font_path: PathLike | str, point_size: float): ...
