from typing import List
from collections import Counter

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_sum = [0]*len(self.nums) 
        self.nums_sum[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.nums_sum[i] = self.nums_sum[i-1]+self.nums[i]
        print(self.nums_sum)
        
    
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0 :
            return self.nums_sum[right]
        return self.nums_sum[right]-self.nums_sum[left-1]
        


obj = NumArray([-2, 0, 3, -5, 2, -1])
obj.sumRange(0,2)
