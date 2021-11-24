import unittest
from data_structures.graph import DirectedGraph, Edge


class CommonGraphTestCase(unittest.TestCase):
    graph = DirectedGraph([
        Edge("V1", "V2"),
        Edge("V3", "V2"), Edge("V3", "V4"),
        Edge("V4", "V2"), Edge("V4", "V5"),
        Edge("V5", "V2"), Edge("V5", "V1")
    ])

    def test_print_outputs(self):
        print("\nDisplaying the directed graph is json indented format")
        self.graph.display()
        print("\nDisplaying the directed graph is json raw format (serialize)")
        print(self.graph)

    def test_edge_count(self):
        # there are 7 edges in the graph. testing it
        count = int(self.graph)
        self.assertEqual(count, 7)

    def test_deserialization(self):
        # serializing graph object into a string
        serial_str = str(self.graph)
        # creating temporary graph with deserializing the string
        tmp_graph = DirectedGraph(serial_str)
        # compare the both dictionary outputs
        self.assertEqual(self.graph.__dict__(), tmp_graph.__dict__())

    def test_path_count_accuracy(self):
        # there is only one path from V3 to V1
        paths = self.graph.trace_paths("V3", "V1")
        count = len(paths)

        print('\nThere', end=' ')
        if count == 0:
            print("is not any path between V3 and v1")
        elif count == 1:
            print("is one path between V3 and v1")
            print(paths)
        else:
            print(f"are {count} paths between V3 and v1")
            print(paths)

        self.assertEqual(count, 1)

    def test_cycle_count_accuracy(self):
        # there is not any cycle from V1
        # print("There is " + ("" if graph.trace_cycles("V1") else "not") + "a cycle from V1")
        cycles = self.graph.trace_cycles("V1")
        count = len(cycles)

        print('\nThere', end=' ')
        if count == 0:
            print("is not any cycle from v1")
        elif count == 1:
            print("is one cycle from v1")
            print(cycles)
        else:
            print(f"are {count} cycles from v1")
            print(cycles)

        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()
