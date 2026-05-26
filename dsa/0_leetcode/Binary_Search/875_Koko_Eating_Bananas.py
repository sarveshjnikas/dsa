from typing import List

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k --> eating speed --> bananas per hour
        # each hour -- some pile
            # if pile has more bananas than k --> eat k
            # else --> eat all in that pile
        
        n = len(piles)
        left = 1 # best case scenario
        right = max(piles) # worst case scenario
        counter = 0
        while left <= right:
            counter +=1

            
            mid = left + (right - left) // 2
            hours = 0 
            for pile in piles: 
                hours = hours + math.ceil(pile/mid)
            
            # print(left, right, mid, hours, counter)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left 
    
    # right → last invalid value
    # left  → first valid value
                

sol = Solution()
sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
