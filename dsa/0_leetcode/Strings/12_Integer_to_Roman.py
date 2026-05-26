from typing import List
from collections import Counter

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [int(x) for x in str(num)]
        length = len(digits)
        for i, digit in enumerate(digits):
            print(digit, 10 ** (length - i - 1))
            # if digit == 4 or digit == 9:
            #     return ""
            # else:
            #     return ""

        return ""


solution = Solution()

print(solution.intToRoman(80))
