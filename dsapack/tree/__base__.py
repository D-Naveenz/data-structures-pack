from queue import Queue
from typing import Any, Optional, Generic

from dsapack.generics import DSGeneric
from dsapack.tree import TN, TreeNode


def get_min_node(root: TN) -> Optional[TN]:
    """
    This returns the minimum key's node in the BST
    Algorithm: If target is none, no solution. Else, traverse the left subtree like a linked list
    and return the left-most node
    :Time: O(N)
    :Space: O(1)
    :return: the minimum key node in the tree
    """
    if root is None:  # BC1
        return None

    current = root
    while current.left is not None:  # Traverse like a linked-list
        current = current.left

    return current


class DSTree(DSGeneric[TN], Generic[TN]):
    _data: list[TN]
    _data_type = "nodes"
    root: Optional[TN]

    def __init__(self, *nodes):
        super().__init__()
        self.root = None
        self._data = []

        if len(nodes) > 0:
            for i in nodes:
                if isinstance(i, tuple):
                    self.insert(i[0], i[1])
                else:
                    self.insert(i, None)

    def __len__(self):
        return len(self._data)

    @property
    def height(self) -> int:
        """
        Returns the height of the binary tree.
        :return: the height of the tree
        """

        return 0 if self.root is None else self.root.height

    def get(self, key: Any) -> TN:
        """
        Get method that to get the node associated with key.
        Raise an error if node does not exist
        :param key: key to look for
        :return: TN if found
        """

        def get_helper(target: Optional[TN] = None) -> Optional[TN]:
            """
            Helper get method that to get the node associated with key
            :param target: parent node of the current processing node
            :Time: O(log(N))
            :Space: O(log(N))
            :return: None if not found, the node, otherwise
            """
            # Always do the edge-case check, which could raise an error, FIRST!!
            if target is None:
                return None

            # BST-order traverse: examine target first, then recur left or recur right depending on key comparison
            if key == target.key:  # BC1 - found
                return target

            # If the current node is less than the key we find, we have to search the child node on the left
            elif key < target.key:
                return get_helper(target.left)

            # If the current node is greater than the key we find, we have to search the child node on the right
            else:
                return get_helper(target.right)

        result = get_helper(self.root)
        if result is None:
            raise LookupError("Error! Key doesn't exist!")
        else:
            return result

    def contains(self, key) -> bool:
        """
        Returns whether the tree contains a given key, this time using level-order traversal (standard BFS)
        :param key: key to be checked
        :Time: O(log(n))
        :return: whether the tree contains the key
        """
        # BFS (level-order traversal) algorithm
        bfs_queue: Queue = Queue()
        bfs_queue.put(self.root)  # Enqueue source node and mark as visited

        while not bfs_queue.empty():
            removed = bfs_queue.get()  # Dequeue from front
            if removed.key == key:  # If the removed node matches, return
                return True
            # Add the removed vertex's adjacent unmarked nodes into the queue and mark them
            # But as in the standard BFS, we only add the adjacent vertices that exist (i.e. not None)
            # NOTE: THIS TIME WE ONLY ENQUEUE ONE CHILD BASED ON THE BST KEY COMPARISON!!!

            if key < removed.key and removed.left is not None:
                bfs_queue.put(removed.left)  # mark visited
            if key > removed.key and removed.right is not None:
                bfs_queue.put(removed.right)  # mark visited
        return False

    def insert(self, key, value=None):
        def insert_helper(parent: TN, target: TN):
            """
            Recursively inserts the passed in node into the BST.
            Clever Algorithm: First ascertain direction (l or r) to recur.
                Before recurring, check if we can insert directly in the ascertained direction by checking the child
                If a child in that direction does not exist, simply assign it there
                Else, recur in that direction
            :param parent: target of bst
            :param target: node to insert
            :Time: O(log(n))
            :Space: O(log(n)) stack space
            :return: none
            """
            if parent is None:
                # Could simply return/"rebound" the target parameter up the stack and assign where needed, or return
                return

            if target.key < parent.key:  # First check to determine direction: left
                if parent.left is None:  # Second check to check if a left child doesn't exist
                    parent.left = target  # If it doesn't simply assign
                else:
                    insert_helper(parent.left, target)  # Else, simply recur left

            elif target.key > parent.key:  # Similar for the right subtree
                if parent.right is None:
                    parent.right = target
                else:
                    insert_helper(parent.right, target)

        node = self.__generic_type__(key, value)
        self._data.append(node)  # push the node to _data list
        if self.root is None:
            self.root = node
        else:
            insert_helper(self.root, node)

    def delete(self, key) -> Optional[TN]:
        """
        Deletes a node associated with key, key, in the tree and returns the target of the resulting
        tree, which may be updated.
        :param key:  key to be deleted
        :return: the resulting target of the tree
        """

        def delete_helper(parent: Optional[TN], _key) -> Optional[TN]:
            """
            Deletes a node associated with key, key, in the tree and returns the target of the resulting
            tree, which may be updated.
            :param parent: key to be deleted
            :param _key: key to be deleted
            :Time: O(log(n)) average
            :Space: O(log(n) average
            :return: the resulting target of the tree
            """
            if parent is None:
                return None
            if key < parent.key:
                new_root_left = delete_helper(parent.left, _key)  # get new target of left subtree
                parent.left = new_root_left  # assign target.left to the new target of the left subtree
            elif key > parent.key:
                new_root_right = delete_helper(parent.right, _key)
                parent.right = new_root_right
            else:  # found match, handle 3 cases
                # case 1 - match is a leaf node (return None back up the stack)
                if parent.left is None and parent.right is None:
                    return None  # target of new subtree is None
                # case 2 - match has one child (return the other back up the stack)
                elif parent.left is None:
                    # return the right subtree back up the stack to indicate that it's the new target
                    return parent.right
                elif parent.right is None:  # vice-versa
                    return parent.left
                # case 3 - replace match with inorder successor; delete the successor; return up the stack
                else:
                    inorder_successor = get_min_node(parent.right)
                    # copy  successor into current
                    parent.key, parent._value = inorder_successor.key, inorder_successor._value
                    # delete inorder successor
                    new_root_successor = delete_helper(parent.right, inorder_successor.key)
                    parent.right = new_root_successor
                    return parent

            return parent  # return target of resulting tree as required

        return delete_helper(self.root, key)

    def _serialize_handler(self) -> dict[str, Any]:
        pass

    @classmethod
    def _deserialize_handler(cls, i_stream: str):
        pass
