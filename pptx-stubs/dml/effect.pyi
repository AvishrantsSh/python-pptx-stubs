from pptx.oxml.shapes.groupshape import CT_GroupShapeProperties
from pptx.oxml.shapes.shared import CT_ShapeProperties

class ShadowFormat:
    """Provides access to shadow effect on a shape."""
    def __init__(self, spPr: CT_ShapeProperties | CT_GroupShapeProperties) -> None: ...
    @property
    def inherit(self) -> bool:
        """True if shape inherits shadow settings.

        Read/write. An explicitly-defined shadow setting on a shape causes
        this property to return |False|. A shape with no explicitly-defined
        shadow setting inherits its shadow settings from the style hierarchy
        (and so returns |True|).

        Assigning |True| causes any explicitly-defined shadow setting to be
        removed and inheritance is restored. Note this has the side-effect of
        removing **all** explicitly-defined effects, such as glow and
        reflection, and restoring inheritance for all effects on the shape.
        Assigning |False| causes the inheritance link to be broken and **no**
        effects to appear on the shape.
        """
        ...

    @inherit.setter
    def inherit(self, value: bool) -> None: ...
