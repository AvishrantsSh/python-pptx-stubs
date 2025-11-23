from typing import Self

from pptx.opc.package import Part
from pptx.package import Package
from pptx.util import lazyproperty

class MediaPart(Part):
    @classmethod
    def new(cls, package: Package, media) -> Self: ...
    @lazyproperty
    def sha1(self) -> str: ...
