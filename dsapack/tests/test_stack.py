from dsapack import Stack

stack: Stack = Stack[int](5, [
    67, 56, 12, 2, 99
])


def test_is_empty():
    assert stack.is_empty is False


def test_length():
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
    # creating temporary stack with deserializing the string
    tmp_stack = Stack() << str(stack)
    # compare the both dictionary outputs
    assert stack == tmp_stack
