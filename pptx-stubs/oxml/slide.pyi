from collections.abc import Callable

from lxml.etree import _Element
from pptx.oxml.dml.fill import (
    CT_BlipFillProperties,
    CT_GradientFillProperties,
    CT_GroupFillProperties,
    CT_NoFillProperties,
    CT_PatternFillProperties,
    CT_SolidColorFillProperties,
    FillProperty,
)
from pptx.oxml.shapes.groupshape import CT_GroupShape
from pptx.oxml.xmlchemy import BaseOxmlElement

class _BaseSlideElement(BaseOxmlElement):
    cSld: CT_CommonSlideData

    @property
    def spTree(self) -> CT_GroupShape: ...

class CT_Background(BaseOxmlElement):
    _insert_bgPr: Callable[[CT_BackgroundProperties], None]

    @property
    def bgPr(self) -> CT_BackgroundProperties | None:
        """``<p:bgPr>`` child element or |None| if not present."""
        ...

    def get_or_add_bgPr(self) -> CT_BackgroundProperties:
        """Return the ``<p:bgPr>`` child element, newly added if not present."""
        ...

    @property
    def bgRef(self) -> _Element | None:
        """``<p:bgRef>`` child element or |None| if not present."""
        ...

    def get_or_add_bgRef(self) -> _Element:
        """Return the ``<p:bgRef>`` child element, newly added if not present."""
        ...

    def add_noFill_bgPr(self) -> CT_BackgroundProperties:
        """Return a new `p:bgPr` element with noFill properties."""
        ...

class CT_BackgroundProperties(BaseOxmlElement):
    @property
    def noFill(self) -> CT_NoFillProperties:
        """``<a:noFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_noFill(self) -> CT_NoFillProperties:
        """Return the ``<a:noFill>`` child, replacing any other group element if found."""
        ...

    @property
    def solidFill(self) -> CT_SolidColorFillProperties:
        """``<a:solidFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_solidFill(self) -> CT_SolidColorFillProperties:
        """Return the ``<a:solidFill>`` child, replacing any other group element if found."""
        ...

    @property
    def gradFill(self) -> CT_GradientFillProperties:
        """``<a:gradFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_gradFill(self) -> CT_GradientFillProperties:
        """Return the ``<a:gradFill>`` child, replacing any other group element if found."""
        ...

    @property
    def blipFill(self) -> CT_BlipFillProperties:
        """``<a:blipFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_blipFill(self) -> CT_BlipFillProperties:
        """Return the ``<a:blipFill>`` child, replacing any other group element if found."""
        ...

    @property
    def pattFill(self) -> CT_PatternFillProperties:
        """``<a:pattFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_pattFill(self) -> CT_PatternFillProperties:
        """Return the ``<a:pattFill>`` child, replacing any other group element if found."""
        ...

    @property
    def grpFill(self) -> CT_GroupFillProperties:
        """``<a:grpFill>`` child element or |None| if not present."""
        ...

    def get_or_change_to_grpFill(self) -> CT_GroupFillProperties:
        """Return the ``<a:grpFill>`` child, replacing any other group element if found."""
        ...

    @property
    def eg_fillProperties(self) -> FillProperty | None:
        """Return the child element belonging to this element group, or |None| if no member child is present."""
        ...

class CT_CommonSlideData(BaseOxmlElement):
    _remove_bg: Callable[[], None]

    @property
    def bg(self) -> CT_Background | None:
        """``<p:bg>`` child element or |None| if not present."""
        ...

    def get_or_add_bg(self) -> CT_Background:
        """Return the ``<p:bg>`` child element, newly added if not present."""
        ...

    @property
    def spTree(self) -> CT_GroupShape:
        """Required ``<p:spTree>`` child element."""
        ...

    @property
    def name(self) -> str:
        """XsdString type-converted value of ``name`` attribute, or |""| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...
    def get_or_add_bgPr(self) -> CT_BackgroundProperties: ...

class CT_NotesMaster(_BaseSlideElement):
    @property
    def cSld(self) -> CT_CommonSlideData:
        """Required ``<p:cSld>`` child element."""
        ...

    @classmethod
    def new_default(cls) -> CT_NotesMaster: ...

class CT_NotesSlide(_BaseSlideElement):
    @property
    def cSld(self) -> CT_CommonSlideData:
        """Required ``<p:cSld>`` child element."""
        ...

    @classmethod
    def new(cls) -> CT_NotesSlide: ...

class CT_Slide(_BaseSlideElement):
    @property
    def cSld(self) -> CT_CommonSlideData:
        """Required ``<p:cSld>`` child element."""
        ...

    @property
    def clrMapOvr(self) -> _Element | None:
        """``<p:clrMapOvr>`` child element or |None| if not present."""
        ...

    def get_or_add_clrMapOvr(self) -> _Element:
        """Return the ``<p:clrMapOvr>`` child element, newly added if not present."""
        ...

    @property
    def timing(self) -> CT_SlideTiming | None:
        """``<p:timing>`` child element or |None| if not present."""
        ...

    def get_or_add_timing(self) -> CT_SlideTiming:
        """Return the ``<p:timing>`` child element, newly added if not present."""
        ...

    @classmethod
    def new(cls) -> CT_Slide:
        """Return new `p:sld` element configured as base slide shape."""
        ...

    @property
    def bg(self) -> CT_Background | None:
        """Return `p:bg` grandchild or None if not present."""
        ...

    def get_or_add_childTnLst(self) -> _Element: ...

class CT_SlideLayout(_BaseSlideElement):
    @property
    def cSld(self) -> CT_CommonSlideData:
        """Required ``<p:cSld>`` child element."""
        ...

class CT_SlideLayoutIdList(BaseOxmlElement):
    @property
    def sldLayoutId_lst(self) -> list[CT_SlideLayoutIdListEntry]:
        """A list containing each of the ``<p:sldLayoutId>`` child elements, in the order they appear."""
        ...

class CT_SlideLayoutIdListEntry(BaseOxmlElement):
    @property
    def rId(self) -> str:
        """XsdString type-converted value of ``r:id`` attribute."""
        ...

    @rId.setter
    def rId(self, value: str) -> None: ...

class CT_SlideMaster(_BaseSlideElement):
    @property
    def cSld(self) -> CT_CommonSlideData:
        """Required ``<p:cSld>`` child element."""
        ...

    @property
    def sldLayoutIdLst(self) -> CT_SlideLayoutIdList | None:
        """``<p:sldLayoutIdLst>`` child element or |None| if not present."""
        ...

    def get_or_add_sldLayoutIdLst(self) -> CT_SlideLayoutIdList:
        """Return the ``<p:sldLayoutIdLst>`` child element, newly added if not present."""
        ...

class CT_SlideTiming(BaseOxmlElement):
    @property
    def tnLst(self) -> _Element | None:
        """``<p:tnLst>`` child element or |None| if not present."""
        ...

    def get_or_add_tnLst(self) -> _Element:
        """Return the ``<p:tnLst>`` child element, newly added if not present."""
        ...

class CT_TimeNodeList(BaseOxmlElement):
    def add_video(self, shape_id) -> CT_TLMediaNodeVideo: ...

class CT_TLMediaNodeVideo(BaseOxmlElement):
    @property
    def cMediaNode(self) -> _Element:
        """Required ``<p:cMediaNode>`` child element."""
        ...
