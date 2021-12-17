from typing import Optional

from . import GraphController


class UndirectedGraph(GraphController):

    def __init__(self, i_list: Optional[list[tuple[str, str] | tuple[str, str, float]]] = None):
        super().__init__(i_list)

    def add_edge(self, l_vrt, r_vrt, weight=1.0):
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
