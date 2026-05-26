from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # we will be building the string from left to right
        # at any point we can open bracket (if we have enough open brackets)
        # but we can not always add a closing bracket (only if open > close)
        
        def backtrack(s, open, close):
            if len(s) == 2*n:
                res.append(s)
                return 
            
            # choices
            if open < n:
                backtrack(s + "(", open+1, close)
                
            if close < open:
                backtrack(s + ")", open, close+1)
            
            
        backtrack("", 0, 0)
        return res 
    
sol = Solution()
sol.generateParenthesis(2)
