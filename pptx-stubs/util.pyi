from collections.abc import Callable
from typing import Any, Self

class Length(int):
    """Base class for length classes Inches, Emu, Cm, Mm, and Pt.

    Provides properties for converting length values to convenient units.
    """

    _EMUS_PER_INCH: int = ...
    _EMUS_PER_CENTIPOINT: int = ...
    _EMUS_PER_CM: int = ...
    _EMUS_PER_MM: int = ...
    _EMUS_PER_PT: int = ...
    def __new__(cls, emu: int) -> Self: ...
    @property
    def inches(self) -> float:
        """Floating point length in inches."""
        ...

    @property
    def centipoints(self) -> int:
        """Integer length in hundredths of a point (1/7200 inch).

        Used internally because PowerPoint stores font size in centipoints.
        """
        ...

    @property
    def cm(self) -> float:
        """Floating point length in centimeters."""
        ...

    @property
    def emu(self) -> int:
        """Integer length in English Metric Units."""
        ...

    @property
    def mm(self) -> float:
        """Floating point length in millimeters."""
        ...

    @property
    def pt(self) -> float:
        """Floating point length in points."""
        ...

class Inches(Length):
    """Convenience constructor for length in inches."""
    def __new__(cls, inches: float) -> Self: ...

class Centipoints(Length):
    """Convenience constructor for length in hundredths of a point."""
    def __new__(cls, centipoints: int) -> Self: ...

class Cm(Length):
    """Convenience constructor for length in centimeters."""
    def __new__(cls, cm: float) -> Self: ...

class Emu(Length):
    """Convenience constructor for length in english metric units."""
    def __new__(cls, emu: int) -> Self: ...

class Mm(Length):
    """Convenience constructor for length in millimeters."""
    def __new__(cls, mm: float) -> Self: ...

class Pt(Length):
    """Convenience value class for specifying a length in points."""
    def __new__(cls, points: float) -> Self: ...

class lazyproperty[T]:
    """Decorator like @property, but evaluated only on first access.

    Like @property, this can only be used to decorate methods having only a `self` parameter, and
    is accessed like an attribute on an instance, i.e. trailing parentheses are not used. Unlike
    @property, the decorated method is only evaluated on first access; the resulting value is
    cached and that same value returned on second and later access without re-evaluation of the
    method.

    Like @property, this class produces a *data descriptor* object, which is stored in the __dict__
    of the *class* under the name of the decorated method ('fget' nominally). The cached value is
    stored in the __dict__ of the *instance* under that same name.

    Because it is a data descriptor (as opposed to a *non-data descriptor*), its `__get__()` method
    is executed on each access of the decorated attribute; the __dict__ item of the same name is
    "shadowed" by the descriptor.

    While this may represent a performance improvement over a property, its greater benefit may be
    its other characteristics. One common use is to construct collaborator objects, removing that
    "real work" from the constructor, while still only executing once. It also de-couples client
    code from any sequencing considerations; if it's accessed from more than one location, it's
    assured it will be ready whenever needed.

    Loosely based on: https://stackoverflow.com/a/6849299/1902513.

    A lazyproperty is read-only. There is no counterpart to the optional "setter" (or deleter)
    behavior of an @property. This is critically important to maintaining its immutability and
    idempotence guarantees. Attempting to assign to a lazyproperty raises AttributeError
    unconditionally.

    The parameter names in the methods below correspond to this usage example::

        class Obj(object)

            @lazyproperty
            def fget(self):
                return 'some result'

        obj = Obj()

    Not suitable for wrapping a function (as opposed to a method) because it is not callable.
    """
    def __init__(self, fget: Callable[..., T]) -> None:
        """*fget* is the decorated method (a "getter" function).

        A lazyproperty is read-only, so there is only an *fget* function (a regular
        @property can also have an fset and fdel function). This name was chosen for
        consistency with Python's `property` class which uses this name for the
        corresponding parameter.
        """
        ...

    def __get__(self, obj: Any, type: Any = ...) -> T:  # noqa: A002
        """Called on each access of 'fget' attribute on class or instance.

        *self* is this instance of a lazyproperty descriptor "wrapping" the property
        method it decorates (`fget`, nominally).

        *obj* is the "host" object instance when the attribute is accessed from an
        object instance, e.g. `obj = Obj(); obj.fget`. *obj* is None when accessed on
        the class, e.g. `Obj.fget`.

        *type* is the class hosting the decorated getter method (`fget`) on both class
        and instance attribute access.
        """
        ...

    def __set__(self, obj: Any, value: Any) -> None:
        """Raises unconditionally, to preserve read-only behavior.

        This decorator is intended to implement immutable (and idempotent) object
        attributes. For that reason, assignment to this property must be explicitly
        prevented.

        If this __set__ method was not present, this descriptor would become a
        *non-data descriptor*. That would be nice because the cached value would be
        accessed directly once set (__dict__ attrs have precedence over non-data
        descriptors on instance attribute lookup). The problem is, there would be
        nothing to stop assignment to the cached value, which would overwrite the result
        of `fget()` and break both the immutability and idempotence guarantees of this
        decorator.

        The performance with this __set__() method in place was roughly 0.4 usec per
        access when measured on a 2.8GHz development machine; so quite snappy and
        probably not a rich target for optimization efforts.
        """
        ...
