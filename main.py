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


def question_2():
    print("### Question 2 ###")

    c_year = 2018  # current year
    _q = 0  # target year

    # get inputs
    cases = int(input())  # number of test cases
    if 1 > cases > 10:
        raise IOError("Invalid test cases input. (1 <= T <= 10)")
    for count in range(cases):
        k_list = []
        l_list = []
        y_list = []
        _q = int(input())

        _k = int(input())  # Number of malfunctioning years that will lead the machine to end up in a forward time
        if 1 > _k > 15:
            raise IOError("Invalid K input. (1 <= K <= 15)")
        for k_itm in range(_k):
            x, y = input().split()
            k_list.append((int(x), int(y)))

        _l = int(input())  # Number of malfunctioning years that will lead the machine to end up in a backward time
        if 1 > _l > 15:
            raise IOError("Invalid K input. (1 <= L <= 15)")
        for l_itm in range(_l):
            x, y = input().split()
            l_list.append((int(x), int(y)))

        # create vertices list
        tmp_year = c_year
        while tmp_year > _q:
            for _map in k_list:
                if tmp_year == _map[0]:
                    tmp_year = _map[1]
                    break
            for _map in l_list:
                if tmp_year == _map[0]:
                    tmp_year = _map[1]
                    break
            y_list.append(tmp_year)
            tmp_year -= 6
        y_list.append(_q)

        # y_list contains current year. So the result should be -1 from the length of y_list
        print(len(y_list) - 1)

    print("### Question 2 ###")
    print()


def run():
    header()
    question_1()
    question_2()


if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
