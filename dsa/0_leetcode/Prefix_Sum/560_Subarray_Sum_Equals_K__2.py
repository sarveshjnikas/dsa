from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s = s + nums[i]
            prefix_sum[i] = s

        print(nums)
        print(prefix_sum)
        ct = 0
        dict = {}
        dict[0] = 1

        for i in prefix_sum:
            req_sum = i - k

            if req_sum in dict:
                ct = ct + dict[req_sum]

            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            print(i, ct)

        return ct


# [1,-1], [0], [1,-1,0]
sol = Solution()
sol.subarraySum(nums=[1, -1, 0], k=0)
