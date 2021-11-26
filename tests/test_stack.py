from data_structures.stack import Stack

stack: Stack = Stack[int](5)


def test_is_empty():
    assert stack.is_empty


def test_push():
    stack.push(67)
    stack.push(56)
    stack.push(12)
    stack.push(2)
    stack.push(99)
    assert len(stack) == 5


def test_display():
    print("\nDisplaying the stack is json indented format")
    stack.display()
    print("\nDisplaying the directed graph is json raw format (serialize)")
    print(stack)
    assert True


def test_is_full():
    assert stack.is_full


def test_pop():
    assert stack.pop() == 99
    assert stack.pop() == 2
    assert stack.pop() == 12


def test_top():
    assert stack.top == 1


def test_deserialize():
    # serializing stack object into a string
    serial_str = str(stack)
    # creating temporary stack with deserializing the string
    tmp_stack = Stack.deserialize(serial_str)
    # compare the both dictionary outputs
    assert stack.__dict__() == tmp_stack.__dict__()
