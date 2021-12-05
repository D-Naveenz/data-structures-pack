from typing import Generic, Optional

from dsapack.core import DSAObj, generic_class, T


@generic_class
class Stack(Generic[T], DSAObj):
    _data_type = "array"
    _data: list[T]

    def __init__(self, length=1, i_str: Optional[list[T]] = None):
        super().__init__()
        self.__length = length
        self._data = []

        if i_str is not None:
            for item in i_str:
                self.push(item)

    @property
    def top(self):
        return len(self._data) - 1

    @property
    def is_empty(self):
        return self.top == -1

    @property
    def is_full(self):
        return self.top == self.__length - 1

    def __len__(self):
        return self.top + 1

    def __dict__(self):
        return self.serialize()

    @classmethod
    def deserialize(cls, i_stream: str):
        super().deserialize(i_stream)

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
