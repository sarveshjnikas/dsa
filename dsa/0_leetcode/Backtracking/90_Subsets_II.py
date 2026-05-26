class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = {}
        subset = []
        # at every index we are making a decision
        # do we include it or do we skip it
        
        def backtrack(i):
            # print(i, subset)
            subset.sort()
            key = "-".join(map(str,subset))
            
            if i >= len(nums):
                if key not in res:
                    res[key]= subset.copy()
                return 
            
            # decision to include number at index i
            subset.append(nums[i])
            backtrack(i+1)
            
            # decision to exclude number at index i
            subset.pop()
            backtrack(i+1)
            
        backtrack(0)
        return list(res.values())
