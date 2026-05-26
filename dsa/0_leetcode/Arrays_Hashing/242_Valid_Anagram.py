from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


sol = Solution()
print(sol.isAnagram("rat", t="car"))
