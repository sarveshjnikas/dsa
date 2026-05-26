from typing import List
from collections import Counter

from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        width =  valueDiff + 1
        for i, num in enumerate(nums):
            
            bucket = num // width
            
            if bucket in buckets:
                return True
            
            if bucket-1 in buckets and abs(buckets[bucket-1] - num) <= valueDiff:
                return True
            
            if bucket+1 in buckets and abs(buckets[bucket+1] - num) <= valueDiff:
                return True
            
            buckets[bucket] = num
            
            # kind of a sliding window, 
            # if index diff = 2, 0,1,2 are fine but for i > 3 --> evict the oldest index 
            # before move foward keep the window ready. for 2 evict 0 so that for 3 only 1,2 are there
             
            if i >= indexDiff:
                old= nums[i-indexDiff]
                del buckets[old//width]
                
        return False
                        

sol = Solution()
print(sol.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3))
