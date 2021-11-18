import json
from abc import abstractmethod
from structures.ds_objects import DSAObj


class Edge:
    def __init__(self, vert1: str, vert2: str, wgt: float = None):
        self.l_vertex = vert1
        self.r_vertex = vert2
        if wgt is None:
            self.weight = 1.0
        else:
            self.weight = wgt


class GraphController(DSAObj):
    _data: dict[str, list[dict]]

    def __init__(self, i_str: list[Edge] | str = None):
        super().__init__()
        self._edges_count = 0
        self._data_type = "adjacency_list"
        self._data = {}

        if i_str is not None:
            if isinstance(i_str, str):
                self.deserialize(i_str)
            else:
                for item in i_str:
                    self.add_edge(item.l_vertex, item.r_vertex, item.weight)

    def __int__(self):
        return self._edges_count

    @property
    def vertices_count(self):
        return len(self._data)

    # Public functions
    def deserialize(self, i_stream: str):
        super().deserialize(i_stream)
        struct: dict = json.loads(i_stream)
        self._data = struct[self._data_type]

    def add_vertex(self, name):
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
        self._edges_count += 1

    @abstractmethod
    def remove_edge(self, l_vrt, r_vrt):
        pass

    def trace_paths(self, start: str, end: str):
        if start != end:
            return self.__pathfinder(start, end)
        return 0

    def trace_cycles(self, vertex: str):
        return self.__pathfinder(vertex, vertex)

    # Public functions

    # Private functions
    def __pathfinder(self, start: str, end: str, **kwargs):
        # temporary variable to store processed vertexes
        if kwargs.get("processed") is None:
            kwargs["processed"] = []

        # base case 1
        # If start or end vertex doesn't exists then return false
        if self._data.get(start) is None and self._data.get(end) is None:
            return 0

        if kwargs.get("it") is None:
            kwargs["it"] = 0
        else:
            kwargs["it"] += 1

        # base case 2
        # If its not the first iteration and both start and end vertices are the same
        if start == end and kwargs["it"] > 0:
            return 1
        else:
            # base case 3
            # If the current (start) node already belongs to the path as a milestone
            if start in kwargs["processed"]:
                return 0

        # recursive steps
        kwargs["processed"].append(start)
        count = 0
        for edges in self._data.values():
            for edge in edges:
                count += self.__pathfinder(edge["adjacent"], end, **kwargs)

        return count
    # Private functions


class DirectedGraph(GraphController):

    def __init__(self, i_str: list[Edge] | str = None):
        super().__init__(i_str)

    def remove_edge(self, l_vrt, r_vrt):
        for edge in self._data[l_vrt]:
            if edge["adjacent"] == r_vrt:
                self._data[l_vrt].remove(edge)
                self._edges_count -= 1


class UndirectedGraph(GraphController):

    def __init__(self, i_str: list[Edge] | str = None):
        super().__init__(i_str)

    def add_edge(self, l_vrt, r_vrt, weight=1.0):
        # Call base function
        super().add_edge(l_vrt, r_vrt, weight)
        # Both verticals should behave adjacent to each other
        self._data[r_vrt].append({"adjacent": l_vrt, "weight": weight})

    def remove_edge(self, l_vrt, r_vrt):
        for edge in self._data[l_vrt]:
            if edge["adjacent"] == r_vrt:
                self._data[l_vrt].remove(edge)

        for edge in self._data[r_vrt]:
            if edge["adjacent"] == l_vrt:
                self._data[r_vrt].remove(edge)
                self._edges_count -= 1
