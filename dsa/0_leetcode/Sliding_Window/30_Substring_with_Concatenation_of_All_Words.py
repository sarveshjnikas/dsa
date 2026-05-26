from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        required_incdices = []
        section_length = len(words[0])
        total_len = len(words) * section_length
        freq = Counter(words)
        for i in range(0, len(s) - total_len + 1):
            section = s[i : i + len(words) * section_length]
            chunks = [
                section[j : j + section_length]
                for j in range(0, len(section), section_length)
            ]
            freq_index = Counter(chunks)
            if freq_index == freq:
                required_incdices.append(i)

        return required_incdices


sol = Solution()
sol.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"])
