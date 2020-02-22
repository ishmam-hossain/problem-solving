# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2

        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t2.right = self.mergeTrees(t1.right, t2.right)

        return t1


tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)


s = Solution()
print(s.mergeTrees(tree1, tree2))

"""
Input: 
           Tree 1                     Tree 2   
                       
              1                         2                             
             / \                       / \                            
            3   2                     1   3                        
           /                           \   \                      
          5                             4   7  
          
          
Output: 
                        Merged tree:
                        
                             3
                            / \
                           4   5
                          / \   \ 
                         5   4   7      

"""
