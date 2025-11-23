from typing import IO

from pptx import presentation

def Presentation(pptx: str | IO[bytes] | None = ...) -> presentation.Presentation: ...
