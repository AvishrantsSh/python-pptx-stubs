from typing import IO, Self

from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import PROG_ID
from pptx.media import Video
from pptx.opc.package import XmlPart
from pptx.oxml.slide import CT_Slide
from pptx.parts.image import Image, ImagePart
from pptx.slide import NotesMaster, NotesSlide, Slide, SlideLayout, SlideMaster
from pptx.util import lazyproperty

class BaseSlidePart(XmlPart):
    """Base class for slide parts.

    This includes slide, slide-layout, and slide-master parts, but also notes-slide,
    notes-master, and handout-master parts.
    """

    _element: CT_Slide
    def get_image(self, rId: str) -> Image:
        """Return an |Image| object containing the image related to this slide by *rId*.

        Raises |KeyError| if no image is related by that id, which would generally indicate a
        corrupted .pptx file.
        """
        ...

    def get_or_add_image_part(self, image_file: str | IO[bytes]) -> tuple[ImagePart, str]:
        """Return `(image_part, rId)` pair corresponding to `image_file`.

        The returned |ImagePart| object contains the image in `image_file` and is
        related to this slide with the key `rId`. If either the image part or
        relationship already exists, they are reused, otherwise they are newly created.
        """
        ...

    @property
    def name(self) -> str:
        """Internal name of this slide."""
        ...

class NotesMasterPart(BaseSlidePart):
    """Notes master part.

    Corresponds to package file `ppt/notesMasters/notesMaster1.xml`.
    """
    @classmethod
    def create_default(cls, package) -> NotesMasterPart:
        """
        Create and return a default notes master part, including creating the
        new theme it requires.
        """
        ...

    @lazyproperty
    def notes_master(self) -> NotesMaster:
        """
        Return the |NotesMaster| object that proxies this notes master part.
        """
        ...

class NotesSlidePart(BaseSlidePart):
    """Notes slide part.

    Contains the slide notes content and the layout for the slide handout page.
    Corresponds to package file `ppt/notesSlides/notesSlide[1-9][0-9]*.xml`.
    """
    @classmethod
    def new(cls, package, slide_part) -> NotesSlidePart:
        """Return new |NotesSlidePart| for the slide in `slide_part`.

        The new notes-slide part is based on the (singleton) notes master and related to
        both the notes-master part and `slide_part`. If no notes-master is present,
        one is created based on the default template.
        """
        ...

    @lazyproperty
    def notes_master(self):
        """Return the |NotesMaster| object this notes slide inherits from."""
        ...

    @lazyproperty
    def notes_slide(self) -> NotesSlide:
        """Return the |NotesSlide| object that proxies this notes slide part."""
        ...

class SlidePart(BaseSlidePart):
    """Slide part. Corresponds to package files ppt/slides/slide[1-9][0-9]*.xml."""
    @classmethod
    def new(cls, partname, package, slide_layout_part) -> Self:
        """Return newly-created blank slide part.

        The new slide-part has `partname` and a relationship to `slide_layout_part`.
        """
        ...

    def add_chart_part(self, chart_type: XL_CHART_TYPE, chart_data: ChartData) -> str:
        """Return str rId of new |ChartPart| object containing chart of `chart_type`.

        The chart depicts `chart_data` and is related to the slide contained in this
        part by `rId`.
        """
        ...

    def add_embedded_ole_object_part(self, prog_id: PROG_ID | str, ole_object_file: str | IO[bytes]) -> str:
        """Return rId of newly-added OLE-object part formed from `ole_object_file`."""
        ...

    def get_or_add_video_media_part(self, video: Video) -> tuple[str, str]:
        """Return rIds for media and video relationships to media part.

        A new |MediaPart| object is created if it does not already exist
        (such as would occur if the same video appeared more than once in
         a presentation). Two relationships to the media part are created,
        one each with MEDIA and VIDEO relationship types. The need for two
        appears to be for legacy support for an earlier (pre-Office 2010)
        PowerPoint media embedding strategy.
        """
        ...

    @property
    def has_notes_slide(self) -> bool:
        """
        Return True if this slide has a notes slide, False otherwise. A notes
        slide is created by the :attr:`notes_slide` property when one doesn't
        exist; use this property to test for a notes slide without the
        possible side-effect of creating one.
        """
        ...

    @lazyproperty
    def notes_slide(self) -> NotesSlide:
        """The |NotesSlide| instance associated with this slide.

        If the slide does not have a notes slide, a new one is created. The same single instance
        is returned on each call.
        """
        ...

    @lazyproperty
    def slide(self) -> Slide:
        """
        The |Slide| object representing this slide part.
        """
        ...

    @property
    def slide_id(self) -> int:
        """Return the slide identifier stored in the presentation part for this slide part."""
        ...

    @property
    def slide_layout(self) -> SlideLayout:
        """|SlideLayout| object the slide in this part inherits appearance from."""
        ...

class SlideLayoutPart(BaseSlidePart):
    """Slide layout part.

    Corresponds to package files ``ppt/slideLayouts/slideLayout[1-9][0-9]*.xml``.
    """
    @lazyproperty
    def slide_layout(self) -> SlideLayout:
        """
        The |SlideLayout| object representing this part.
        """
        ...

    @property
    def slide_master(self) -> SlideMaster:
        """Slide master from which this slide layout inherits properties."""
        ...

class SlideMasterPart(BaseSlidePart):
    """Slide master part.

    Corresponds to package files ppt/slideMasters/slideMaster[1-9][0-9]*.xml.
    """
    def related_slide_layout(self, rId: str) -> SlideLayout:
        """Return |SlideLayout| related to this slide-master by key `rId`."""
        ...

    @lazyproperty
    def slide_master(self) -> SlideMaster:
        """
        The |SlideMaster| object representing this part.
        """
        ...
