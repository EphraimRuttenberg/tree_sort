from Int_Tree import Int_Tree as Tree
import unittest

def init_tree() -> Tree:
    '''
    Generates a tree that looks like
                    6
                   / \
                  5   8
                 /\   /\
                2    7  9 
               /\       /\
              1  3       10
                 /\
                   4      
    '''
    tree = Tree()
    children = [6, 8, 9, 5, 2, 1, 3, 7, 10, 4]
    [tree.add_child(child) for child in children]
    return tree

class Create_Parent(unittest.TestCase):
    def test(self):
        tree = Tree()
        tree.add_child(5)
        assert(tree.parent == 5)

class Children_Are_None(unittest.TestCase):
    def test(self):
        tree = Tree()
        tree.add_child(5)
        assert(tree.tree[5]["left"] is None)
        assert(tree.tree[5]["right"] is None)
                      
class Single_Left_Child(unittest.TestCase):
    def test(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(3)
        assert(tree.tree[5]["left"] == 3)
        

class Single_Right_Child(unittest.TestCase):
    def test(self):
        tree = Tree()
        tree.add_child(5)
        tree.add_child(6)
        assert(tree.tree[5]["right"] == 6)

class Two_Children(unittest.TestCase):
    def test(self):
       tree = Tree()
       children = [5, 4, 6]
       [tree.add_child(child) for child in children]
       assert(tree.tree[5]["left"] == 4 and tree.tree[5]["right"] == 6)

class Complex_Tree(unittest.TestCase):
    def test(self):
        tree = init_tree()
        assert(tree.parent == 6)
        try:
            assert(tree.tree == {
                6:  {"left": 5,     "right": 8},
                8:  {"left": 7,     "right": 9},
                9:  {"left": None,  "right": 10},
                5:  {"left": 2,     "right": None},
                2:  {"left": 1,     "right": 3},
                1:  {"left": None,  "right": None},
                3:  {"left": None,  "right": 4},
                7:  {"left": None,  "right": None},
                10: {"left": None,  "right": None},
                4:  {"left": None,  "right": None}
                })
        except AssertionError:
            raise AssertionError(str(tree.tree))

class Collate(unittest.TestCase):
    def test(self):
        tree = init_tree()
        l = tree.collate()
        try:
            assert(l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        except AssertionError:
            raise AssertionError(str(l))


if __name__ == "__main__":
    unittest.main()
