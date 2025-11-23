from typing import Protocol

from pptx.opc.package import XmlPart
from pptx.util import Length

class ProvidesExtents(Protocol):
    @property
    def height(self) -> Length: ...
    @property
    def width(self) -> Length: ...

class ProvidesPart(Protocol):
    @property
    def part(self) -> XmlPart: ...
