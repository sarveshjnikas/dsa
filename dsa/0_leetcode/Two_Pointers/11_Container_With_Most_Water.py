from typing import List

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = min(height[left], height[right]) * (right - left)

        while left <= right:
            if height[left] < height[right]:
                left += 1
                area = max(area, min(height[left], height[right]) * (right - left))
            else:
                right -= 1
                area = max(area, min(height[left], height[right]) * (right - left))

        return area


sol = Solution()
sol.maxArea(height=[1, 1])


"""
area = (right-left) * min(height[right], height[left])
left = i, right = j
height[i] < height[j]

What are we skipping?
(i, j), (i, j-1), (i, j-2)

So none of them can beat current best involving i

"""
