import json
from typing import Optional

from ..__base__ import DSObject


class GraphController(DSObject):
    _data: dict[str, list[dict]]
    _data_type = "adjacency_list"

    def __init__(self, i_list: Optional[list[tuple[str, str] | tuple[str, str, float]]] = None):
        super().__init__()
        self.__edge_count = 0
        self._data = {}

        if i_list is not None:
            for item in i_list:
                self.add_edge(*item)

    @property
    def edge_count(self):
        return self.__edge_count

    @property
    def vertex_count(self):
        return len(self._data)

    def __len__(self):
        return self.edge_count

    # Public functions
    def add_vertex(self, name):
        if name not in self._data:
            self._data[name] = []

    def remove_vertex(self, name):
        if self._data.get(name) is not None:
            # clear the list
            self._data[name].clear()
            # unbind target vertex from edges
            for edges in self._data.values():
                for edge in edges:
                    if edge["adjacent"] == name:
                        edges.remove(edge)
            # remove vertex at last
            self._data.pop(name)
        else:
            raise IndexError("Couldn't find the vertex named " + name + ".")

    def add_edge(self, l_vrt, r_vrt, weight=1.0):
        # create new vertices if not exist them
        if self._data.get(l_vrt) is None:
            self.add_vertex(l_vrt)
        if self._data.get(r_vrt) is None:
            self.add_vertex(r_vrt)

        # append the edge to the relevant place
        self._data[l_vrt].append({"adjacent": r_vrt, "weight": weight})
        self.__edge_count += 1

    def remove_edge(self, l_vrt, r_vrt):
        for edge in self._data[l_vrt]:
            if edge["adjacent"] == r_vrt:
                self._data[l_vrt].remove(edge)
                self.__edge_count -= 1

    def trace_paths(self, start, end):
        # If start or end vertex doesn't exist
        if self._data.get(start) is None and self._data.get(end) is None and start == end:
            raise IOError("Invalid input")

        return self.__trace_util(start, end, True)

    def trace_cycles(self, vertex):
        # If the vertex doesn't exist
        if self._data.get(vertex) is None:
            raise IOError("Invalid input")

        return self.__trace_util(vertex, vertex, True)

    def trace_trails(self, start, end):
        # If start or end vertex doesn't exist
        if self._data.get(start) is None and self._data.get(end) is None and start == end:
            raise IOError("Invalid input")

        return self.__trace_util(start, end, False)

    def trace_circuit(self, vertex):
        # If the vertex doesn't exist
        if self._data.get(vertex) is None:
            raise IOError("Invalid input")

        return self.__trace_util(vertex, vertex, False)

    # Public functions

    # Protected functions
    @DSObject.serializer
    def _serialize_handler(self):
        struct = {
            "edge_count": self.__edge_count,
            self._data_type: self._data
        }
        return struct

    @classmethod
    @DSObject.deserializer
    def _deserialize_handler(cls, i_stream: str):
        struct: dict = json.loads(i_stream)

        new = cls()
        new.__edge_count = struct["edge_count"]
        new._data = struct[cls._data_type]
        return new

    # Protected functions

    # Private functions
    def __trace_util(self, start, end, is_path) -> Optional[list[list]]:
        # Mark all the vertices as not visited
        visited = {}
        for vertex in self._data.keys():
            visited[vertex] = False

        # Create an array to store paths
        paths: list[list] = []

        if is_path:
            self.__path_finder(
                start,
                end,
                visited=visited,
                current=[],
                paths=paths,
                recursion=-1,
            )
        else:
            self.__trail_finder(
                start,
                end,
                visited=visited,
                current=[],
                paths=paths,
                recursion=-1,
                streak=0
            )

        if paths is [[]]:
            return None
        else:
            return paths

    def __path_finder(self, start, end, **kwargs):
        # Mark the current node as visited and store in path
        kwargs["visited"][start] = True
        kwargs["current"].append(start)
        kwargs["recursion"] += 1

        # base case 1
        # If it's not the first iteration and both start and end vertices are the same
        if start == end and kwargs["recursion"] > 0:
            kwargs["paths"].append(list(kwargs["current"]))
        else:
            # recursive steps
            for edge in self._data.get(start):
                # If the current (start) vertex already belongs to the path as a milestone
                if kwargs["visited"][edge["adjacent"]] is False:
                    self.__path_finder(edge["adjacent"], end, **kwargs)

        # Remove current vertex from path[] and mark it as unvisited
        kwargs["current"].pop()
        kwargs["visited"][start] = False

    def __trail_finder(self, start, end, **kwargs):
        # Mark the current node as visited and store in path
        kwargs["visited"][start] = True
        kwargs["current"].append(start)
        kwargs["recursion"] += 1

        # base case 1
        # If it's not the first iteration and both start and end vertices are the same
        if start == end and kwargs["recursion"] > 0:
            kwargs["paths"].append(list(kwargs["current"]))
        else:
            # recursive steps
            for edge in self._data.get(start):
                # If the current (start) vertex already belongs to the path as a milestone
                if kwargs["visited"][edge["adjacent"]] is True:
                    kwargs["streak"] += 1
                else:
                    kwargs["streak"] = 0
                # If not crossing an edge
                if kwargs["streak"] <= 1:
                    self.__path_finder(edge["adjacent"], end, **kwargs)

        # Remove current vertex from path[] and mark it as unvisited
        kwargs["current"].pop()
        kwargs["visited"][start] = False
    # Private functions
