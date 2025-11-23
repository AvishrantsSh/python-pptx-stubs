from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Hyperlink(BaseOxmlElement):
    @property
    def rId(self) -> str | None:
        """XsdString type-converted value of ``r:id`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @rId.setter
    def rId(self, value: str | None) -> None: ...
    @property
    def action(self) -> str | None:
        """XsdString type-converted value of ``action`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @action.setter
    def action(self, value: str | None) -> None: ...
    @property
    def action_fields(self) -> dict[str, str]: ...
    @property
    def action_verb(self) -> str | None: ...
