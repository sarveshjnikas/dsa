from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # if middle value is > left value --> left half sorted
                if nums[left] <= target < nums[mid]:
                    # target lies in the sorted part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # else --> right half sorted
                if nums[mid] < target <= nums[right]:
                    # target lies in the sorted part
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


sol = Solution()
sol.search([4, 5, 6, 7, 0, 1, 2], target=0)
