from pptx.opc.package import XmlPart
from pptx.types import ProvidesPart

class Subshape:
    def __init__(self, parent: ProvidesPart) -> None: ...
    @property
    def part(self) -> XmlPart: ...
