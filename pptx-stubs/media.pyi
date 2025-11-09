from typing import IO, Self

from pptx.util import lazyproperty

class Video:
    """Immutable value object representing a video such as MP4."""
    def __init__(self, blob: bytes, mime_type: str | None, filename: str | None) -> None: ...
    @classmethod
    def from_blob(cls, blob: bytes, mime_type: str | None, filename: str | None = ...) -> Self:
        """Return a new |Video| object loaded from image binary in *blob*."""
        ...

    @classmethod
    def from_path_or_file_like(cls, movie_file: str | IO[bytes], mime_type: str | None) -> Video:
        """Return a new |Video| object containing video in *movie_file*.

        *movie_file* can be either a path (string) or a file-like
        (e.g. StringIO) object.
        """
        ...

    @property
    def blob(self) -> bytes:
        """The bytestream of the media "file"."""
        ...

    @property
    def content_type(self) -> str | None:
        """MIME-type of this media, e.g. `'video/mp4'`."""
        ...

    @property
    def ext(self) -> str:
        """Return the file extension for this video, e.g. 'mp4'.

        The extension is that from the actual filename if known. Otherwise
        it is the lowercase canonical extension for the video's MIME type.
        'vid' is used if the MIME type is 'video/unknown'.
        """
        ...

    @property
    def filename(self) -> str:
        """Return a filename.ext string appropriate to this video.

        The base filename from the original path is used if this image was
        loaded from the filesystem. If no filename is available, such as when
        the video object is created from an in-memory stream, the string
        'movie.{ext}' is used where 'ext' is suitable to the video format,
        such as 'mp4'.
        """
        ...

    @lazyproperty
    def sha1(self) -> str:
        """The SHA1 hash digest for the binary "file" of this video.

        Example: `'1be010ea47803b00e140b852765cdf84f491da47'`
        """
        ...

SPEAKER_IMAGE_BYTES: bytes = ...
