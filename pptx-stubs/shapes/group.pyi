from pptx.action import ActionSetting
from pptx.dml.effect import ShadowFormat
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.shapes.groupshape import CT_GroupShape
from pptx.shapes.base import BaseShape
from pptx.shapes.shapetree import GroupShapes
from pptx.types import ProvidesPart
from pptx.util import lazyproperty

class GroupShape(BaseShape):
    _element: CT_GroupShape
    _grpSp: CT_GroupShape
    def __init__(self, grpSp: CT_GroupShape, parent: ProvidesPart) -> None: ...
    @lazyproperty
    def click_action(self) -> ActionSetting: ...
    @property
    def has_text_frame(self) -> bool: ...
    @lazyproperty
    def shadow(self) -> ShadowFormat: ...
    @property
    def shape_type(self) -> MSO_SHAPE_TYPE: ...
    @lazyproperty
    def shapes(self) -> GroupShapes: ...
