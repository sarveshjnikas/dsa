from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        offset = 10
        seen = set()
        repeated = set()

        for i in range(offset):
            for j in range(i, len(s) - offset + 1, offset):
                seq = s[j : j + offset]
                if seq in seen:
                    repeated.add(seq)
                else:
                    seen.add(seq)

        return list(repeated)


sol = Solution()
sol.findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
