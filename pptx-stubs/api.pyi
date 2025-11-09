from typing import IO

from pptx import presentation

def Presentation(pptx: str | IO[bytes] | None = ...) -> presentation.Presentation:
    """
    Return a |Presentation| object loaded from *pptx*, where *pptx* can be
    either a path to a ``.pptx`` file (a string) or a file-like object. If
    *pptx* is missing or ``None``, the built-in default presentation
    "template" is loaded.
    """
    ...
