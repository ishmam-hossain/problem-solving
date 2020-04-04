class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_of_digits(x):
            d = 0
            while x:
                d += x % 10
                x //= 10

            return d

        all_ = {}
        max_sz = -99999999999
        for i in range(1, n + 1, 1):
            grp = sum_of_digits(i)
            temp = all_.get(grp, 0) + 1
            all_[grp] = temp
            max_sz = max(max_sz, temp)

        return list(all_.values()).count(max_sz)


s = Solution()
print(s.countLargestGroup(13))
