from typing import List 
from collections import defaultdict

class Int_Tree:
    '''
    Sorted integer binary tree
    When traversed in preorder it the integers will be sorted from least to greatest
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
    '''
    def __init__(self):
        self.tree = {}
        self.parent = None
        self.occurences = defaultdict(int)
        self.size = 0

    def add_child(self, child: int):
        '''
        Adds a child to the tree
        Left branch will always be less than the parent
        Right branch will always be greater than the parent
        '''

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
                if(not self.tree[node]["left"]):
                    self.tree[node]["left"] = child
                    self.tree[child] = empty_child
                    return
                else:
                    node = self.tree[node]["left"]
                    continue
           
            else: 
                if(not self.tree[node]["right"]):
                    self.tree[node]["right"] = child
                    self.tree[child] = empty_child
                    return
                else:
                    node = self.tree[node]["right"]
                    continue

    @staticmethod
    def remove_from_parent(parent: int, child: int) -> dict:
        if(parent["left"] == child):
            parent["left"] = None
        else:
            parent["right"] = None

#'''
#if a left exists, go there
#if no left exists, print this node, delete it, 
#if theres a right, go there
#otherwise, go back
#'''

    def collate(self) -> List[int]:
        '''
        A preorder traversal of the tree, returning a sorted list of the
        nodes of the tree
        '''

        tree = self.tree
        result = []
        stack = []
        node = self.parent
        traversed = set()

        while len(result) < self.size:
            stack.append(node)
            left = self.tree[node]["left"]
            right = self.tree[node]["right"]
            parent = stack[-1]

            if(left is None or left in traversed):
                result += [node] * self.occurences[node]
                traversed.add(stack.pop())

                if(right is None):
                    node = parent
                    continue
                else:
                    node = right
                    continue
            else:
                node = left
                continue

        return result
