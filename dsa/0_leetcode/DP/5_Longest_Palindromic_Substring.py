from typing import List

# bruteforce solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> str:
            return True if s == s[len(s)::-1]  else False
        pal = ""
        for i in range(0, len(s)+1):
            for j in range(i, len(s)+1):
                pal = s[i:j] if isPalindrome(s[i:j]) and j-i+1 > len(pal) else pal
        print(pal)
            
            
# expand solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # trying to see longest palindrome we can get
        # case1: current ele in middle --> odd number of elements
        # case2: current ele + next in middle --> even number of elements

        def expand(l: int, r: int) -> str:
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        pal = ""
        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            pal = max(p1,p2,pal,key=len)
        return pal


sol = Solution()
sol.longestPalindrome("babad")
