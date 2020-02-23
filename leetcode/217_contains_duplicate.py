class Solution:
    def containsDuplicate(self, nums) -> bool:
        """
        :param nums:
        :return: bool

        time --> O(n)
        space --> O(n)
        """
        has_seen = set()

        for n in nums:
            if n in has_seen:
                return True
            has_seen.add(n)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 4, 3, 5]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
