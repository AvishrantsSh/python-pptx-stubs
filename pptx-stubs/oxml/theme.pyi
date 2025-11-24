from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_OfficeStyleSheet(BaseOxmlElement):
    @classmethod
    def new_default(cls) -> CT_OfficeStyleSheet: ...
