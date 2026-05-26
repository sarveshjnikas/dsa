from typing import List
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # move the right pointer till we come across a char already seen
        # if already seen --> move the left pointer to the position last seen + 1

        longest_substring_length = 0
        left = 0
        character_map = {}
        for right, char in enumerate(s):
            print("--------")
            print(right, char)
            if char in character_map:
                left = character_map[char] + 1
                left = max(left, character_map[char] + 1)
                character_map[char] = right
            else:
                character_map[char] = right

            length_current = right - left + 1
            longest_substring_length = max(length_current, longest_substring_length)
            print("char", char, "left", left, "right", right)
            print(character_map)

        return longest_substring_length


solution = Solution()

print(solution.lengthOfLongestSubstring("abba"))
