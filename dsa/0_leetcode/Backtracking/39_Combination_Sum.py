class Solution:
    def tionSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i, sum):
            # BASE CASE
            if sum == target:
                res.append(subset.copy())
                return 
            
            # CONSTRAINT
            if i >= len(candidates) or sum > target:
                return 
            
            # CHOICES
            subset.append(candidates[i])
            backtrack(i, sum+ candidates[i]) # BACKTRACKING
            
            subset.pop()
            backtrack(i+1, sum)
                
        backtrack(0, 0)
        return  res
    
sol = Solution()
sol.combinationSum( candidates = [7,3,2], target = 18)
