from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        for i in range(len(nums)+1):
            res = res ^ i
        return res
    
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i
        return res
