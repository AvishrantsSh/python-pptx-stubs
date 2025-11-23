from lxml.etree import _Element
from pptx.oxml.shapes.shared import CT_ShapeProperties
from pptx.oxml.text import CT_TextBody
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Boolean(BaseOxmlElement):
    @property
    def val(self) -> bool:
        """XsdBoolean type-converted value of ``val`` attribute, or |True| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: bool) -> None: ...

class CT_Boolean_Explicit(BaseOxmlElement):
    @property
    def _val(self) -> bool:
        """XsdBoolean type-converted value of ``val`` attribute, or |True| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @_val.setter
    def _val(self, value: bool) -> None: ...
    @property
    def val(self) -> bool: ...
    @val.setter
    def val(self, value: bool) -> None: ...

class CT_Double(BaseOxmlElement):
    @property
    def val(self) -> float:
        """XsdDouble type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: float) -> None: ...

class CT_Layout(BaseOxmlElement):
    @property
    def manualLayout(self) -> CT_ManualLayout | None:
        """``<c:manualLayout>`` child element or |None| if not present."""
        ...

    def get_or_add_manualLayout(self) -> CT_ManualLayout:
        """Return the ``<c:manualLayout>`` child element, newly added if not present."""
        ...

    @property
    def horz_offset(self) -> float: ...
    @horz_offset.setter
    def horz_offset(self, offset: float) -> None: ...

class CT_LayoutMode(BaseOxmlElement):
    @property
    def val(self) -> str:
        """ST_LayoutMode type-converted value of ``val`` attribute, or |ST_LayoutMode.FACTOR| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: str) -> None: ...

class CT_ManualLayout(BaseOxmlElement):
    @property
    def xMode(self) -> CT_LayoutMode | None:
        """``<c:xMode>`` child element or |None| if not present."""
        ...

    def get_or_add_xMode(self) -> CT_LayoutMode:
        """Return the ``<c:xMode>`` child element, newly added if not present."""
        ...

    @property
    def x(self) -> CT_Double | None:
        """``<c:x>`` child element or |None| if not present."""
        ...

    def get_or_add_x(self) -> CT_Double:
        """Return the ``<c:x>`` child element, newly added if not present."""
        ...

    @property
    def horz_offset(self) -> float: ...
    @horz_offset.setter
    def horz_offset(self, offset: float) -> None: ...

class CT_NumFmt(BaseOxmlElement):
    @property
    def formatCode(self) -> str:
        """XsdString type-converted value of ``formatCode`` attribute."""
        ...

    @formatCode.setter
    def formatCode(self, value: str) -> None: ...
    @property
    def sourceLinked(self) -> bool | None:
        """XsdBoolean type-converted value of ``sourceLinked`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @sourceLinked.setter
    def sourceLinked(self, value: bool | None) -> None: ...

class CT_Title(BaseOxmlElement):
    @property
    def tx(self) -> CT_Tx | None:
        """``<c:tx>`` child element or |None| if not present."""
        ...

    def get_or_add_tx(self) -> CT_Tx:
        """Return the ``<c:tx>`` child element, newly added if not present."""
        ...

    @property
    def spPr(self) -> CT_ShapeProperties | None:
        """``<c:spPr>`` child element or |None| if not present."""
        ...

    def get_or_add_spPr(self) -> CT_ShapeProperties:
        """Return the ``<c:spPr>`` child element, newly added if not present."""
        ...

    def get_or_add_tx_rich(self) -> CT_TextBody: ...
    @property
    def tx_rich(self) -> CT_TextBody | None: ...
    @staticmethod
    def new_title() -> CT_Title: ...

class CT_Tx(BaseOxmlElement):
    @property
    def strRef(self) -> _Element | None:
        """``<c:strRef>`` child element or |None| if not present."""
        ...

    def get_or_add_strRef(self) -> _Element:
        """Return the ``<c:strRef>`` child element, newly added if not present."""
        ...

    @property
    def rich(self) -> CT_TextBody | None:
        """``<c:rich>`` child element or |None| if not present."""
        ...

    def get_or_add_rich(self) -> CT_TextBody:
        """Return the ``<c:rich>`` child element, newly added if not present."""
        ...

class CT_UnsignedInt(BaseOxmlElement):
    @property
    def val(self) -> int:
        """XsdUnsignedInt type-converted value of ``val`` attribute."""
        ...

    @val.setter
    def val(self, value: int) -> None: ...
