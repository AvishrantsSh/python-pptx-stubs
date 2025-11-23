from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_PresetLineDashProperties(BaseOxmlElement):
    @property
    def val(self) -> MSO_LINE_DASH_STYLE | None:
        """MSO_LINE_DASH_STYLE type-converted value of ``val`` attribute, or |None| if not present. Assigning the default value causes the attribute to be removed from the element."""
        ...

    @val.setter
    def val(self, value: MSO_LINE_DASH_STYLE | None) -> None: ...
