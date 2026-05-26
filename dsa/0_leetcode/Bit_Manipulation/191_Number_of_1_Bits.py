from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        bi = bin(n)[2:]
        count = 0
        for i in bi:
            if int(i) == 1:
                count += 1
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count = count + (n & 1)
            n = n >> 1
        return count
sol = Solution()
sol.hammingWeight(n= 128)
