from queue import Queue


def validate_bst(root) -> bool:
    """
    CONTINUOUS TRACKING OF MIN/MAX INTERVAL:
    :param root: root of tree
    :Time: O(N)
    :Space: O(N)
    :return: whether it is a BST
    """

    def validate(_root, curr_min, curr_max):
        """
        Returns whether the tree at root is a valid BST bounded by lower and upper intervals, curr_min & curr_max.
        Algorithm: Instead of comparing root with children values, compare with L-R intervals.
                - If current root is within the interval check left and right
                    - recur on left while updating upper interval to current root's key (ensure nothing bigger than it)
                    - recur on right while updating lower interval to current root's key (ensure everything bigger than it)
                    - if both the left and right subtrees are valid, then entire tree is valid
                - else, not valid
        :param _root: root of tree
        :param curr_min:
        :param curr_max:
        :return: whether tree is a BST.
        """
        if not _root:  # BC: empty tree is valid
            return True
        if curr_min < _root.key < curr_max:  # recur left and right and update intervals accordingly
            return validate(_root.left, curr_min, _root.key) and validate(_root.right, _root.key, curr_max)
        else:
            return False  # not valid

    return validate(root, float('-inf'), float('+inf'))


def print_pre_order(root):
    """
    Prints a pre-order traversal of a binary tree: Root, Left, Right
    :param root: target of tree
    :return: none
    :Time: O(N)
    :Space: O(N) stack space due to recursion
    """
    if root is None:
        return

    print(root.key, end=" ")
    print_pre_order(root.left)
    print_pre_order(root.right)


def print_post_order(root):
    """
    Prints a post-order traversal of a binary tree: Left, Right, Root
    :param root: target of tree
    :return: none
    :Time: O(N)
    :Space: O(N) stack space due to recursion
    """
    if root is None:
        return

    print_post_order(root.left)
    print_post_order(root.right)
    print(root.key, end=" ")


def print_in_order(root):
    """
    Prints a in-order traversal of a binary tree: Left, Root, Right
    :param root: target of tree
    :return: none
    :Time: O(N)
    :Space: O(N) stack space due to recursion
    """
    if root is None:
        return

    print_in_order(root.left)
    print(root.key, end=" ")
    print_in_order(root.right)


def print_level_order(root):
    """
    Prints a level-order traversal of a binary tree, using BFS Algorithm.
    :param root: target of tree
    :return: none
    :Time: O(N)
    :Space: O(N)
    """
    # Initialize a marked[] array and mark source as visited -> not relevant
    # Create a queue and enqueue source node
    bfs_queue = Queue()
    bfs_queue.put(root)

    while not bfs_queue.empty():
        # Deque from the queue and print
        removed = bfs_queue.get()
        print(removed.key, end=" ")

        # Get all neighbors/adjacent nodes/vertices of the dequeued vertex and enqueue if not visited and mark it

        # In standard BFS, we push vertices adjacent to a node, which all exist in the adjacency list representation
        # Here, children may be non-existent so we must push only those children that exist
        if removed.left is not None:
            bfs_queue.put(removed.left)
        if removed.right is not None:
            bfs_queue.put(removed.right)
