class Solution:
    def preorder(self, root):
        if root is None:
            return []
        output = []
        i = 0
        while i < len(root):
            output.append(root[i])
            output.extend([root[i * 2], root[i * 2 + 1]])

        return output


s = Solution()
print(s.preorder([1, None, 3, 2, 4, None, 5, 6]))


"""

Input: root => [1, None, 3, 2, 4, None, 5, 6]

Output:        [1, 3, 5, 6, 2, 4]

--------------------------------------------------------------------
                 
Input: [1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8, null, 9, 10, null, null, 11, null, 12, null, 13, null, null, 14]

Output:        [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

"""
