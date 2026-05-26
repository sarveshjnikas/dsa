class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        res = []
        subset = []
        def backtrack(i, remaining):
            
            if remaining == 0:
                res.append(subset.copy())
                return

            if i >= len(candidates) or remaining < 0:
                return
            
            # choices
            # 1. keep the number in the solution
            subset.append(candidates[i])
            backtrack(i+1, remaining-candidates[i])
            
            # 2. do not keep the number in the solution
            subset.pop()
            
            j = i
            while j + 1 < len(candidates) and candidates[j] == candidates[j+1]:
                j +=1
            backtrack(j+1, remaining)
            
        backtrack(0, target)    
        return res

sol = Solution()
sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
