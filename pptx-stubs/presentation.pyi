from typing import IO

from pptx.oxml.presentation import CT_Presentation
from pptx.parts.coreprops import CorePropertiesPart
from pptx.parts.presentation import PresentationPart
from pptx.shared import PartElementProxy
from pptx.slide import NotesMaster, SlideLayouts, SlideMaster, SlideMasters, Slides
from pptx.util import Length, lazyproperty

class Presentation(PartElementProxy):
    """PresentationML (PML) presentation.

    Not intended to be constructed directly. Use :func:`pptx.Presentation` to open or
    create a presentation.
    """

    _element: CT_Presentation
    part: PresentationPart
    @property
    def core_properties(self) -> CorePropertiesPart:
        """|CoreProperties| instance for this presentation.

        Provides read/write access to the Dublin Core document properties for the presentation.
        """
        ...

    @property
    def notes_master(self) -> NotesMaster:
        """Instance of |NotesMaster| for this presentation.

        If the presentation does not have a notes master, one is created from a default template
        and returned. The same single instance is returned on each call.
        """
        ...

    def save(self, file: str | IO[bytes]) -> None:
        """Writes this presentation to `file`.

        `file` can be either a file-path or a file-like object open for writing bytes.
        """
        ...

    @property
    def slide_height(self) -> Length | None:
        """Height of slides in this presentation, in English Metric Units (EMU).

        Returns |None| if no slide width is defined. Read/write.
        """
        ...

    @slide_height.setter
    def slide_height(self, height: Length) -> None: ...
    @property
    def slide_layouts(self) -> SlideLayouts:
        """|SlideLayouts| collection belonging to the first |SlideMaster| of this presentation.

        A presentation can have more than one slide master and each master will have its own set
        of layouts. This property is a convenience for the common case where the presentation has
        only a single slide master.
        """
        ...

    @property
    def slide_master(self) -> SlideMaster:
        """
        First |SlideMaster| object belonging to this presentation. Typically,
        presentations have only a single slide master. This property provides
        simpler access in that common case.
        """
        ...

    @lazyproperty
    def slide_masters(self) -> SlideMasters:
        """|SlideMasters| collection of slide-masters belonging to this presentation."""
        ...

    @property
    def slide_width(self) -> Length | None:
        """
        Width of slides in this presentation, in English Metric Units (EMU).
        Returns |None| if no slide width is defined. Read/write.
        """
        ...

    @slide_width.setter
    def slide_width(self, width: Length) -> None: ...
    @lazyproperty
    def slides(self) -> Slides:
        """|Slides| object containing the slides in this presentation."""
        ...
