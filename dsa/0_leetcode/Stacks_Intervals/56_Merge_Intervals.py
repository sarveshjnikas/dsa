from typing import List
from collections import Counter

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        elif len(intervals) ==2:
            first_start = intervals[0][0]
            first_end = intervals[0][1]
            
            second_start = intervals[1][0]
            second_end = intervals[1][1]
            
            if first_end<= second_start:
                return [first_start, second_end]
            
            if second_end<= first_start:
                return [second_start, first_end]
            
            return intervals
        else:
            return self.merge(self.merge(intervals[:-1]),intervals[-1] )
        # merged = [] # start end
        return merged
        
    def merge(self, intervals):
        merged = [0] * 20

        for inter in intervals:
            merged[inter[0]:inter[1]] = [1] * (inter[1] - inter[0])

        answer = []
        i = 0
        while i < len(merged):
            if merged[i] == 0:
                i += 1
            else:
                j = i
                while j < len(merged) and merged[j] == 1:
                    j += 1
                answer.append([i, j])
                i = j

        return answer
    
    def merge(self, intervals):
        intervals.sort()
        # print(intervals)
        answer= []
        i = 0
        j = 1
        left = intervals[0]
        
        while i < len(intervals):
            # print(i,"i")
            while j<len(intervals) and j>=i and intervals[j][0] <= left[1]:
                left = [left[0], intervals[j][1]]
                answer.append(left)
                j = j + 1
            left = intervals[i]
            i = j
        return answer
        
    def merge(self, intervals):
        answer = []
        left_start, left_end = intervals[0]
        for start, end in intervals[1:]:
            if start <= left_end:
                left_end = max(left_end, end)
            else:
                answer.append([left_start, left_end])
                left_start, left_end = start, end
                
        answer.append([left_start, left_end])
        return answer
        


sol = Solution()
print(sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
