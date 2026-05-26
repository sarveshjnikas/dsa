from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False
        

sol = Solution()
sol.isPalindrome(10)
