from dsapack.graph import DirectedGraph, Edge

graph = DirectedGraph([
    Edge("V1", "V2"),
    Edge("V3", "V2"), Edge("V3", "V4"),
    Edge("V4", "V2"), Edge("V4", "V5"),
    Edge("V5", "V2"), Edge("V5", "V1")
])


def test_display():
    print("\nDisplaying the directed graph is json indented format")
    graph.display()
    print("\nDisplaying the directed graph is json raw format (serialize)")
    print(graph)
    assert True


def test_edge_count():
    assert len(graph) == 7


def test_deserialize():
    # serializing graph object into a string
    serial_str = str(graph)
    # creating temporary graph with deserializing the string
    tmp_graph = DirectedGraph.deserialize(serial_str)
    # compare the both dictionary outputs
    assert graph.__dict__() == tmp_graph.__dict__()


def test_trace_paths():
    paths = graph.trace_paths("V3", "V1")
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

    assert count == 1


def test_trace_cycles():
    # print("There is " + ("" if graph.trace_cycles("V1") else "not") + "a cycle from V1")
    cycles = graph.trace_cycles("V1")
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

    assert count == 0
