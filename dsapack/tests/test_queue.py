from dsapack import Queue

queue: Queue = Queue[int](5, [
    67, 56, 12, 2, 99
])


def test_is_empty():
    assert queue.is_empty is False


def test_length():
    assert len(queue) == 5


def test_display():
    print("\nDisplaying the queue is json indented format")
    queue.display()
    print("\nDisplaying the directed graph is json raw format (serialize)")
    print(queue)
    assert True


def test_is_full():
    assert queue.is_full


def test_dequeue():
    assert queue.deque() == 67
    assert queue.deque() == 56
    assert queue.deque() == 12


def test_rear_pointer():
    assert queue.rear == 1


def test_deserialize():
    # creating temporary queue with deserializing the string
    tmp_queue = Queue() << str(queue)
    # compare the both dictionary outputs
    assert queue == tmp_queue
