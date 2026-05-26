from typing import List

import math
class Solution:
    def jump(self, nums: List[int]) -> bool:
        jumps = [math.inf]*len(nums)
        reach = 0
        print(jumps)
        jumps[0] = 0
        print(jumps)
        for i in range(len(nums)):
            reach = max(reach, i+nums[i])
            for j in range(i+1, i+nums[i]+1):
                print(i,i+1, i+nums[i]+1)
                if j <= len(nums)-1:
                    jumps[j] = min(jumps[j], jumps[i]+1)
            print(jumps)
                
        return jumps[-1]
    

sol = Solution()

sol.jump(nums=[2,1])
