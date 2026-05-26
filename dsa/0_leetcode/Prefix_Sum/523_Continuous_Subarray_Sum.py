""" 
The sum of range (l,r) is asked many times.
Prefix sum is used to compute it as:

P = [0] * (len(nums) + 1)
for i in range(len(nums)):
    P[i + 1] = P[i] + nums[i]
    
sum_l_to_r = P[r + 1] - P[l]

"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        P = [0]*(len(nums)+1)
        for i in range(len(nums)):
            P[i+1] = P[i] + nums[i]
        
        # now if P[i] = a * k + r and P[j] = b * k + r
        # then subtraction (sum of cont subarray) will be divisible by k
        
        print(P)
        dict = {}
        for j in range(0, len(nums)+1):
            rem = P[j]%k
            if rem in dict:
                if j - dict[rem] >=2:
                    return True
            else:
                dict[rem] = j
        return False
