from typing import List 
from collections import defaultdict


class Tree:
    """
    Sorted integer binary tree
    When traversed in inorder the integers will be sorted from least to greatest
    Example tree:
                   5
                  / \
                 3   6
                /\   /\ 
               2  4    8
              /\       /\
             1        7  9   
    When collated:
    1, 2, 3, 4, 5, 6, 7, 8, 9
    """
    def __init__(self):
        self.tree = {}
        self.parent = None
        self.occurences = defaultdict(int)
        self.size = 0

    def add_child(self, child: int):
        """
        Adds a child to the tree
        Left branch will always be less than the parent
        Right branch will always be greater than the parent
        """

        self.size += 1
        self.occurences[child] += 1
        empty_child = {"left": None, "right": None}

        if(not self.parent):
            self.tree[child] = empty_child 
            self.parent = child
            return
        else:   
            node = self.parent
           
        while 1:
            if(child < node):
                # If the child is less than the node, either move to the left 
                # node or add the child as the left node, if it is empty
                if(self.tree[node]["left"] is None):
                    self.tree[node]["left"] = child
                    self.tree[child] = empty_child
                    return
                else:
                    node = self.tree[node]["left"]
                    continue
           
            else: 
                if(self.tree[node]["right"] is None):
                    self.tree[node]["right"] = child
                    self.tree[child] = empty_child
                    return
                else:
                    node = self.tree[node]["right"]
                    continue

    def collate(self) -> List[int]:
        """
        A inorder traversal of the tree, returning a sorted list of the
        nodes of the tree
        """
        result = []
        stack = []
        node = self.parent

        while stack or node:
            if(node is not None):
                stack.append(node)
                node = self.tree[node]["left"]
            else:
                node = stack.pop()
                result += [node] * self.occurences[node]
                node = self.tree[node]["right"]

        return result
