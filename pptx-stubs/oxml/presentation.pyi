from collections.abc import Callable

from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Presentation(BaseOxmlElement):
    @property
    def sldMasterIdLst(self) -> CT_SlideMasterIdList | None:
        """``<p:sldMasterIdLst>`` child element or |None| if not present."""
        ...

    def get_or_add_sldMasterIdLst(self) -> CT_SlideMasterIdList:
        """Return the ``<p:sldMasterIdLst>`` child element, newly added if not present."""
        ...

    @property
    def sldIdLst(self) -> CT_SlideIdList | None:
        """``<p:sldIdLst>`` child element or |None| if not present."""
        ...

    def get_or_add_sldIdLst(self) -> CT_SlideIdList:
        """Return the ``<p:sldIdLst>`` child element, newly added if not present."""
        ...

    @property
    def sldSz(self) -> CT_SlideSize | None:
        """``<p:sldSz>`` child element or |None| if not present."""
        ...

    def get_or_add_sldSz(self) -> CT_SlideSize:
        """Return the ``<p:sldSz>`` child element, newly added if not present."""
        ...

class CT_SlideId(BaseOxmlElement):
    @property
    def id(self) -> int:
        """ST_SlideId type-converted value of ``id`` attribute."""
        ...

    @id.setter
    def id(self, value: int) -> None: ...
    @property
    def rId(self) -> str:
        """XsdString type-converted value of ``r:id`` attribute."""
        ...

    @rId.setter
    def rId(self, value: str) -> None: ...

class CT_SlideIdList(BaseOxmlElement):
    _add_sldId: Callable[..., CT_SlideId]
    @property
    def sldId_lst(self) -> list[CT_SlideId]:
        """A list containing each of the ``<p:sldId>`` child elements, in the order they appear."""
        ...

    def add_sldId(self, rId: str) -> CT_SlideId: ...

class CT_SlideMasterIdList(BaseOxmlElement):
    @property
    def sldMasterId_lst(self) -> list[CT_SlideMasterIdListEntry]:
        """A list containing each of the ``<p:sldMasterId>`` child elements, in the order they appear."""
        ...

class CT_SlideMasterIdListEntry(BaseOxmlElement):
    @property
    def rId(self) -> str:
        """XsdString type-converted value of ``r:id`` attribute."""
        ...

    @rId.setter
    def rId(self, value: str) -> None: ...

class CT_SlideSize(BaseOxmlElement):
    @property
    def cx(self) -> int:
        """ST_SlideSizeCoordinate type-converted value of ``cx`` attribute."""
        ...

    @cx.setter
    def cx(self, value: int) -> None: ...
    @property
    def cy(self) -> int:
        """ST_SlideSizeCoordinate type-converted value of ``cy`` attribute."""
        ...

    @cy.setter
    def cy(self, value: int) -> None: ...
