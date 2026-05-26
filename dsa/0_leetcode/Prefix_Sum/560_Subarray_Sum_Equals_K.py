from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            sum_till = 0
            for j in range(i, len(nums)):
                sum_till = sum_till + nums[j]
                if sum_till == k: 
                    total += 1
        return total
        
        
sol = Solution()
sol.subarraySum(nums = [1,2,3], k = 3)
