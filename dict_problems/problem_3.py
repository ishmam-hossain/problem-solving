
def lca(node1, node2):
    if not node1 or not node2:
        raise TypeError

    if not node1.value or not node2.value:
        raise AttributeError

    node_1_ancestors = set()

    while node1.parent:
        node_1_ancestors.add(node1.value)
        node1 = node1.parent
    node_1_ancestors.add(node1.value)

    while node2.parent:
        if node2.value in node_1_ancestors:
            return node2.value
        node2 = node2.parent

    return node2.value


# -----------------------------------------
"""
Time Complexity: --> Linear
    
    * there are 2 while loops in the lca method
    * Assuming there are total n nodes in the tree
    
    * in worst case scenario any one of them will run n times where all the leaf nodes are in one side
            so, loop 1 time complexity --> O(n)
                loop 2 time complexity --> O(n)
        as both of the loops complexity is order of 1
        so, 
                final time complexity is --> O(n)
    
"""
# -----------------------------------------

"""
Problem statementg
-----------------------
Write following functions body.
2 Nodes are passed as parameter. 
You need to find Least Common Ancestor and print its value. 

-----------------------
Node structure are as following: 

class Node{ 
    value;
    parent; 
} 
-----------------------

                    1
                  /   \
                2       3
               /  \    /  \
              4    5  6    7
            /  \
           8    9
           
-----------------------
Ancestor Definition: 

1) Any node falls under parent chain till root node. 
2) A node is an ancestor of itself. 

For example:
if we consider Node 7 it’s ancestors will be 1, 3, and 7. 
All nodes values are unique for this tree. 

-----------------------
You function needs to find least common ancestor (closest common ancestor).

For an example for the tree image,
if 6 and 7 passed to lca it should return 3 if 3 and 7 passed to lca it should return 3 

-----------------------

"""
