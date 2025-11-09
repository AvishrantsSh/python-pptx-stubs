from pptx.opc.package import XmlPart
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.types import ProvidesPart

class ElementProxy:
    """Base class for lxml element proxy classes.

    An element proxy class is one whose primary responsibilities are fulfilled by manipulating the
    attributes and child elements of an XML element. They are the most common type of class in
    python-pptx other than custom element (oxml) classes.
    """
    def __init__(self, element: BaseOxmlElement) -> None: ...
    def __eq__(self, other: object) -> bool:
        """Return |True| if this proxy object refers to the same oxml element as does *other*.

        ElementProxy objects are value objects and should maintain no mutable local state.
        Equality for proxy objects is defined as referring to the same XML element, whether or not
        they are the same proxy object instance.
        """
        ...

    def __ne__(self, other: object) -> bool: ...
    @property
    def element(self) -> BaseOxmlElement:
        """The lxml element proxied by this object."""
        ...

class ParentedElementProxy(ElementProxy):
    """Provides access to ancestor objects and part.

    An ancestor may occasionally be required to provide a service, such as add or drop a
    relationship. Provides the :attr:`_parent` attribute to subclasses and the public
    :attr:`parent` read-only property.
    """
    def __init__(self, element: BaseOxmlElement, parent: ProvidesPart) -> None: ...
    @property
    def parent(self) -> ProvidesPart:
        """The ancestor proxy object to this one.

        For example, the parent of a shape is generally the |SlideShapes| object that contains it.
        """
        ...

    @property
    def part(self) -> XmlPart:
        """The package part containing this object."""
        ...

class PartElementProxy(ElementProxy):
    """Provides common members for proxy-objects that wrap a part's root element, e.g. `p:sld`."""
    def __init__(self, element: BaseOxmlElement, part: XmlPart) -> None: ...
    @property
    def part(self) -> XmlPart:
        """The package part containing this object."""
        ...
