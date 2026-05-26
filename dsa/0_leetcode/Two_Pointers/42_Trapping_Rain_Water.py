from typing import List

"""
what i am thinking:
start at some point --> capture water 
    --> if we find bar taller or equal to our start --> capture
    --> else missed water
    
this does not work. even if we do not find a taller bar, water can be captured

THE CORE INSIGHT IS:

water trapped at position i = min(all bars to left, all bars to right) - h[i] --> if this is neg --> trap zero water
consider i where we know left_max now if that left_max < right then left_max < right_max

"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = 0 
        right_max = 0
        total_water  = 0
        while left < right:
            if height[left]< height[right]: # this means there exists a right wall at least as tall as height[right]
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total_water =  total_water + left_max - height[left]
                left +=1   
            else:
                if height[right] > right_max:
                    right_max = height[left]
                else:
                    total_water =  total_water + right_max - height[right]                
                right -=1
                
        return total_water
        
        
        
sol = Solution()
sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
