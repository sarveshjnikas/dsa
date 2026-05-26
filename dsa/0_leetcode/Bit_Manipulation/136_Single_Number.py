from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a ^ a = 0
        # a ^ 0 = a
        
        res = 0 
        for i in nums:
            res = res ^ i
        return res

        
sol = Solution()
sol.singleNumber(nums = [1])
