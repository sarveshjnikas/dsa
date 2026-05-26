from typing import List
from collections import Counter

class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     print(nums)
    #     last_seen = nums[0]
    #     new_nums = [nums[0]]
    #     for i in range(1, len(nums)):
    #         if nums[i] != last_seen:
    #             new_nums.append(nums[i])
    #             last_seen = nums[i]
    #     l = len(new_nums)
    #     new_nums.extend((len(nums)-l)*["_"])
    #     print(new_nums)
                

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

     
     
sol = Solution()
print(sol.removeDuplicates(nums = [1,1,1,1,2]))
