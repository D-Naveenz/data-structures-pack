import json
from collections import deque
from typing import Any, Generic, Optional

from . import DSGeneric, T
from ..__base__ import DSObject


class Queue(DSGeneric[T], Generic[T]):
    _data_type = "list"
    _data: deque[T]

    def __init__(self, length=1, i_list: Optional[list[T]] = None):
        super().__init__()
        self.__length = length
        self._data = deque(maxlen=length)

        if i_list is not None:
            for item in i_list:
                self.enqueue(item)

    @property
    def rear(self):
        return len(self._data) - 1

    @property
    def is_empty(self):
        return len(self._data) == 0

    @property
    def is_full(self):
        return len(self._data) == self.__length

    def __len__(self):
        return self.__length

    def enqueue(self, data: T):
        try:
            self._data.append(data)
        except IndexError:
            print("Error - Queue is overflowing")

    def deque(self):
        try:
            return self._data.popleft()
        except IndexError:
            print("Error - Queue is empty!")

    @DSObject.serializer
    def _serialize_handler(self) -> dict[str, Any]:
        struct = {
            "length": self.__length,
            self._data_type: list(self._data)
        }
        return struct

    @classmethod
    @DSObject.deserializer
    def _deserialize_handler(cls, i_stream: str):
        struct: dict = json.loads(i_stream)

        new = cls.create_class(struct["ds_modal"], struct["length"], list(struct["list"]))
        return new
