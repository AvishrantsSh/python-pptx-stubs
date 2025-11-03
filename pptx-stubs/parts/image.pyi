from typing import IO

from pptx.opc.package import Part
from pptx.opc.packuri import PackURI
from pptx.package import Package
from pptx.util import lazyproperty

class ImagePart(Part):
    """An image part.

    An image part generally has a partname matching the regex `ppt/media/image[1-9][0-9]*.*`.
    """
    def __init__(
        self, partname: PackURI, content_type: str, package: Package, blob: bytes, filename: str | None = ...
    ) -> None: ...
    @classmethod
    def new(cls, package: Package, image: Image) -> ImagePart:
        """Return new |ImagePart| instance containing `image`.

        `image` is an |Image| object.
        """
        ...

    @property
    def desc(self) -> str:
        """The filename associated with this image.

        Either the filename of the original image or a generic name of the form `image.ext` where
        `ext` is appropriate to the image file format, e.g. `'jpg'`. An image created using a path
        will have that filename; one created with a file-like object will have a generic name.
        """
        ...

    @property
    def ext(self) -> str:
        """File-name extension for this image e.g. `'png'`."""
        ...

    @property
    def image(self) -> Image:
        """An |Image| object containing the image in this image part.

        Note this is a `pptx.image.Image` object, not a PIL Image.
        """
        ...

    def scale(self, scaled_cx: int | None, scaled_cy: int | None) -> tuple[int, int]:
        """Return scaled image dimensions in EMU based on the combination of parameters supplied.

        If `scaled_cx` and `scaled_cy` are both |None|, the native image size is returned. If
        neither `scaled_cx` nor `scaled_cy` is |None|, their values are returned unchanged. If a
        value is provided for either `scaled_cx` or `scaled_cy` and the other is |None|, the
        missing value is calculated such that the image's aspect ratio is preserved.
        """
        ...

    @lazyproperty
    def sha1(self) -> str:
        """The 40-character SHA1 hash digest for the image binary of this image part.

        like: `"1be010ea47803b00e140b852765cdf84f491da47"`.
        """
        ...

class Image:
    """Immutable value object representing an image such as a JPEG, PNG, or GIF."""
    def __init__(self, blob: bytes, filename: str | None) -> None: ...
    @classmethod
    def from_blob(cls, blob: bytes, filename: str | None = ...) -> Image:
        """Return a new |Image| object loaded from the image binary in `blob`."""
        ...

    @classmethod
    def from_file(cls, image_file: str | IO[bytes]) -> Image:
        """Return a new |Image| object loaded from `image_file`.

        `image_file` can be either a path (str) or a file-like object.
        """
        ...

    @property
    def blob(self) -> bytes:
        """The binary image bytestream of this image."""
        ...

    @lazyproperty
    def content_type(self) -> str:
        """MIME-type of this image, e.g. `"image/jpeg"`."""
        ...

    @lazyproperty
    def dpi(self) -> tuple[int, int]:
        """A (horz_dpi, vert_dpi) 2-tuple specifying the dots-per-inch resolution of this image.

        A default value of (72, 72) is used if the dpi is not specified in the image file.
        """
        ...

    @lazyproperty
    def ext(self) -> str:
        """Canonical file extension for this image e.g. `'png'`.

        The returned extension is all lowercase and is the canonical extension for the content type
        of this image, regardless of what extension may have been used in its filename, if any.
        """
        ...

    @property
    def filename(self) -> str | None:
        """Filename from path used to load this image, if loaded from the filesystem.

        |None| if no filename was used in loading, such as when loaded from an in-memory stream.
        """
        ...

    @lazyproperty
    def sha1(self) -> str:
        """SHA1 hash digest of the image blob."""
        ...

    @lazyproperty
    def size(self) -> tuple[int, int]:
        """A (width, height) 2-tuple specifying the dimensions of this image in pixels."""
        ...
