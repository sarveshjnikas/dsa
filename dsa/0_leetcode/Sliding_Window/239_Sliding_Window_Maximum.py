from typing import List
from collections import Counter

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        maximum = []

        for right in range(len(nums)):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] <= right - k:
                dq.popleft()

            current_window_max = dq[0]
            if right >= k - 1:
                maximum.append(nums[current_window_max])

        return maximum


sol = Solution()
sol.maxSlidingWindow(nums=[1, 2, 300, 4, 5, 1, 2000], k=3)
