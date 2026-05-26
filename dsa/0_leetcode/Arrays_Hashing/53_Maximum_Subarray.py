from typing import List
from collections import Counter

class Solution:
    # bruteforce

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                print(nums[i : j + 1], sum(nums[i : j + 1]))
                if sum(nums[i : j + 1]) > max_sum:
                    max_sum = sum(nums[i : j + 1])
        return max_sum

    # Kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0 :
                curr_sum = 0
            
        return max_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*n
        for i in range(n):
            arr[i] = max(nums[i], arr[i-1]+nums[i])

        print(max(arr))
sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
