class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        l = len(nums)
        output = [None] * l

        for i, n in enumerate(nums):
            output[i] = prod
            prod *= n

        prod = 1
        for i in range(l):
            output[l-1-i] = output[l-1-i] * prod
            prod = prod * nums[l-1-i]

        return output
    

s = Solution()
print(s.productExceptSelf([0, 1]))

