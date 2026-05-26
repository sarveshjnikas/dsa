from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(i, remaining):
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            if i == len(nums):
                return 1 if remaining == 0 else 0
            
            if i >= len(nums):
                return

            using_subtract = backtrack(i+1, nums[i]+remaining)
            using_add = backtrack(i+1, -nums[i]+remaining)
            memo[(i, remaining)] = using_add + using_subtract
            return  memo[(i, remaining)] 
            
        return backtrack(0, target)
        
sol = Solution()
sol.findTargetSumWays(nums = [1,2,3], target = 6)
