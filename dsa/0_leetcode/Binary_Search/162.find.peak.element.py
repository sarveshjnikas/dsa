from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # PROBLEM STATES THAT WE GOTTA SOLVE THIS IN LOG TIME -> SO SOME KIND OF BINARY SEARCH
        # GIVEN THAT nums[i] != nums[i + 1]. SO FROM ANY INDEX IF nums[i] < nums[i+1] AS nums[n]= INF 
        # WE CAN BE CERTAIN THAT A PEAK EXISTS IN [i+1, n-1]
        # ELSE A PEAK EXISTS BETWEEN [0,i]
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right-left) // 2
            
            l_ele = nums[mid-1] if mid-1 >= 0 else float('-inf')
            r_ele = nums[mid+1] if mid+1 <= len(nums)-1 else float('-inf')

            
            if nums[mid] > l_ele and nums[mid] > r_ele:
                return mid
            
            if nums[mid+1] > nums[mid]:
                left = mid+1
            else:
                right = mid