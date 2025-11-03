from os import PathLike
from typing import IO, Any, Self

class FontFiles:
    """A class-based singleton serving as a lazy cache for system font details."""

    _font_files = ...
    @classmethod
    def find(cls, family_name: str, is_bold: bool, is_italic: bool) -> str:
        """Return the absolute path to an installed OpenType font.

        File is matched by `family_name` and the styles `is_bold` and `is_italic`.
        """
        ...

class _Font:
    """
    A wrapper around an OTF/TTF font file stream that knows how to parse it
    for its name and style characteristics, e.g. bold and italic.
    """
    def __init__(self, stream: _Stream) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exception_type, exception_value, exception_tb) -> None: ...
    @property
    def is_bold(self) -> bool:
        """
        |True| if this font is marked as a bold style of its font family.
        """
        ...

    @property
    def is_italic(self) -> bool:
        """
        |True| if this font is marked as an italic style of its font family.
        """
        ...

    @classmethod
    def open(cls, font_file_path: PathLike | str) -> Self:
        """
        Return a |_Font| instance loaded from *font_file_path*.
        """
        ...

    @property
    def family_name(self) -> str:
        """
        The name of the typeface family for this font, e.g. 'Arial'. The full
        typeface name includes optional style names, such as 'Regular' or
        'Bold Italic'. This attribute is only the common base name shared by
        all fonts in the family.
        """
        ...

class _Stream:
    """A thin wrapper around a binary file that facilitates reading C-struct values."""
    def __init__(self, file: IO[bytes]) -> None: ...
    @classmethod
    def open(cls, path: PathLike | str) -> Self:
        """Return |_Stream| providing binary access to contents of file at `path`."""
        ...

    def close(self) -> None:
        """
        Close the wrapped file. Using the stream after closing raises an
        exception.
        """
        ...

    def read(self, offset: int, length: int):
        """
        Return *length* bytes from this stream starting at *offset*.
        """
        ...

    def read_fields(self, template: str, offset: int = ...) -> tuple[Any, ...]:
        """
        Return a tuple containing the C-struct fields in this stream
        specified by *template* and starting at *offset*.
        """
        ...

class _BaseTable:
    """
    Base class for OpenType font file table objects.
    """
    def __init__(self, tag, stream, offset, length) -> None: ...

class _HeadTable(_BaseTable):
    """
    OpenType font table having the tag 'head' and containing certain header
    information for the font, including its bold and/or italic style.
    """
    def __init__(self, tag, stream: _Stream, offset: int, length: int) -> None: ...
    @property
    def is_bold(self) -> bool:
        """
        |True| if this font is marked as having emboldened characters.
        """
        ...

    @property
    def is_italic(self) -> bool:
        """
        |True| if this font is marked as having italicized characters.
        """
        ...

class _NameTable(_BaseTable):
    """
    An OpenType font table having the tag 'name' and containing the
    name-related strings for the font.
    """
    def __init__(self, tag, stream, offset, length) -> None: ...
    @property
    def family_name(self) -> str | None:
        """
        The name of the typeface family for this font, e.g. 'Arial'.
        """
        ...
