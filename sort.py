from Tree import Tree
from typing import List


def tree_sort(l: List(int)) -> List(int):
    """
    A python implementation of tree sort
    Tree sort constructs a binary search tree where each left branch is less
    than the parent, and each right branch is greater than the parent. When 
    the tree is traversed in inorder the nodes are in ascending order
    """

    tree = Tree()
    [tree.add_child(n) for n in l]
    return tree.collate()
