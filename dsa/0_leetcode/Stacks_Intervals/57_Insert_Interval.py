from typing import List
from collections import Counter

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        small = newInterval[0]
        big = newInterval[1]
        res = []
        i = 0
        n = len(intervals) 
        # small intervals
        while i < n and small > intervals[i][1]:
            res.append(intervals[i])
            i +=1
            
        print(res,"ppp")
        # combine with new intervals
        while i < n and big >= intervals[i][0]:
            small = min(small,intervals[i][0])
            big = max(big, intervals[i][1])
            i += 1
        
        res.append([small, big])
        # big intervals
        while i < n:
            res.append(intervals[i])
            i +=1
        # i +=1
        return res
        
sol = Solution()
sol.insert(intervals=([[1,2],[3,5],[6,7],[8,10],[12,16]]), newInterval = [4,8]) #[[1,2],[3,10],[12,16]]
# sol.insert(intervals=([[1,3],[6,9]]), newInterval = [2,5]) # [[1,5],[6,9]]
