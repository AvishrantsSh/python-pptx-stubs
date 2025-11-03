from typing import Self

from pptx.enum.shapes import PROG_ID
from pptx.opc.package import Part
from pptx.package import Package
from pptx.util import lazyproperty

class EmbeddedPackagePart(Part):
    """A distinct OPC package, e.g. an Excel file, embedded in this PPTX package.

    Has a partname like: `ppt/embeddings/Microsoft_Excel_Sheet1.xlsx`.
    """
    @classmethod
    def factory(cls, prog_id: PROG_ID | str, object_blob: bytes, package: Package) -> Self:
        """Return a new |EmbeddedPackagePart| subclass instance added to *package*.

        The subclass is determined by `prog_id` which corresponds to the "application"
        used to open the "file-type" of `object_blob`. The returned part contains the
        bytes of `object_blob` and has the content-type also determined by `prog_id`.
        """
        ...

    @classmethod
    def new(cls, blob: bytes, package: Package) -> Self:
        """Return new |EmbeddedPackagePart| subclass object.

        The returned part object contains `blob` and is added to `package`.
        """
        ...

class EmbeddedDocxPart(EmbeddedPackagePart):
    """A Word .docx file stored in a part.

    This part-type arises when a Word document appears as an embedded OLE-object shape.
    """

    partname_template: str = ...
    content_type: lazyproperty[str] = ...

class EmbeddedPptxPart(EmbeddedPackagePart):
    """A PowerPoint file stored in a part.

    This part-type arises when a PowerPoint presentation (.pptx file) appears as an
    embedded OLE-object shape.
    """

    partname_template: str = ...
    content_type: lazyproperty[str] = ...

class EmbeddedXlsxPart(EmbeddedPackagePart):
    """An Excel file stored in a part.

    This part-type arises as the data source for a chart, but may also be the OLE-object
    for an embedded object shape.
    """

    partname_template: str = ...
    content_type: lazyproperty[str] = ...
