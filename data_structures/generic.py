from typing import get_args, TypeVar

T = TypeVar("T")


def generic_class(cls):
    """
    This decorator can use to get the generic type after initialization. Class instances of generic classes have a
    __orig_class__ attribute available after initialization. This attribute is set after init (see source code).
    Hence, the decorator will modify the source class to basically listen to when the __orig_class__ attribute is set
    by the runtime. This heavily relies on an undocumented implementation detail though and will probably not work
    the same way in future versions or other implementations of Python.

    :param cls: Class Type
    :return: Generic class
    """
    orig_bases = cls.__orig_bases__
    generic_type = orig_bases[0]

    class GenericClass(cls, generic_type):
        __generic_type__ = type
        _ds_modal = cls.__name__

        def __init__(self, *args, **kwargs):
            super().__init__(*args, *kwargs)

        def __setattr__(self, name, value):
            object.__setattr__(self, name, value)
            if name == "__orig_class__":
                self.__generic_type__ = get_args(self.__orig_class__)[0]
                self._ds_modal += '[' + get_args(self.__orig_class__)[0].__name__ + ']'

    GenericClass.__orig_bases__ = orig_bases
    return GenericClass
