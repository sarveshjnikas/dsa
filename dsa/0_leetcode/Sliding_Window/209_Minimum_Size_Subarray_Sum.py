from typing import List
from collections import Counter

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_sub_len = 0
        for right, element in enumerate(nums):
            print(right, "---------")
            current_sum = current_sum + nums[right]
            print(current_sum)
            if current_sum == target:
                print("dd", right - left + 1)
                current_sum = current_sum - nums[left]
                left = left + 1

        return


sol = Solution()
sol.minSubArrayLen(target=7, nums=[2, 3, 2, 2, 4, 3])
