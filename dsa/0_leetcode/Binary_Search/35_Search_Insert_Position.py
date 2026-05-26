from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                return mid + 1
        return low


s = Solution()
print(s.searchInsert(nums=[1, 2, 3, 4, 5, 6], target=7))
