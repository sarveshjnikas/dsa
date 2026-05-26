from typing import List
from collections import Counter

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        stack.append((0,nums[0]))
        for i in range(1, 2*n):
            i = i% n
            while stack and stack[-1][1] < nums[i]:
                res[stack[-1][0]] = nums[i]
                # print(res, stack)
                stack.pop()
            stack.append((i, nums[i]))
        return res
        
        
sol = Solution()
sol.nextGreaterElements(nums = [9,1,1,1,3,4,3])
