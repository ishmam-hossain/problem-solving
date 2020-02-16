class Solution:
    def minimumAbsDifference(self, arr):
        # gonna get a TLE :3
        res = {}
        arr.sort()
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    val = abs(arr[i] - arr[j])
                    comb = [[min(arr[i], arr[j]), max(arr[i], arr[j])]]
                    if val not in res:
                        res[val] = comb
                    else:
                        temp = res.get(val)
                        if comb[0] not in temp:
                            temp.extend(comb)
                            res[val] = temp

        return res.get(min(res.keys()))


s = Solution()
print(s.minimumAbsDifference([4, 2, 1, 3]))
print(s.minimumAbsDifference([1, 3, 6, 10, 15]))
print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))

"""
Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

"""
