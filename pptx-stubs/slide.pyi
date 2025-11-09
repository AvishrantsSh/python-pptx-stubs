from collections.abc import Generator, Iterator
from typing import Any

from pptx.dml.fill import FillFormat
from pptx.oxml.presentation import CT_SlideIdList, CT_SlideMasterIdList
from pptx.oxml.slide import CT_CommonSlideData, CT_NotesSlide, CT_Slide, CT_SlideLayoutIdList, CT_SlideMaster
from pptx.parts.presentation import PresentationPart
from pptx.parts.slide import SlideLayoutPart, SlideMasterPart, SlidePart
from pptx.presentation import Presentation
from pptx.shapes.placeholder import LayoutPlaceholder, NotesSlidePlaceholder
from pptx.shapes.shapetree import (
    LayoutPlaceholders,
    LayoutShapes,
    MasterPlaceholders,
    MasterShapes,
    NotesSlidePlaceholders,
    NotesSlideShapes,
    SlidePlaceholders,
    SlideShapes,
)
from pptx.shared import ElementProxy, ParentedElementProxy, PartElementProxy
from pptx.text.text import TextFrame
from pptx.util import lazyproperty

class _BaseSlide(PartElementProxy):
    """Base class for slide objects, including masters, layouts and notes."""

    _element: CT_Slide
    @lazyproperty
    def background(self) -> _Background:
        """|_Background| object providing slide background properties.

        This property returns a |_Background| object whether or not the
        slide, master, or layout has an explicitly defined background.

        The same |_Background| object is returned on every call for the same
        slide object.
        """
        ...

    @property
    def name(self) -> str:
        """String representing the internal name of this slide.

        Returns an empty string (`''`) if no name is assigned. Assigning an empty string or |None|
        to this property causes any name to be removed.
        """
        ...

    @name.setter
    def name(self, value: str | None) -> None: ...

class _BaseMaster(_BaseSlide):
    """Base class for master objects such as |SlideMaster| and |NotesMaster|.

    Provides access to placeholders and regular shapes.
    """
    @lazyproperty
    def placeholders(self) -> MasterPlaceholders:
        """|MasterPlaceholders| collection of placeholder shapes in this master.

        Sequence sorted in `idx` order.
        """
        ...

    @lazyproperty
    def shapes(self) -> MasterShapes:
        """
        Instance of |MasterShapes| containing sequence of shape objects
        appearing on this slide.
        """
        ...

class NotesMaster(_BaseMaster):
    """Proxy for the notes master XML document.

    Provides access to shapes, the most commonly used of which are placeholders.
    """

    ...

class NotesSlide(_BaseSlide):
    """Notes slide object.

    Provides access to slide notes placeholder and other shapes on the notes handout
    page.
    """

    element: CT_NotesSlide
    def clone_master_placeholders(self, notes_master: NotesMaster) -> None:
        """Selectively add placeholder shape elements from `notes_master`.

        Selected placeholder shape elements from `notes_master` are added to the shapes
        collection of this notes slide. Z-order of placeholders is preserved. Certain
        placeholders (header, date, footer) are not cloned.
        """
        ...

    @property
    def notes_placeholder(self) -> NotesSlidePlaceholder | None:
        """the notes placeholder on this notes slide, the shape that contains the actual notes text.

        Return |None| if no notes placeholder is present; while this is probably uncommon, it can
        happen if the notes master does not have a body placeholder, or if the notes placeholder
        has been deleted from the notes slide.
        """
        ...

    @property
    def notes_text_frame(self) -> TextFrame | None:
        """The text frame of the notes placeholder on this notes slide.

        |None| if there is no notes placeholder. This is a shortcut to accommodate the common case
        of simply adding "notes" text to the notes "page".
        """
        ...

    @lazyproperty
    def placeholders(self) -> NotesSlidePlaceholders:
        """Instance of |NotesSlidePlaceholders| for this notes-slide.

        Contains the sequence of placeholder shapes in this notes slide.
        """
        ...

    @lazyproperty
    def shapes(self) -> NotesSlideShapes:
        """Sequence of shape objects appearing on this notes slide."""
        ...

