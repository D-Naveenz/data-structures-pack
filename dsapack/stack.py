from typing import Generic, Optional, Any

from dsapack.core import *


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

    @DSAObj.serializer
    def _serialize_handler(self) -> dict[str, Any]:
        struct = {
            "length": self.__length
        }
        return struct

    @classmethod
    @DSAObj.deserializer
    def _deserialize_handler(cls, i_stream: str):
        struct: dict = json.loads(i_stream)

        new = cls.create_class(struct["ds_modal"], struct["length"], list(struct["array"]))
        return new
