class Solution:
    def majorityElement(self, nums) -> int:
        """
        :param nums:
        :return: int

        Moor's Voting Algorithm
        """
        maj_index = 0
        count = 1

        for i, n in enumerate(nums[1:]):
            if nums[maj_index] == n:
                count += 1
            else:
                count -= 1

            if count == 0:
                maj_index = i
                count = 1

        return nums[maj_index]


s = Solution()
print(s.majorityElement([1, 2, 3, 2, 2, 2, 2, 5]))
