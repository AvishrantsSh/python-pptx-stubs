class PythonPptxError(Exception):
    """Generic error class."""

    ...

class PackageNotFoundError(PythonPptxError):
    """
    Raised when a package cannot be found at the specified path.
    """

    ...

class InvalidXmlError(PythonPptxError):
    """
    Raised when a value is encountered in the XML that is not valid according
    to the schema.
    """

    ...
