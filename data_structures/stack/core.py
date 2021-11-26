from typing import Generic

from data_structures import DSAObj
from data_structures.generic import generic_class, T


@generic_class
class Stack(Generic[T], DSAObj):
    _data_type = "array"
    _data: list[T]

    def __init__(self, length=1):
        super().__init__()
        self.__length = length
        self._data = []

    @property
    def __top(self):
        return len(self._data) - 1

    @property
    def is_empty(self):
        return self.__top == -1

    @property
    def is_full(self):
        return self.__top == self.__length - 1

    def __len__(self):
        return self.__top + 1

    def generic_type(self):
        return "[" + self.__orig_class__.__args__[0].__name__ + "]"

    def deserialize(self, i_stream: str):
        pass

    def push(self, data: T):
        if not self.is_full:
            self._data.append(data)
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty:
            return self._data.pop()
        else:
            return None
