class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1).intersection(set(nums2))

    def intersection_faster(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [n for n in nums1 if n in nums2]
