from pptx.dml.fill import FillFormat
from pptx.dml.line import LineFormat
from pptx.shared import ElementProxy
from pptx.util import lazyproperty

class ChartFormat(ElementProxy):
    @lazyproperty
    def fill(self) -> FillFormat: ...
    @lazyproperty
    def line(self) -> LineFormat: ...
