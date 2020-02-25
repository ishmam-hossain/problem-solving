class Solution:
    def thirdMax(self, nums) -> int:
        max_num = sec_max_num = third_max_num = -9999999999999

        for n in nums:
            if n > max_num:
                third_max_num = sec_max_num
                sec_max_num = max_num
                max_num = n
            elif sec_max_num < n < max_num:
                third_max_num = sec_max_num
                sec_max_num = n
            elif third_max_num < n < sec_max_num:
                third_max_num = n

        return third_max_num if third_max_num > -9999999999999 else max_num


s = Solution()
print(s.thirdMax([3, 2]))
