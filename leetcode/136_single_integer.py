class Solution:
    def singleNumber(self, nums):
        visited = []
        for n in nums:
            if n in visited:
                visited.remove(n)
            else:
                visited.append(n)

        return visited[0]


s = Solution()
print(s.singleNumber([2, 2, 4, 4, 1]))
