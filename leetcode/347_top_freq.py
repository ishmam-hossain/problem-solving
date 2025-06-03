class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in nums:
            count[n] = count.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums))]

        for n, c in count.items():
            bucket[c-1].append(n)

        res = []
        for n in bucket[::-1]:
            if k <= 0:
                return res
            if not n:
                continue

            res.extend(n[:k])
            k -= len(n)

        return res
