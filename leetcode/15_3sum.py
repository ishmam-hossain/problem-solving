class Solution:
    def threeSum(self, nums):
        def two_sum(j, target):
            temp = []
            compliments = [None]*len(nums)
            for i, n in enumerate(nums):
                if i != j:
                    if n in compliments:
                        found_cpl = [nums[compliments.index(n)], nums[i]]
                        if found_cpl not in temp:
                            temp.append(found_cpl)

                    compliments[i] = (target - n)

            return temp

        final = []
        for k, val in enumerate(nums):
            res = two_sum(k, -val)
            if res:
                for cpl in res:
                    cpl.append(val)
                    cpl = sorted(cpl)
                    if cpl not in final:
                        final.append(cpl)
        return final


if __name__ == '__main__':
    arr = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    s = Solution()
    print(s.threeSum(arr))
    print([[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]])
