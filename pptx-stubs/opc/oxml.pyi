from collections.abc import Callable

from pptx.opc.packuri import PackURI
from pptx.oxml.xmlchemy import BaseOxmlElement

nsmap: dict[str, str] = ...

def oxml_to_encoded_bytes(
    element: BaseOxmlElement, encoding: str = ..., pretty_print: bool = ..., standalone: bool | None = ...
) -> bytes: ...
def oxml_tostring(
    elm: BaseOxmlElement, encoding: str | None = ..., pretty_print: bool = ..., standalone: bool | None = ...
): ...
def serialize_part_xml(part_elm: BaseOxmlElement) -> bytes: ...

class CT_Default(BaseOxmlElement):
    @property
    def extension(self) -> str:
        """ST_Extension type-converted value of ``Extension`` attribute."""
        ...

    @extension.setter
    def extension(self, value: str) -> None: ...
    @property
    def contentType(self) -> str:
        """ST_ContentType type-converted value of ``ContentType`` attribute."""
        ...

    @contentType.setter
    def contentType(self, value: str) -> None: ...

class CT_Override(BaseOxmlElement):
    @property
    def partName(self) -> str:
        """XsdAnyUri type-converted value of ``PartName`` attribute."""
        ...

    @partName.setter
    def partName(self, value: str) -> None: ...
    @property
    def contentType(self) -> str:
        """ST_ContentType type-converted value of ``ContentType`` attribute."""
        ...

    @contentType.setter
    def contentType(self, value: str) -> None: ...

class CT_Relationship(BaseOxmlElement):
    @property
    def rId(self) -> str:
        """XsdId type-converted value of ``Id`` attribute."""
        ...

    @rId.setter
    def rId(self, value: str) -> None: ...
    @property
    def reltype(self) -> str:
        """XsdAnyUri type-converted value of ``Type`` attribute."""
        ...

    @reltype.setter
    def reltype(self, value: str) -> None: ...
    @property
    def target_ref(self) -> str:
        """XsdAnyUri type-converted value of ``Target`` attribute."""
        ...

    @target_ref.setter
    def target_ref(self, value: str) -> None: ...
    @property
    def targetMode(self) -> str:
        """ST_TargetMode type-converted value of ``TargetMode`` attribute, or |RELATIONSHIP_TARGET_MODE.INTERNAL| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @targetMode.setter
    def targetMode(self, value: str) -> None: ...
    @classmethod
    def new(cls, rId: str, reltype: str, target_ref: str, target_mode: str = ...) -> CT_Relationship: ...

class CT_Relationships(BaseOxmlElement):
    _insert_relationship: Callable[[CT_Relationship], CT_Relationship]

    @property
    def relationship_lst(self) -> list[CT_Relationship]:
        """A list containing each of the ``<pr:Relationship>`` child elements, in the order they appear."""
        ...

    def add_rel(self, rId: str, reltype: str, target: str, is_external: bool = ...) -> CT_Relationship: ...
    @classmethod
    def new(cls) -> CT_Relationships: ...
    @property
    def xml_file_bytes(self) -> bytes: ...

class CT_Types(BaseOxmlElement):
    _add_default: Callable[..., CT_Default]
    _add_override: Callable[..., CT_Override]

    @property
    def default_lst(self) -> list[CT_Default]:
        """A list containing each of the ``<ct:Default>`` child elements, in the order they appear."""
        ...

    @property
    def override_lst(self) -> list[CT_Override]:
        """A list containing each of the ``<ct:Override>`` child elements, in the order they appear."""
        ...

    def add_default(self, ext: str, content_type: str) -> CT_Default: ...
    def add_override(self, partname: PackURI, content_type: str) -> CT_Override: ...
    @classmethod
    def new(cls) -> CT_Types: ...
