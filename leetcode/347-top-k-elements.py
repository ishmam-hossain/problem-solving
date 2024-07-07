from typing import List
from collections import Counter


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    frequency_list = []
    for x in range(len(nums) + 1):
        frequency_list.append([])

    for num, count in counter.items():
        frequency_list[count].append(num)

    res = []

    for item in reversed(frequency_list):
        if k == 0:
            return res
        if len(item) > k:
            item = item[:k]
            k = 0
            res.extend(item)
        else:
            res.extend(item)
            k -= len(item)

    return res


def top_k_with_sort(nums, k):
        c = dict()
        for n in nums:
            c[n] = c.get(n, 0) + 1
        cc = sorted(c.items(), key=lambda x: x[1], reverse=True)

        res = [cc[i][0] for i in range(k)]
        return res


a = [1, 1, 2, 2, 2, 4, 5, 5, 5]
ka = 2

print(top_k_frequent(a, ka))
