from typing import Self

from pptx.opc.package import Part
from pptx.util import lazyproperty

class MediaPart(Part):
    """A media part, containing an audio or video resource.

    A media part generally has a partname matching the regex
    `ppt/media/media[1-9][0-9]*.*`.
    """
    @classmethod
    def new(cls, package, media) -> Self:
        """Return new |MediaPart| instance containing `media`.

        `media` must be a |Media| object.
        """
        ...

    @lazyproperty
    def sha1(self) -> str:
        """The SHA1 hash digest for the media binary of this media part.

        Example: `'1be010ea47803b00e140b852765cdf84f491da47'`
        """
        ...
