from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # NUMBER OF SUCH PROBLEMS NEED US TO THINK ABOUT WHAT IS THE OPTIMAL SOLUTUTION ENDING AT INDEX 
        product_max = [0]*len(nums)
        product_min = [0]*len(nums)
        
        product_max[0] = nums[0]
        product_min[0] = nums[0]

        for i in range(1, len(nums)):
            product_max[i] = max(product_min[i-1] * nums[i], nums[i], product_max[i-1] * nums[i])
            product_min[i] = min(product_min[i-1] * nums[i], nums[i], product_max[i-1] * nums[i])                
        return max(product_max)