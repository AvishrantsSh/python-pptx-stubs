from collections.abc import Generator, Iterator
from typing import IO, Any

from pptx.opc.package import OpcPackage
from pptx.opc.packuri import PackURI
from pptx.parts.coreprops import CorePropertiesPart
from pptx.parts.image import ImagePart
from pptx.parts.media import MediaPart
from pptx.parts.presentation import PresentationPart
from pptx.util import lazyproperty

class Package(OpcPackage):
    """An overall .pptx package."""
    @lazyproperty
    def core_properties(self) -> CorePropertiesPart:
        """Instance of |CoreProperties| holding read/write Dublin Core doc properties.

        Creates a default core properties part if one is not present (not common).
        """
        ...

    def get_or_add_image_part(self, image_file: str | IO[bytes]) -> ImagePart:
        """
        Return an |ImagePart| object containing the image in *image_file*. If
        the image part already exists in this package, it is reused,
        otherwise a new one is created.
        """
        ...

    def get_or_add_media_part(self, media) -> MediaPart:
        """Return a |MediaPart| object containing the media in *media*.

        If a media part for this media bytestream ("file") is already present
        in this package, it is reused, otherwise a new one is created.
        """
        ...

    def next_image_partname(self, ext: str) -> PackURI:
        """Return a |PackURI| instance representing the next available image partname.

        Partname uses the next available sequence number. *ext* is used as the extention on the
        returned partname.
        """
        ...

    def next_media_partname(self, ext) -> PackURI:
        """Return |PackURI| instance for next available media partname.

        Partname is first available, starting at sequence number 1. Empty
        sequence numbers are reused. *ext* is used as the extension on the
        returned partname.
        """
        ...

    @property
    def presentation_part(self) -> PresentationPart:
        """
        Reference to the |Presentation| instance contained in this package.
        """
        ...

class _ImageParts:
    """Provides access to the image parts in a package."""
    def __init__(self, package: Package) -> None: ...
    def __iter__(self) -> Iterator[ImagePart]:
        """Generate a reference to each |ImagePart| object in the package."""
        ...

    def get_or_add_image_part(self, image_file: str | IO[bytes]) -> ImagePart:
        """Return |ImagePart| object containing the image in `image_file`.

        `image_file` can be either a path to an image file or a file-like object
        containing an image. If an image part containing this same image already exists,
        that instance is returned, otherwise a new image part is created.
        """
        ...

class _MediaParts:
    """Provides access to the media parts in a package.

    Supports iteration and :meth:`get()` using the media object SHA1 hash as
    its key.
    """
    def __init__(self, package: Package) -> None: ...
    def __iter__(self) -> Generator[MediaPart, Any, None]:
        """Generate a reference to each |MediaPart| object in the package."""
        ...

    def get_or_add_media_part(self, media) -> MediaPart:
        """Return a |MediaPart| object containing the media in *media*.

        If this package already contains a media part for the same
        bytestream, that instance is returned, otherwise a new media part is
        created.
        """
        ...
