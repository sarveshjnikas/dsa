from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] --> number of ways to decode form i to end
        n = len(s)
        res = [0]*n
        res[n-1] = 1 if s[-1] != "0" else 0
        print(res)
        
sol = Solution()
sol.numDecodings("10")
