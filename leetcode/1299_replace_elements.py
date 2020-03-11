class Solution:
    def replaceElements(self, arr):
        temp = last_temp = -1
        length = len(arr) - 1

        for i in range(len(arr)):
            temp = max(arr[length - i], temp)
            arr[length - i] = last_temp
            last_temp = temp

        return arr


s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))  # [18,6,6,6,1,-1]
