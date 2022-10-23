from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mn = len(nums1) + len(nums2)
        res = [None] * mn
        a1p = a2p = 0

        i = 0
        while i < mn:
            if a1p >= len(nums1):
                res[i:] = nums2[a2p:]
                break
            elif a2p >= len(nums2):
                res[i:] = nums1[a1p:]
                break

            if nums1[a1p] < nums2[a2p]:
                res[i] = nums1[a1p]
                a1p += 1
            else:
                res[i] = nums2[a2p]
                a2p += 1
            i += 1

        mid = (mn - 1) // 2
        if mn % 2 == 0:
            return (res[mid] + res[mid + 1]) / 2
        return res[mid]


a1 = [1]
a2 = [1]
s = Solution()
print(s.findMedianSortedArrays(a1, a2))
