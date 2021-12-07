from typing import Optional

from .graph import GraphController


class DirectedGraph(GraphController):

    def __init__(self, i_list: Optional[list[tuple[str, str] | tuple[str, str, float]]] = None):
        super().__init__(i_list)

    def is_universal_sink(self, vertex):
        # checking there are adjacent vertices from the given vertex
        if len(self._data.get(vertex)) == 0:
            count = 0
            for adj_list in self.store.values():
                for adj in adj_list:
                    if adj.get("adjacent") is vertex:
                        count += 1
                        break
            if count == self.vertex_count - 1:
                return True
        return False
