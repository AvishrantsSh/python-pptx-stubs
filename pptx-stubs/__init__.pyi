from pptx.api import Presentation
from pptx.opc.package import Part

content_type_to_part_class_map: dict[str, type[Part]] = ...

__all__ = ["Presentation"]
