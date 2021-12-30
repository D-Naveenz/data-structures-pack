from typing import Optional

from . import DSTree, AVLTreeNode


class AVLTree(DSTree[AVLTreeNode]):
    root: Optional[AVLTreeNode]

    def __init__(self, *nodes):
        super().__init__(*nodes)

    def insert(self, key, value=None):
        """
        Public insert function to insert a node into an AVL Tree.
        :param key: key of node to be inserted
        :param value: corresponding value
        :Time: O(log(n))
        :Space: O(log(n))
        :return: none
        """

        new_node = AVLTreeNode(key, value)
        self._data.append(new_node)
        # Returns target of resulting tree after insertion - update it
        self.root = self.__insert(key, self.root, new_node)

    def __insert(self, key, parent: Optional[AVLTreeNode], target: Optional[AVLTreeNode]):
        """
        Given an AVLTreeNode, inserts the node in the tree rooted at "target", updates heights and balance
        factors of affected nodes in the tree, and updates parent pointers; finally, returns target of resulting tree.

        :param parent: target of AVL tree
        :param target: target AVL Node to be inserted
        :Time: O(log(n))
        :Space: O(log(n)) stack space proportional to height
        :return: target of resulting tree after insertion
        """

        if parent is None:
            # If parent is empty, this is the target of new tree
            return target

        if key < parent.key:
            # insert and update left child
            left_child = self.__insert(key, parent.left, target)
            parent.left = left_child
            # assign the parent
            left_child.parent = parent
        elif key > parent.key:
            # insert and update right child
            right_child = self.__insert(key, parent.right, target)
            parent.right = right_child
            # assign the parent
            right_child.parent = parent
        else:
            # no duplicate keys allowed; no insertion, return current parent as is
            return parent

        # finally, update heights and bf's of current parent after insertion completed (postorder processing)
        left_height = 0 if parent.left is None else parent.left.height
        right_height = 0 if parent.right is None else parent.right.height
        parent.bf = left_height - right_height
        # RE-BALANCE CURRENT parent (if required)
        return self.re_balance(parent)

    @staticmethod
    def re_balance(target: AVLTreeNode) -> AVLTreeNode:
        """
        Main re-balance routine to re-balance the tree rooted at target appropriately using rotations.
        4 cases:
        1) bf(target) = 2 and bf(target.left) < 0 ==> L-R Imbalance
        2) bf(target) = 2 ==> L-L Imbalance
        3) bf(target) = -2 and bf(target.right) > 0 ==> R-L Imbalance
        4) bf(target) = -2 ==> R-R Imbalance
        :param target: target of tree needing re-balancing.
        :return: target of resulting tree after rotations
        """

        def rotate_left(_target: AVLTreeNode) -> AVLTreeNode:
            """
            Performs a left rotation on the tree rooted at target, and returns target of resulting tree
            :param _target: target of tree
            :Time: O(1)
            :Space: O(1)
            :return: target of updated tree
            """
            # set up pointers
            pivot = _target.right
            _target.right = None
            tmp = pivot.left

            # 1st Move: reassign pivot's left child to target and update parent pointers
            pivot.left = _target
            pivot.parent = _target.parent  # pivot's parent now target's parent
            _target.parent = pivot  # target's parent now pivot

            # 2nd Move: use saved left child of pivot and assign it to target's right and update its parent
            _target.right = tmp
            if tmp:  # tmp can be null
                tmp.parent = _target

            # Not done yet - need to update pivot's parent (manually check which one matches the target that was passed)
            if pivot.parent:
                if pivot.parent.right == _target:  # if the parent's left subtree is the one to be updated
                    pivot.parent.right = pivot  # assign the pivot as the new child
                else:
                    pivot.parent.left = pivot  # vice-versa for left child

            # Still not done :) -- update bfs using tracked heights
            _target.bf = (0 if not target.right else target.right.height) - (
                0 if not target.left else target.left.height)
            pivot.bf = (0 if not pivot.right else pivot.right.height) - (0 if not pivot.left else pivot.left.height)

            # return target of new tree
            return pivot

        def rotate_right(_target: AVLTreeNode) -> AVLTreeNode:
            """
            Performs a right rotation on the tree rooted at target, and returns target of resulting tree
            :param _target: target of tree
            :Time: O(1)
            :Space: O(1)
            :return: target of updated tree
            """
            # set up pointers
            pivot = _target.left
            _target.left = None
            tmp = pivot.right

            # 1st Move: reassign pivot's right child to target and update parent pointers
            pivot.right = _target
            pivot.parent = _target.parent  # pivot's parent now target's parent
            _target.parent = pivot  # target's parent now pivot

            # 2nd Move: use saved right child of pivot and assign it to target's left and update its parent
            _target.left = tmp
            if tmp:  # tmp can be null
                tmp.parent = _target

            # Not done yet - need to update pivot's parent (manually check which one matches the target that was passed)
            if pivot.parent:
                if pivot.parent.left == _target:  # if the parent's left subtree is the one to be updated
                    pivot.parent.left = pivot  # assign the pivot as the new child
                else:
                    pivot.parent.right = pivot  # vice-versa for right child

            # Still not done :) -- update bfs using tracked heights
            _target.bf = (0 if not target.left else target.left.height) - (
                0 if not target.right else target.right.height)
            pivot.bf = (0 if not pivot.left else pivot.left.height) - (0 if not pivot.right else pivot.right.height)

            # return target of new tree
            return pivot

        # main function
        if target.bf == 2:
            if target.left.bf < 0:  # L-R
                target.left = rotate_left(target.left)
                return rotate_right(target)
            else:  # L-L
                return rotate_right(target)
        elif target.bf == -2:
            if target.right.bf > 0:  # R-L
                target.right = rotate_right(target.right)
                return rotate_left(target)
            else:  # R-R
                return rotate_left(target)
        else:
            # no need to re-balance
            return target
