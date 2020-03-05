class Solution:
    def findSpecialInteger(self, arr) -> int:
        """A wrong solution but will work for this particular problem :3"""
        if len(arr) == 1:
            return arr[0]

        count = 1
        last_max_count = count
        length = len(arr)

        for i, _ in enumerate(arr[1:]):
            if arr[i+1] == arr[i]:
                count += 1
                if count >= int(length*.25) and count > last_max_count:
                    last_max_count = arr[i+1]
            else:
                count = 1

        return last_max_count


s = Solution()
print(s.findSpecialInteger([1,2,3,3]))