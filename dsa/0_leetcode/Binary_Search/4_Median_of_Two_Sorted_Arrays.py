from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        combined = []
        while i < m or j < n:
            # print(combined)
            if i >= m:
                combined = combined + nums2[j:]
                break
            else:
                left = nums1[i]

            if j >= n:
                combined = combined + nums1[i:]
                break
            else:
                right = nums2[j]

            if left < right:
                combined.append(left)
                i = i + 1
            elif left > right:
                combined.append(right)
                j = j + 1
            else:
                combined.append(left)
                combined.append(right)
                i = i + 1
                j = j + 1
        l = len(combined)
        median = (
            combined[l // 2]
            if l % 2 == 1
            else (combined[l // 2 - 1] + combined[l // 2]) / 2
        )

        return median


s = Solution()
print(s.findMedianSortedArrays([4, 5, 11, 22, 33], [6, 7]))
