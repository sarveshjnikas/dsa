from typing import List
from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            print(i)
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                print(i, seen[nums[i]])
                if i - seen[nums[i]] <= k:
                    return True
                seen[nums[i]] = i
        return False


sol = Solution()
sol.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
