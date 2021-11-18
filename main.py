from typing import Dict, List

from structures import DirectedGraph, Edge


def directed_graph_test():
    # here 240 spaces are reserved for the particular output string. And the string is printed in the middle
    print(f"{'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Directed Graph ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' : ^120}")
    print("\n")

    graph = DirectedGraph([
        Edge("V1", "V2"),
        Edge("V3", "V2"), Edge("V3", "V4"),
        Edge("V4", "V2"), Edge("V4", "V5"),
        Edge("V5", "V2"), Edge("V5", "V1")
    ])

    # testing outputs
    print(f"There are {int(graph)} edges in the graph")
    print("Displaying the directed graph is json indented format")
    graph.display()
    print("\nDisplaying the directed graph is json raw format (serialize)")
    print(graph)

    # checking serialization / deserialization
    print("\nCreated a new temporary object with deserializing current object")
    tmp_obj = DirectedGraph(str(graph))
    print(tmp_obj)

    # checking path finder algorithms
    # Returns number of paths between first given vertex and the second given vertex
    path_count = graph.trace_paths("V3", "V1")
    print('\nThere', end=' ')
    if path_count == 0:
        print("is not any path between V3 and v1")
    elif path_count == 1:
        print("is one path between V3 and v1")
    else:
        print(f"are {path_count} paths between V3 and v1")
    # Check whether a given directed graph contains a cycle or not
    print("There is " + ("" if graph.trace_cycles("V1") else "not") + "a cycle from V1")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directed_graph_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
