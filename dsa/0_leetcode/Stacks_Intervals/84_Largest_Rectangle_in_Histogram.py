from typing import List
from collections import Counter

class Solution:
    # brute force
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        for i in range(0, len(heights)):
            for j in range(i, len(heights)):
                height = min(heights[i:j+1])
                largest_area = max(largest_area,(j-i+1)*height)
        return largest_area
    
    # optimised
    def largestRectangleArea(self, heights: List[int]) -> int:
        width = 1
        largest_area = heights[0]*width
        left = 0
        for i in range(1, len(heights)):
            current_height = heights[i]
            # if largest area increases --> do nothing
            # if it decreases
            if current_height*width > largest_area:
                left = i
                
              
        return largest_area    
        
sol = Solution()
print(sol.largestRectangleArea(heights = [2,1,5,6,2,3]))
