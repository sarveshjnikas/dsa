"""
brute force solution
"""

class Solution:
    def find132pattern(self, nums):
        for i in range(0, len(nums)-2):
            print(nums[i])
            temp = [nums[i]]
            for j in range(i+1, len(nums)):
                print(nums[i], nums[j], temp)
                if len(temp) ==2:
                    print(temp)
                    if temp[0] < nums[j] < temp[-1]:
                        return True
                    if temp[-1] < nums[j]:
                        temp.pop()
                        temp.append(nums[j])
                else:
                    if temp[0] < nums[j]:
                        temp.append(nums[j])
                    
        return False