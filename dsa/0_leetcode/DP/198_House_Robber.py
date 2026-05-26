from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        odd_sum = 0
        even_sum = 0
        for i in range(len(nums)):
            if i%2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
        return max(even_sum, odd_sum)
    
    last_index = 0
    def rob(self, nums: List[int]) -> int:
        max_rob = 0
        l = len(nums)
        if l == 1:
            return nums[0]
        
        if l == 2:
            if nums[0]>nums[1]:
                self.last_index = 0
                # print(self.last_index)

                return nums[0]
            # , self.last_index
            else:
                self.last_index = 1
                return nums[1]
            # , self.last_index
        if l>=3:
            subsol = self.rob(nums[0:-1])
            print(l,subsol,self.last_index)
            if self.last_index == l-2:
                if nums[self.last_index] > nums[-1]:
                    return subsol
                # , self.last_index
                else: 
                    self.last_index = self.last_index-1
                    # print(l,"o")
                    return (subsol-nums[l-2]+ nums[self.last_index]+nums[-1])
                # , self.last_index
            
            else:
                self.last_index = l-1
                # print(self.last_index,"property")
                return subsol + nums[-1]
            # , self.last_index

            
        return None
    
    def rob(self, nums):
        """
        at house i we have two options
        we either rob house i and don't rob house i-1
        or 
        we skip house i
        """
        if len(nums) == 1:
            return nums[0]
        
        second = nums[0]
        first = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(first, second + nums[i])
            second = first
            first = current
        
        return first
        
  
sol = Solution()
print(sol.rob([1000,2,3]))
