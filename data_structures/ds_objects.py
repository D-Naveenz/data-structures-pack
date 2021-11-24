from abc import ABC, abstractmethod
import json

STRUCTURE_VERSION = 1.0


class DSAObj(ABC):
    def __init__(self):
        self.__ds_modal = self.__class__.__name__  # retrieve the name of the class of the instance self.
        self.__version = STRUCTURE_VERSION
        self._data_type = None
        self._data = None

    @abstractmethod
    def __int__(self):
        pass

    def __str__(self):
        return json.dumps(self.serialize())

    def __dict__(self):
        return self.serialize()

    @property
    def type(self):
        return self.__ds_modal

    def display(self):
        print(json.dumps(self._data, indent=4))

    def serialize(self):
        struct = {
            "ds_modal": self.__ds_modal,
            "version": self.__version,
            self._data_type: self._data,
        }
        return struct

    @abstractmethod
    def deserialize(self, i_stream: str):
        struct: dict = json.loads(i_stream)
        modal = struct["ds_modal"]
        version = struct["version"]
        if modal != self.__ds_modal:
            raise TypeError(f"Invalid data structure type: {modal} is not compatible with {self.__ds_modal}")
        if version != self.__version:
            raise TypeError(f"Structure version '{modal}' is not compatible with '{self.__ds_modal}'")
