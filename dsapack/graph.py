import json
from typing import Any, Optional

from .core import DSAObj


class Edge:
    def __init__(self, vert1, vert2, wgt: float = None):
        self.l_vertex = vert1
        self.r_vertex = vert2
        if wgt is None:
            self.weight = 1.0
        else:
            self.weight = wgt


class GraphController(DSAObj):
    _data_type = "adjacency_list"
    _data: dict[Any, list[dict]]

    def __init__(self, i_str: Optional[list[Edge]] = None):
        super().__init__()
        self.__edge_count = 0
        self._data = {}

        if i_str is not None:
            for item in i_str:
                self.add_edge(item.l_vertex, item.r_vertex, item.weight)

    @property
    def edge_count(self):
        return self.__edge_count

    @property
    def vertex_count(self):
        return len(self._data)

    @property
    def adjacency_list(self):
        return self._data

    def __len__(self):
        return self.edge_count

    # Public functions
    @classmethod
    def deserialize(cls, i_stream: str):
        super().deserialize(i_stream)
        struct: dict = json.loads(i_stream)

        new = cls()
        new._data = struct[cls._data_type]
        return new

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

    def add_edge(self, l_vrt, r_vrt, weight):
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
        # If start or end vertex doesn't exists
        if self._data.get(start) is None and self._data.get(end) is None and start == end:
            raise IOError("Invalid input")

        return self.__trace_util(start, end, True)

    def trace_cycles(self, vertex):
        # If the vertex doesn't exists
        if self._data.get(vertex) is None:
            raise IOError("Invalid input")

        return self.__trace_util(vertex, vertex, True)

    def trace_trails(self, start, end):
        # If start or end vertex doesn't exists
        if self._data.get(start) is None and self._data.get(end) is None and start == end:
            raise IOError("Invalid input")

        return self.__trace_util(start, end, False)

    def trace_circuit(self, vertex):
        # If the vertex doesn't exists
        if self._data.get(vertex) is None:
            raise IOError("Invalid input")

        return self.__trace_util(vertex, vertex, False)

    # Public functions

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
        # If its not the first iteration and both start and end vertices are the same
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
        # If its not the first iteration and both start and end vertices are the same
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
