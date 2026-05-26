from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # choices, constraints, 
        res = []
        subset = []
        def backtrack(options):
            if len(subset) == len(nums):
                res.append([subset].copy())
                return
            
            for i in range(len(options)):
                subset.append(options[i])
                backtrack(options[:i] + options[i+1:])
                subset.pop()

        backtrack(nums)
        return res
        
sol = Solution()
sol.permute(nums = [])
