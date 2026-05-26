from typing import List
from collections import Counter

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]*len(nums)
        s = 0
        for i in range(len(nums)):
            s = s + nums[i]
            prefix_sum[i] = s
        # print(prefix_sum)  
        for j in range(len(nums)):
            left = 0 if j==0 else prefix_sum[j-1]
            right = prefix_sum[-1] - nums[j] - left
            if left == right:
                return j
        return -1

sol = Solution()
sol.pivotIndex(nums = [1,7,3,6,5,6])
