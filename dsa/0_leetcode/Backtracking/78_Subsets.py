from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # at every index we are making a decision
        # do we include it or do we skip it
        
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # decision to include number at index i
            subset.append(nums[i])
            backtrack(i+1)
            
            # decision to exclude number at index i
            subset.pop()
            backtrack(i+1)
            
        backtrack(0)
        return res
        
    
sol = Solution()
sol.subsets([1,2,2])
