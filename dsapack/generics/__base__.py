import re
from abc import ABC
from typing import get_args, Optional, Generic, TypeVar

from ..__base__ import DSObject

# Type variable that generic type data structures can use
T = TypeVar("T")


class DSGeneric(DSObject, Generic[T], ABC):
    """
    This metaclass can use to get the generic type after initialization. Class instances of generic classes have a
    __orig_class__ attribute available after initialization. This attribute is set after init (see source code).
    Hence, the 'DS generic' class will modify the source class to basically listen to when the __orig_class__
    attribute is set by the runtime. This heavily relies on an undocumented implementation detail though and will
    probably not work the same way in future versions or other implementations of Python.
    """
    __generic_type__: Optional[type] = None

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == "__orig_class__":
            self.__generic_type__ = get_args(self.__orig_class__)[0]
            self._ds_modal += '[' + get_args(self.__orig_class__)[0].__name__ + ']'

    @classmethod
    def create_class(cls, ds_modal, *args, **kwargs):
        gen_type = re.findall(r'(?<=\[)[a-zA-Z]+', ds_modal)
        gen_type = cls.get_type(gen_type[0])

        new = cls[gen_type](*args, **kwargs)
        return new

    @staticmethod
    def get_type(name: str) -> type:
        """
        Lexical cast from a string to a type.
        It's working for all built-in types.
        :param name: type name
        :return: type
        """
        from collections import deque
        # q is short for "queue", here
        q = deque([object])
        while q:
            t = q.popleft()
            if t.__name__ == name:
                return t

            try:
                # Keep looking!
                q.extend(t.__subclasses__())
            except TypeError:
                # type.__subclasses__ needs an argument, for whatever reason.
                if t is type:
                    continue
                else:
                    raise
        else:
            raise ValueError('No such type: %r' % name)
