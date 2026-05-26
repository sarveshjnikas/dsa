from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                print(mid)
                left_index = mid
                right_index = mid

                while (left_index - 1) > 0 and nums[mid] == nums[left_index - 1]:
                    left_index = left_index - 1
                while (right_index + 1) < len(nums) and nums[mid] == nums[
                    right_index + 1
                ]:
                    right_index = right_index + 1

                return [left_index, right_index]

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left = 0
            right = len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

                if nums[mid] == target:
                    ans = mid

            return ans

        def findLast():
            left = 0
            right = len(nums) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

                if nums[mid] == target:
                    ans = mid

            return ans

        return [findFirst(), findLast()]


sol = Solution()
sol.searchRange(nums=[1, 1, 2], target=1)
