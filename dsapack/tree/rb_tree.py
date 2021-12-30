from typing import Optional

from dsapack.tree import DSTree, RBTreeNode, Color


class RedBlackTree(DSTree[RBTreeNode]):
    root: RBTreeNode

    def __init__(self, *nodes):
        super().__init__(*nodes)

    def insert(self, key, value=None):
        """
        Public insert function to insert a node into a Red-Black Tree
        :param key: key of node to be inserted
        :param value: corresponding value
        :Time: O(log(n))
        :Space: O(log(n))
        :return: none
        """
        # noinspection DuplicatedCode
        def insert_helper(parent: Optional[RBTreeNode], target: Optional[RBTreeNode]):
            if parent is None:
                # If parent is empty, this is the target of new tree
                return target

            if key < parent.key:
                # insert and update left child
                left_child = insert_helper(parent.left, target)
                parent.left = left_child
                # assign the parent
                left_child.parent = parent
            elif key > parent.key:
                # insert and update right child
                right_child = insert_helper(parent.right, target)
                parent.right = right_child
                # assign the parent
                right_child.parent = parent
            else:
                # no duplicate keys allowed; no insertion, return current parent as is
                return parent

            # RE-COLOR nodes using insert fix algorithm
            return RedBlackTree.insert_fix(target)  # type: ignore

        new_node = RBTreeNode(key, value)
        self._data.append(new_node)
        # Returns target of resulting tree after insertion - update it
        self.root = insert_helper(self.root, new_node)
        if not self.root.is_root:
            self.root = self.root.get_root()
        # Root node is always black
        self.root.color = Color.BLACK

    @staticmethod
    def insert_fix(target: RBTreeNode):
        def rotate_left(_target: RBTreeNode) -> RBTreeNode:
            """
            Performs a left rotation on the tree rooted at target, and returns target of resulting tree
            :param _target: target of tree
            :Time: O(1)
            :Space: O(1)
            :return: target of updated tree
            """
            # set up pointers
            pivot = _target.right
            tmp = pivot.left

            # 1st Move: reassign pivot's left child to target and update parent pointers
            pivot.left = _target
            pivot.parent = _target.parent  # pivot's parent now target's parent
            _target.parent = pivot  # target's parent now pivot

            # 2nd Move: use saved left child of pivot and assign it to target's right and update its parent
            _target.right = tmp
            if tmp:  # tmp can be null
                tmp.parent = _target

            # 3rd Move: update pivot's parent (manually check which one matches the target that was passed)
            if pivot.parent:
                if pivot.parent.right == _target:  # if the parent's left subtree is the one to be updated
                    pivot.parent.right = pivot  # assign the pivot as the new child
                else:
                    pivot.parent.left = pivot  # vice-versa for left child

            # return target of new tree
            return pivot

        def rotate_right(_target: RBTreeNode) -> RBTreeNode:
            """
            Performs a right rotation on the tree rooted at target, and returns target of resulting tree
            :param _target: target of tree
            :Time: O(1)
            :Space: O(1)
            :return: target of updated tree
            """
            # set up pointers
            pivot = _target.left
            tmp = pivot.right

            # 1st Move: reassign pivot's right child to target and update parent pointers
            pivot.right = _target
            pivot.parent = _target.parent  # pivot's parent now target's parent
            _target.parent = pivot  # target's parent now pivot

            # 2nd Move: use saved right child of pivot and assign it to target's left and update its parent
            _target.left = tmp
            if tmp:  # tmp can be null
                tmp.parent = _target

            # 3rd Move: update pivot's parent (manually check which one matches the target that was passed)
            if pivot.parent:
                if pivot.parent.left == _target:  # if the parent's left subtree is the one to be updated
                    pivot.parent.left = pivot  # assign the pivot as the new child
                else:
                    pivot.parent.right = pivot  # vice-versa for right child

            # return target of new tree
            return pivot

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Main function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # BC1: Target is root
        if target.is_root:
            target.color = Color.BLACK
            return target

        # setup pointers
        parent: RBTreeNode = target.parent
        grandpa: RBTreeNode = parent.parent

        # BC2: Target node is BLACK
        if parent.color == Color.BLACK:
            return parent

        # If parent is the left child of grandparent
        if parent == grandpa.left:
            uncle = grandpa.right
            # Case: If uncle is RED, both siblings set to BLACK and grandpa will be RED
            if uncle and uncle.color == Color.RED:
                uncle.color = Color.BLACK
                parent.color = Color.BLACK
                # Re-balancing the tree starting from grandpa node
                return RedBlackTree.insert_fix(grandpa)

            # Case:LL -> If target is left child of the parent,
            # Parent and Grandpa will swap the color do left-left rotation
            if target == parent.left:
                parent.color = Color.BLACK
                grandpa.color = Color.RED
                target = rotate_right(grandpa)
            # Case:LR -> If target is right child of the parent, doing left-right rotation
            else:
                target = rotate_left(parent)

            # Re-balancing the tree starting from target node
            return RedBlackTree.insert_fix(target)

        # If parent is the right child of grandparent
        else:
            uncle = grandpa.left
            # Case: If uncle is RED, both siblings set to BLACK and grandpa will be RED
            if uncle and uncle.color == Color.RED:
                uncle.color = Color.BLACK
                parent.color = Color.BLACK
                # Re-balancing the tree starting from grandpa node
                return RedBlackTree.insert_fix(grandpa)

            # Case:RR -> If target is right child of the parent,
            # Parent and Grandpa will swap the color do right-right rotation
            if target == parent.right:
                parent.color = Color.BLACK
                grandpa.color = Color.RED
                target = rotate_left(grandpa)
            # Case:RL -> If target is left child of the parent, doing right-left rotation
            else:
                target = rotate_right(parent)

            # Re-balancing the tree starting from target node
            return RedBlackTree.insert_fix(target)
