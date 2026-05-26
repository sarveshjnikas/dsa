from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        furthest = 0
        for i in range(len(nums)):
            if i <= furthest:
                furthest = max(furthest, i+nums[i])
        return furthest>= len(nums)-1
    

sol = Solution()
sol.canJump(nums=[2,0,0])
