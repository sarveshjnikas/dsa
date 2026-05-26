from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        n  = format(n, "032b")
        return n[::-1]

sol = Solution()
sol.reverseBits(n= 43261596)
