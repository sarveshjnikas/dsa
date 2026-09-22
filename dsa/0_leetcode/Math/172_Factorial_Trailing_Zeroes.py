class Solution:
    def trailingZeroes(self, n: int) -> int:
        # here we just find out maximum power of 5 in n!
        if n < 4:
            return 0
        i = 5
        tz = 0
        125
        while i <= n:
            p = i
            k = 0
            while p % 5 == 0:
                p = p / 5
                k += 1
            tz = tz + k
            i = i + 5

        return tz


sol = Solution()
sol.trailingZeroes(125000)
