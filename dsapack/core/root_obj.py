import json
from abc import ABC, abstractmethod

from dsapack.config import __version__
__description__ = "A data structure implemented on 'data structures' python package"


class DSAObj(ABC):
    __version: str = __version__
    _ds_modal = "data structure"  # retrieve the name of the class of the instance self.
    _data_type = "dsa_object"

    def __init__(self):
        DSAObj._ds_modal = type(self).__name__
        self._data = None
        self.description = __description__

    @property
    def modal(self):
        return self._ds_modal

    @property
    def store(self):
        return self._data

    @abstractmethod
    def __len__(self):
        pass

    def __str__(self):
        return json.dumps(self.serialize())

    def __repr__(self):
        return self.serialize()

    def __eq__(self, other):
        if self.modal == other.modal and self.store == other.store:
            return True
        return False

    def display(self):
        print(json.dumps(self._data, indent=4))

    def serialize(self):
        """
        Serialize the object and returns as a dictionary
        :return: serialized object
        """
        struct = {
            "ds_modal": self._ds_modal,
            "version": self.__version,
            "description": self.description,
            self._data_type: self._data,
        }
        return struct

    @classmethod
    @abstractmethod
    def deserialize(cls, i_stream: str):
        """
        Deserialize the string and into a new object
        :param i_stream: string that contains serialized data
        :return: new instance
        """
        struct: dict = json.loads(i_stream)
        modal = struct["ds_modal"]
        version = struct["version"]
        if modal != cls._ds_modal:
            if modal[:len(cls._ds_modal)] != cls._ds_modal:
                raise TypeError(f"Invalid data structure type: {modal} is not compatible with {cls._ds_modal}")
        if version != cls.__version:
            raise TypeError(f"Structure version '{modal}' is not compatible with '{cls._ds_modal}'")
