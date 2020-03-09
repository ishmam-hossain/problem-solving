class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr[:] = arr[:i] + [0]*2 + arr[i+1:length-1]
                i += 1
            i += 1

        if len(arr) >= length + 1:
            arr[:] = arr[:length + 1]


s = Solution()
print(s.duplicateZeros([0]))
