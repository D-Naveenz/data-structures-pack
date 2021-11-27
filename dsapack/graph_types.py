from typing import Optional

from .graph import GraphController, Edge


class DirectedGraph(GraphController):

    def __init__(self, i_str: Optional[list[Edge]] = None):
        super().__init__(i_str)

    def is_universal_sink(self, vertex):
        # checking there are adjacent vertices from the given vertex
        if len(self._data.get(vertex)) == 0:
            count = 0
            for adj_list in self.adjacency_list.values():
                for adj in adj_list:
                    if adj.get("adjacent") is vertex:
                        count += 1
                        break
            if count == self.vertex_count - 1:
                return True
        return False


class UndirectedGraph(GraphController):

    def __init__(self, i_str: Optional[list[Edge]] = None):
        super().__init__(i_str)

    def add_edge(self, l_vrt, r_vrt, weight):
        # Call base function
        super().add_edge(l_vrt, r_vrt, weight)
        # Both verticals should behave adjacent to each other
        self._data[r_vrt].append({"adjacent": l_vrt, "weight": weight})

    def remove_edge(self, l_vrt, r_vrt):
        # Call base function
        super().remove_edge(l_vrt, r_vrt)
        # Both verticals should be removed
        for edge in self._data[r_vrt]:
            if edge["adjacent"] == l_vrt:
                self._data[r_vrt].remove(edge)
