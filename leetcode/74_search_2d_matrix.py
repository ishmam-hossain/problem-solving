class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(arr: list, target: int) -> bool:
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if (mid_val := arr[mid]) == target:
                    return True
                if target < mid_val:
                    right = mid - 1
                if target > mid_val:
                    left = mid + 1

            return False

        found = False
        for arr in matrix:
            found = found or bin_search(arr, target)
        return found