class Slide(_BaseSlide):
    """Slide object. Provides access to shapes and slide-level properties."""

    part: SlidePart
    @property
    def follow_master_background(self) -> bool:
        """|True| if this slide inherits the slide master background.

        Assigning |False| causes background inheritance from the master to be
        interrupted; if there is no custom background for this slide,
        a default background is added. If a custom background already exists
        for this slide, assigning |False| has no effect.

        Assigning |True| causes any custom background for this slide to be
        deleted and inheritance from the master restored.
        """
        ...

    @property
    def has_notes_slide(self) -> bool:
        """`True` if this slide has a notes slide, `False` otherwise.

        A notes slide is created by :attr:`.notes_slide` when one doesn't exist; use this property
        to test for a notes slide without the possible side effect of creating one.
        """
        ...

    @property
    def notes_slide(self) -> NotesSlide:
        """The |NotesSlide| instance for this slide.

        If the slide does not have a notes slide, one is created. The same single instance is
        returned on each call.
        """
        ...

    @lazyproperty
    def placeholders(self) -> SlidePlaceholders:
        """Sequence of placeholder shapes in this slide."""
        ...

    @lazyproperty
    def shapes(self) -> SlideShapes:
        """Sequence of shape objects appearing on this slide."""
        ...

    @property
    def slide_id(self) -> int:
        """Integer value that uniquely identifies this slide within this presentation.

        The slide id does not change if the position of this slide in the slide sequence is changed
        by adding, rearranging, or deleting slides.
        """
        ...

    @property
    def slide_layout(self) -> SlideLayout:
        """|SlideLayout| object this slide inherits appearance from."""
        ...

class Slides(ParentedElementProxy):
    """Sequence of slides belonging to an instance of |Presentation|.

    Has list semantics for access to individual slides. Supports indexed access, len(), and
    iteration.
    """

    part: PresentationPart
    def __init__(self, sldIdLst: CT_SlideIdList, prs: Presentation) -> None: ...
    def __getitem__(self, idx: int) -> Slide:
        """Provide indexed access, (e.g. 'slides[0]')."""
        ...

    def __iter__(self) -> Iterator[Slide]:
        """Support iteration, e.g. `for slide in slides:`."""
        ...

    def __len__(self) -> int:
        """Support len() built-in function, e.g. `len(slides) == 4`."""
        ...

    def add_slide(self, slide_layout: SlideLayout) -> Slide:
        """Return a newly added slide that inherits layout from `slide_layout`."""
        ...

    def get(self, slide_id: int, default: Slide | None = ...) -> Slide | None:
        """Return the slide identified by int `slide_id` in this presentation.

        Returns `default` if not found.
        """
        ...

    def index(self, slide: Slide) -> int:
        """Map `slide` to its zero-based position in this slide sequence.

        Raises |ValueError| on *slide* not present.
        """
        ...

class SlideLayout(_BaseSlide):
    """Slide layout object.

    Provides access to placeholders, regular shapes, and slide layout-level properties.
    """

    part: SlideLayoutPart
    def iter_cloneable_placeholders(self) -> Iterator[LayoutPlaceholder]:
        """Generate layout-placeholders on this slide-layout that should be cloned to a new slide.

        Used when creating a new slide from this slide-layout.
        """
        ...

    @lazyproperty
    def placeholders(self) -> LayoutPlaceholders:
        """Sequence of placeholder shapes in this slide layout.

        Placeholders appear in `idx` order.
        """
        ...

    @lazyproperty
    def shapes(self) -> LayoutShapes:
        """Sequence of shapes appearing on this slide layout."""
        ...

    @property
    def slide_master(self) -> SlideMaster:
        """Slide master from which this slide-layout inherits properties."""
        ...

    @property
    def used_by_slides(self) -> tuple[Slide, ...]:
        """Tuple of slide objects based on this slide layout."""
        ...

