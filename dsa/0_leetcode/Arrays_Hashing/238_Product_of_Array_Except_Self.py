from typing import List
from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> int:
        product = 1
        zero_count = 0
        for ele in nums:
            if ele != 0:
                product = product * ele
            else:
                zero_count = zero_count + 1
                if zero_count >= 2:
                    return len(nums) * [0]
        if zero_count == 0:
            return [int(product / i) for i in nums]
        elif zero_count == 1:
            return [0 if i != 0 else product for i in nums]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        left_product = 1
        right_product = 1
        for i in range(1, len(nums)):
            left_product = left_product * nums[i - 1]
            left.append(left_product)

            right_product = right_product * nums[-i]
            right.append(right_product)

        return [a * b for a, b in zip(left, right[::-1])]


sol = Solution()
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
