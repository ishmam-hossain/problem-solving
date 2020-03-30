from math import sqrt, ceil


class Solution:
    def constructRectangle(self, area: int):
        root = sqrt(area)
        if root == int(root):
            return [int(root)] * 2

        mid = ceil(root)
        low = mid - 1
        print(mid, low)
        last_diff = abs(mid - low)
        cur_pair = None

        while low > 0:
            if mid * low == area:
                if abs(mid - low) >= last_diff:
                    cur_pair = [mid, low]
                    last_diff = abs(mid - low)
            low -= 1
        return cur_pair


s = Solution()
print(s.constructRectangle(18))
