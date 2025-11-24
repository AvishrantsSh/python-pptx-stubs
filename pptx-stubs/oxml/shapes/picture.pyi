from pptx.oxml.dml.fill import CT_BlipFillProperties
from pptx.oxml.shapes.shared import (
    BaseShapeElement,
    CT_ApplicationNonVisualDrawingProps,
    CT_LineProperties,
    CT_NonVisualDrawingProps,
    CT_ShapeProperties,
)
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.util import Length

class CT_Picture(BaseShapeElement):
    @property
    def nvPicPr(self) -> CT_PictureNonVisual:
        """Required ``<p:nvPicPr>`` child element."""
        ...

    @property
    def blipFill(self) -> CT_BlipFillProperties:
        """Required ``<p:blipFill>`` child element."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties:
        """Required ``<p:spPr>`` child element."""
        ...

    @property
    def blip_rId(self) -> str | None: ...
    def crop_to_fit(self, image_size: tuple[float, float], view_size: tuple[float, float]) -> None: ...
    def get_or_add_ln(self) -> CT_LineProperties: ...
    @property
    def ln(self) -> CT_LineProperties | None: ...
    @classmethod
    def new_ph_pic(cls, id_: int, name: str, desc: str, rId: str) -> CT_Picture: ...
    @classmethod
    def new_pic(cls, shape_id: int, name: str, desc: str, rId: str, x: int, y: int, cx: int, cy: int) -> CT_Picture: ...
    @classmethod
    def new_video_pic(
        cls,
        shape_id: int,
        shape_name: str,
        video_rId: str,
        media_rId: str,
        poster_frame_rId: str,
        x: Length,
        y: Length,
        cx: Length,
        cy: Length,
    ) -> CT_Picture: ...
    @property
    def srcRect_b(self) -> float: ...
    @srcRect_b.setter
    def srcRect_b(self, value: float) -> None: ...
    @property
    def srcRect_l(self) -> float: ...
    @srcRect_l.setter
    def srcRect_l(self, value: float) -> None: ...
    @property
    def srcRect_r(self) -> float: ...
    @srcRect_r.setter
    def srcRect_r(self, value: float) -> None: ...
    @property
    def srcRect_t(self) -> float: ...
    @srcRect_t.setter
    def srcRect_t(self, value: float) -> None: ...

class CT_PictureNonVisual(BaseOxmlElement):
    @property
    def cNvPr(self) -> CT_NonVisualDrawingProps:
        """Required ``<p:cNvPr>`` child element."""
        ...

    @property
    def nvPr(self) -> CT_ApplicationNonVisualDrawingProps:
        """Required ``<p:nvPr>`` child element."""
        ...
