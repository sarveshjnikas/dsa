from typing import List
from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        def getConjugate(e):
            if e == ")":
                return "("
            elif e == "]":
                return "["
            else:
                return "{"
        
        if len(s) % 2 == 1:
            return False

        opens = ["(", "[", "{"]

        open_stack = []
        for i in s:
            if i in opens:
                open_stack.append(i)
            else:
                if len(open_stack)>=1:
                    if getConjugate(i) != open_stack[-1]:
                        print(i,getConjugate(i) )
                        return False
                    else: 
                        open_stack.pop(-1)
                else:
                    return False
              
        return True if len(open_stack) == 0 else False
    
sol = Solution()
print(sol.isValid("))"))
