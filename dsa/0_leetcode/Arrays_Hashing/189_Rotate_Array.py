from typing import List
from collections import Counter

class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     for i in range(k):
    #         nums[:] = [nums[-1]] + nums[:-1]
    #     print(nums)

    # chatgpt optimised
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k :] + nums[: n - k]


sol = Solution()
print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))
