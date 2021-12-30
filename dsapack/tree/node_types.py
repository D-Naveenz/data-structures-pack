import json
from typing import Optional, Any, TypeVar


class TreeNode:

    def __init__(self, key: Any, value: Optional[dict] = None):
        self.key = key
        self.value = value
        self.parent: Optional[TreeNode] = None  # Parent of this node for easier rotations
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    @property
    def is_root(self) -> bool:
        return True if self.parent is None else False

    @property
    def height(self) -> int:
        """
        Getter function to get the height of current node (this is important to update bf's after re-balancing)
        :return: Height of tree rooted at this node
        """

        def get_height(parent: Optional[TreeNode]) -> int:
            """
            Returns the height of the binary tree.
            Algorithm: max(recur left, recur right) + 1
            Explanation: The height of a binary tree that is rooted at a certain node is equal to the
            maximum of the heights of its left and right subtrees + 1 (take into account the target node)
            :param parent: parent of the subtree (current node)
            :return: the height of the tree
            """
            # BC
            if parent is None:
                return 0
            # Take the maximum of the height of the left subtree and the right subtree, and add 1 to the result
            height = max(get_height(parent.left), get_height(parent.right)) + 1
            return height

        return get_height(self)

    def __len__(self):
        return self.height

    def __repr__(self):
        struct: dict[str, Any] = {
            'key': self.key,
            'value': self.value,
            'left-child': None if not self.left else self.left.key,
            'right-child': None if not self.right else self.right.key
        }
        return json.dumps(struct)

    def get_root(self):
        def find_root(_self: TreeNode):
            return _self if _self.is_root else find_root(_self.parent)

        return find_root(self)


class AVLTreeNode(TreeNode):

    def __init__(self, key: Any, value: Optional[dict] = None, bf=0):
        super().__init__(key, value)
        self.parent: Optional[AVLTreeNode] = None  # Parent of this node for easier rotations
        self.left: Optional[AVLTreeNode] = None
        self.right: Optional[AVLTreeNode] = None
        self.bf = bf  # Balance factor of current node


TN = TypeVar('TN', TreeNode, AVLTreeNode)
