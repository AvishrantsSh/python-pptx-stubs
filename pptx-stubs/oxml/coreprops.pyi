from datetime import datetime
from re import Pattern

from lxml.etree import _Element
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_CoreProperties(BaseOxmlElement):
    _coreProperties_tmpl: str = ...
    _offset_pattern: Pattern[str] = ...

    @property
    def category(self) -> _Element | None:
        """``<cp:category>`` child element or |None| if not present."""
        ...

    def get_or_add_category(self) -> _Element:
        """Return the ``<cp:category>`` child element, newly added if not present."""
        ...

    @property
    def contentStatus(self) -> _Element | None:
        """``<cp:contentStatus>`` child element or |None| if not present."""
        ...

    def get_or_add_contentStatus(self) -> _Element:
        """Return the ``<cp:contentStatus>`` child element, newly added if not present."""
        ...

    @property
    def created(self) -> _Element | None:
        """``<dcterms:created>`` child element or |None| if not present."""
        ...

    def get_or_add_created(self) -> _Element:
        """Return the ``<dcterms:created>`` child element, newly added if not present."""
        ...

    @property
    def creator(self) -> _Element | None:
        """``<dc:creator>`` child element or |None| if not present."""
        ...

    def get_or_add_creator(self) -> _Element:
        """Return the ``<dc:creator>`` child element, newly added if not present."""
        ...

    @property
    def description(self) -> _Element | None:
        """``<dc:description>`` child element or |None| if not present."""
        ...

    def get_or_add_description(self) -> _Element:
        """Return the ``<dc:description>`` child element, newly added if not present."""
        ...

    @property
    def identifier(self) -> _Element | None:
        """``<dc:identifier>`` child element or |None| if not present."""
        ...

    def get_or_add_identifier(self) -> _Element:
        """Return the ``<dc:identifier>`` child element, newly added if not present."""
        ...

    @property
    def keywords(self) -> _Element | None:
        """``<cp:keywords>`` child element or |None| if not present."""
        ...

    def get_or_add_keywords(self) -> _Element:
        """Return the ``<cp:keywords>`` child element, newly added if not present."""
        ...

    @property
    def language(self) -> _Element | None:
        """``<dc:language>`` child element or |None| if not present."""
        ...

    def get_or_add_language(self) -> _Element:
        """Return the ``<dc:language>`` child element, newly added if not present."""
        ...

    @property
    def lastModifiedBy(self) -> _Element | None:
        """``<cp:lastModifiedBy>`` child element or |None| if not present."""
        ...

    def get_or_add_lastModifiedBy(self) -> _Element:
        """Return the ``<cp:lastModifiedBy>`` child element, newly added if not present."""
        ...

    @property
    def lastPrinted(self) -> _Element | None:
        """``<cp:lastPrinted>`` child element or |None| if not present."""
        ...

    def get_or_add_lastPrinted(self) -> _Element:
        """Return the ``<cp:lastPrinted>`` child element, newly added if not present."""
        ...

    @property
    def modified(self) -> _Element | None:
        """``<dcterms:modified>`` child element or |None| if not present."""
        ...

    def get_or_add_modified(self) -> _Element:
        """Return the ``<dcterms:modified>`` child element, newly added if not present."""
        ...

    @property
    def revision(self) -> _Element | None:
        """``<cp:revision>`` child element or |None| if not present."""
        ...

    def get_or_add_revision(self) -> _Element:
        """Return the ``<cp:revision>`` child element, newly added if not present."""
        ...

    @property
    def subject(self) -> _Element | None:
        """``<dc:subject>`` child element or |None| if not present."""
        ...

    def get_or_add_subject(self) -> _Element:
        """Return the ``<dc:subject>`` child element, newly added if not present."""
        ...

    @property
    def title(self) -> _Element | None:
        """``<dc:title>`` child element or |None| if not present."""
        ...

    def get_or_add_title(self) -> _Element:
        """Return the ``<dc:title>`` child element, newly added if not present."""
        ...

    @property
    def version(self) -> _Element | None:
        """``<cp:version>`` child element or |None| if not present."""
        ...

    def get_or_add_version(self) -> _Element:
        """Return the ``<cp:version>`` child element, newly added if not present."""
        ...

    @staticmethod
    def new_coreProperties() -> CT_CoreProperties:
        """Return a new `cp:coreProperties` element"""
        ...

    @property
    def author_text(self) -> str: ...
    @author_text.setter
    def author_text(self, value: str) -> None: ...
    @property
    def category_text(self) -> str: ...
    @category_text.setter
    def category_text(self, value: str) -> None: ...
    @property
    def comments_text(self) -> str: ...
    @comments_text.setter
    def comments_text(self, value: str) -> None: ...
    @property
    def contentStatus_text(self) -> str: ...
    @contentStatus_text.setter
    def contentStatus_text(self, value: str) -> None: ...
    @property
    def created_datetime(self) -> datetime | None: ...
    @created_datetime.setter
    def created_datetime(self, value: datetime) -> None: ...
    @property
    def identifier_text(self) -> str: ...
    @identifier_text.setter
    def identifier_text(self, value: str) -> None: ...
    @property
    def keywords_text(self) -> str: ...
    @keywords_text.setter
    def keywords_text(self, value: str) -> None: ...
    @property
    def language_text(self) -> str: ...
    @language_text.setter
    def language_text(self, value: str) -> None: ...
    @property
    def lastModifiedBy_text(self) -> str: ...
    @lastModifiedBy_text.setter
    def lastModifiedBy_text(self, value: str) -> None: ...
    @property
    def lastPrinted_datetime(self) -> datetime | None: ...
    @lastPrinted_datetime.setter
    def lastPrinted_datetime(self, value: datetime) -> None: ...
    @property
    def modified_datetime(self) -> datetime | None: ...
    @modified_datetime.setter
    def modified_datetime(self, value: datetime) -> None: ...
    @property
    def revision_number(self) -> int: ...
    @revision_number.setter
    def revision_number(self, value: int) -> None: ...
    @property
    def subject_text(self) -> str: ...
    @subject_text.setter
    def subject_text(self, value: str) -> None: ...
    @property
    def title_text(self) -> str: ...
    @title_text.setter
    def title_text(self, value: str) -> None: ...
    @property
    def version_text(self) -> str: ...
    @version_text.setter
    def version_text(self, value: str) -> None: ...
