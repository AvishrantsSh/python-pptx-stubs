from pptx.oxml.shapes.groupshape import CT_GroupShapeProperties
from pptx.oxml.shapes.shared import CT_ShapeProperties

class ShadowFormat:
    _element: CT_ShapeProperties | CT_GroupShapeProperties
    def __init__(self, spPr: CT_ShapeProperties | CT_GroupShapeProperties) -> None: ...
    @property
    def inherit(self) -> bool: ...
    @inherit.setter
    def inherit(self, value: bool) -> None: ...
