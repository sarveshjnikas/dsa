from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = Counter(s1)
        window = Counter(s2[0:n])

        if need == window:
            return True

        for i in range(n, m):
            window[s2[i]] += 1
            window[s2[i - n]] -= 1

            if window == need:
                return True

        return False


sol = Solution()
sol.checkInclusion(s1="ab", s2="abdbaooo")
