from typing import List

from itertools import permutations


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = n*["("] + n*[")"]
        # print(left)
        per = permutations(left)
        arr = ["".join(p) for p in set(per)]
        # print(len(set(arr)))
        # print(arr)
        arr2 =[]
        for i, element in enumerate(arr):
            # print(element)
            if element[0] == "(" and element[-1] == ")":
                arr2.append(element)
        print(arr2)
        return
        
sol = Solution()
sol.generateParenthesis(3)
