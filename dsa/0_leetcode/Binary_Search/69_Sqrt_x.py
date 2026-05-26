from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1

        return ans


s = Solution()
print(s.mySqrt(400))
