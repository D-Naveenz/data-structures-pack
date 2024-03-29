from dsapack import DirectedGraph

graph = DirectedGraph([
    ("V1", "V2"),
    ("V3", "V2"), ("V3", "V4"),
    ("V4", "V2"), ("V4", "V5"),
    ("V5", "V2"), ("V5", "V1")
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
    # creating temporary graph with deserializing the string
    tmp_graph = DirectedGraph() << str(graph)
    # compare the both dictionary outputs
    assert graph == tmp_graph


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
