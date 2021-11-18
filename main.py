from helpers import console
from structures import DirectedGraph, Edge

TERMINAL_WIDTH = console.get_terminal_width()


def header():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(TERMINAL_WIDTH))
    print("Directed Graph".center(TERMINAL_WIDTH))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~".center(TERMINAL_WIDTH))
    print("\n")


def run():
    header()


if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
