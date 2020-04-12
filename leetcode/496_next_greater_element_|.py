class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        pos = {}
        for i, n in enumerate(nums2):
            pos[n] = i

        for n in nums1:
            index = pos.get(n) + 1
            while index < len(nums2):
                if nums2[index] > n:
                    res.append(nums2[index])
                    break
                index += 1
            else:
                res.append(-1)

        return res


s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
# print(s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
