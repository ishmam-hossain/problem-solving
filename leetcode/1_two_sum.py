# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:


def two_sum():
    compliments = [None]*len(nums)

    for i, n in enumerate(nums):
        if n in compliments:
            return [compliments.index(n), i]

        compliments[i] = (target - n)

    return []


if __name__ == '__main__':
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(two_sum())

