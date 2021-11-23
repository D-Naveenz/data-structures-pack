# Gthub: https://github.com/D-Naveenz/data-structures-pack

from helpers import console
from structures import DirectedGraph, Edge

TERMINAL_WIDTH = console.get_terminal_width()


def header():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(TERMINAL_WIDTH))
    print("DSA Practicals - Lab Sheet 03".center(TERMINAL_WIDTH))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~".center(TERMINAL_WIDTH))
    print()


def question_1():
    print("### Question 1 ###")

    graph = DirectedGraph([
        Edge("V1", "V2"), Edge("V1", "V3"), Edge("V1", "V6"),
        Edge("V2", "V3"), Edge("V2", "V4"),
        Edge("V4", "V3"),
        Edge("V5", "V3"),
        Edge("V6", "V3"), Edge("V2", "V8"),
        Edge("V7", "V1"), Edge("V7", "V3"),
        Edge("V8", "V3"), Edge("V8", "V7")
    ])

    # Display the graph structure
    graph.display()

    # calculating how many universal sinks in this graph
    count = 0
    for vertex in graph.adjacency_list.keys():
        if graph.is_universal_sink(vertex):
            count += 1

    print('\nThere', end=' ')
    if count == 0:
        print("is not any universal sink in this graph")
    elif count == 1:
        print("is one universal sink in this graph")
    else:
        print(f"are {count} universal sinks in this graph")

    print("### Question 1 ###\n")
    print()


def run():
    header()
    question_1()


if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
