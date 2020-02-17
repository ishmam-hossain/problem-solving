class Solution:
    def singleNumber(self, nums):
        visited = []
        for n in nums:
            if n in visited:
                visited.remove(n)
            else:
                visited.append(n)

        return visited[0]

    def single_num_dict(self, nums):
        count = {}
        for n in nums:
            temp = count.get(n)
            if temp:
                count.pop(n)
            else:
                count[n] = 1
        return count.__iter__().__next__()

    def single_num_set(self, nums):
        unq_nums = set()
        for n in nums:
            if n in unq_nums:
                unq_nums.remove(n)
            else:
                unq_nums.add(n)

        return unq_nums.__iter__().__next__()

    def single_num_xor(self, nums):
        res = 0
        for n in nums:
            res = res ^ n

        return res


s = Solution()
# print(s.singleNumber([2, 2, 4, 4, 1]))
# print(s.single_num_dict([2, 2, 4, 4, 1]))
# print(s.single_num_set([2, 2, 4, 4, 1]))
print(s.single_num_xor([2, 2, 4, 4, 1]))
