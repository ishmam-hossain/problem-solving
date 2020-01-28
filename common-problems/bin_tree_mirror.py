class Tree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def mirror(root):
    if not root:
        return

    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)

    return root


tree5 = Tree(5, None, None)
tree6 = Tree(6, None, None)
tree7 = Tree(7, None, None)
tree8 = Tree(8, None, None)
tree9 = Tree(9, None, None)
tree4 = Tree(4, tree8, tree9)
tree3 = Tree(3, tree6, tree7)
tree2 = Tree(2, tree4, tree5)
tree1 = Tree(1, tree2, tree3)


x = mirror(tree1)
print(tree1.left.left.val)
print(tree1.right.right.left.val)

# __________________________________________
"""

                                1
                                
                            /       \
                          2           3
                        /   \       /   \
                      4      5     6     7
                    /   \
                  8      9        

"""