from typing import List

class Solution:
    freq = {}

    def climbStairs(self, n: int) -> int:
        if n in self.freq:
            return self.freq[n]

        if n <= 2:
            return n

        self.freq[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.freq[n]
        
sol = Solution()
sol.climbStairs(10)