class SlideLayouts(ParentedElementProxy):
    """Sequence of slide layouts belonging to a slide-master.

    Supports indexed access, len(), iteration, index() and remove().
    """

    part: SlideMasterPart
    def __init__(self, sldLayoutIdLst: CT_SlideLayoutIdList, parent: SlideMaster) -> None: ...
    def __getitem__(self, idx: int) -> SlideLayout:
        """Provides indexed access, e.g. `slide_layouts[2]`."""
        ...

    def __iter__(self) -> Iterator[SlideLayout]:
        """Generate each |SlideLayout| in the collection, in sequence."""
        ...

    def __len__(self) -> int:
        """Support len() built-in function, e.g. `len(slides) == 4`."""
        ...

    def get_by_name(self, name: str, default: SlideLayout | None = ...) -> SlideLayout | None:
        """Return SlideLayout object having `name`, or `default` if not found."""
        ...

    def index(self, slide_layout: SlideLayout) -> int:
        """Return zero-based index of `slide_layout` in this collection.

        Raises `ValueError` if `slide_layout` is not present in this collection.
        """
        ...

    def remove(self, slide_layout: SlideLayout) -> None:
        """Remove `slide_layout` from the collection.

        Raises ValueError when `slide_layout` is in use; a slide layout which is the basis for one
        or more slides cannot be removed.
        """
        ...

class SlideMaster(_BaseMaster):
    """Slide master object.

    Provides access to slide layouts. Access to placeholders, regular shapes, and slide master-level
    properties is inherited from |_BaseMaster|.
    """

    _element: CT_SlideMaster
    @lazyproperty
    def slide_layouts(self) -> SlideLayouts:
        """|SlideLayouts| object providing access to this slide-master's layouts."""
        ...

class SlideMasters(ParentedElementProxy):
    """Sequence of |SlideMaster| objects belonging to a presentation.

    Has list access semantics, supporting indexed access, len(), and iteration.
    """

    part: PresentationPart
    def __init__(self, sldMasterIdLst: CT_SlideMasterIdList, parent: Presentation) -> None: ...
    def __getitem__(self, idx: int) -> SlideMaster:
        """Provides indexed access, e.g. `slide_masters[2]`."""
        ...

    def __iter__(self) -> Generator[SlideMaster, Any, None]:
        """Generate each |SlideMaster| instance in the collection, in sequence."""
        ...

    def __len__(self) -> int:
        """Support len() built-in function, e.g. `len(slide_masters) == 4`."""
        ...

class _Background(ElementProxy):
    """Provides access to slide background properties.

    Note that the presence of this object does not by itself imply an
    explicitly-defined background; a slide with an inherited background still
    has a |_Background| object.
    """
    def __init__(self, cSld: CT_CommonSlideData) -> None: ...
    @lazyproperty
    def fill(self) -> FillFormat:
        """|FillFormat| instance for this background.

        This |FillFormat| object is used to interrogate or specify the fill
        of the slide background.

        Note that accessing this property is potentially destructive. A slide
        background can also be specified by a background style reference and
        accessing this property will remove that reference, if present, and
        replace it with NoFill. This is frequently the case for a slide
        master background.

        This is also the case when there is no explicitly defined background
        (background is inherited); merely accessing this property will cause
        the background to be set to NoFill and the inheritance link will be
        interrupted. This is frequently the case for a slide background.

        Of course, if you are accessing this property in order to set the
        fill, then these changes are of no consequence, but the existing
        background cannot be reliably interrogated using this property unless
        you have already established it is an explicit fill.

        If the background is already a fill, then accessing this property
        makes no changes to the current background.
        """
        ...
