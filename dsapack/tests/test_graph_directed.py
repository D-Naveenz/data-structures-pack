from dsapack import DirectedGraph

graph = DirectedGraph([
    ("V1", "V2"), ("V1", "V3"), ("V1", "V6"),
    ("V2", "V3"), ("V2", "V4"),
    ("V4", "V3"),
    ("V5", "V3"),
    ("V6", "V3"), ("V2", "V8"),
    ("V7", "V1"), ("V7", "V3"),
    ("V8", "V3"), ("V8", "V7")
])


def test_display():
    print("\nDisplaying the directed graph is json indented format")
    graph.display()
    print("\nDisplaying the directed graph is json raw format (serialize)")
    print(graph)
    assert True


def test_is_universal_sink():
    # calculating how many universal sinks in this graph
    count = 0
    for vertex in graph.store.keys():
        if graph.is_universal_sink(vertex):
            count += 1

    print('\nThere', end=' ')
    if count == 0:
        print("is not any universal sink in this graph")
    elif count == 1:
        print("is one universal sink in this graph")
    else:
        print(f"are {count} universal sinks in this graph")

    assert count == 1
