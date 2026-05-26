from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_of_freq = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in freq_of_freq:
                freq_of_freq[key].append(i)
            else:
                freq_of_freq[key] = [i]
        return list(freq_of_freq.values())
        
sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
