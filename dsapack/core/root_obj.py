import json
from abc import ABC, abstractmethod
from typing import Any

from dsapack.config import __version__, validate_version

__description__ = "A data structure implemented on 'data structures' python package"


class DSAObj(ABC):
    __version: str = __version__
    _ds_modal = "data structure"  # retrieve the name of the class of the instance self.
    _data_type = "dsa_object"

    # decorators
    def serializer(function):
        """
        In-class decorator that use to generate serialize function
        Serialize the object and returns as a dictionary
        :return: serialize() function
        """

        def serialize(self) -> dict[str, Any]:
            # generating header section
            struct = {
                "ds_modal": self._ds_modal,
                "version": self.__version,
                "description": self.description,
            }

            # executing function and get the output
            add: dict[str, Any] = function(self)
            # appending to the 'struct' dictionary
            for key, value in add.items():
                struct[key] = value

            return struct

        return serialize

    def deserializer(function):
        """
        In-class decorator that use to generate deserialize function
        Deserialize the string and into a new object
        :return: deserialize() function
        """
        def deserialize(cls, i_stream: str):
            # validate the jason string
            struct: dict = json.loads(i_stream)
            modal = struct["ds_modal"]
            version = struct["version"]
            if modal != cls._ds_modal:
                if modal[:len(cls._ds_modal)] != cls._ds_modal:
                    raise TypeError(f"Invalid data structure type: {modal} is not compatible with {cls._ds_modal}")
            if not validate_version(version):
                raise TypeError(f"Structure version '{cls.__version}' is not compatible with '{version}'")

            # executing function and get the output
            new = function(cls, i_stream)
            return new

        return deserialize
    # decorators

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
        return json.dumps(self._serialize_handler())

    def __repr__(self):
        return self._serialize_handler()

    def __eq__(self, other):
        if self.modal == other.modal and self.store == other.store:
            return True
        return False

    def __lshift__(self, other: str):
        new = self._deserialize_handler(other)
        return new

    def display(self):
        try:
            print(json.dumps(self._data, indent=4))
        except TypeError:
            print(json.dumps(list(self._data), indent=4))

    @abstractmethod
    def _serialize_handler(self) -> dict[str, Any]:
        """
        Serialize the object and returns as a dictionary
        :return: serialized object
        """
        struct = dict()
        return struct

    @classmethod
    @abstractmethod
    def _deserialize_handler(cls, i_stream: str):
        """
        Deserialize the string and into a new object
        :param i_stream: string that contains serialized data
        :return: new instance
        """
        pass
