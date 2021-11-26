import json
import os
from abc import ABC, abstractmethod
from pathlib import Path

base_path = Path(os.path.dirname(__file__))
with open(base_path.joinpath('config.json'), "r") as info:
    config: dict = json.load(info)


class DSAObj(ABC):
    __version: str = config["pkg_info"]["version"]
    _ds_modal = "data structure"  # retrieve the name of the class of the instance self.
    _data_type = "dsa_object"

    def __init__(self):
        DSAObj._ds_modal = type(self).__name__
        self._data = None
        self.description = config["struct_config"]["description"]

    @abstractmethod
    def __len__(self):
        pass

    def __str__(self):
        return json.dumps(self.serialize())

    def __dict__(self):
        return self.serialize()

    def display(self):
        print(json.dumps(self._data, indent=4))

    def serialize(self):
        struct = {
            "ds_modal": self._ds_modal,
            "version": self.__version,
            "description": self.description,
            self._data_type: self._data,
        }
        return struct

    @abstractmethod
    def deserialize(self, i_stream: str):
        struct: dict = json.loads(i_stream)
        modal = struct["ds_modal"]
        version = struct["version"]
        if modal != self._ds_modal:
            raise TypeError(f"Invalid data structure type: {modal} is not compatible with {self._ds_modal}")
        if version != self.__version:
            raise TypeError(f"Structure version '{modal}' is not compatible with '{self._ds_modal}'")
