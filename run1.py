# MOST QUESTIONS IN THIS RUN ARE ALREADY SOLVED ONCE. THIS IS REVISION RUN. 

############################################################# 

class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = float("-inf")
        l = 0 
        r = len(height)-1
        while l <= r:
            curr_area = min(height[l], height[r])*(r-l)
            area = max(area, curr_area)
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return area
    
############################################################# 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                pres = nums[l] + nums[r]
                if pres == curr:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l+1 < n-1 and nums[l+1] == nums[l]:
                        l = l+1
                    l = l + 1
                    while r-1 >=0 and nums[r-1] == nums[r]:
                        r = r-1
                    r = r - 1
                elif pres < curr:   
                    l = l + 1
                else:
                    r = r - 1
        return triplets

#############################################################

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for word in strs:
            key = "".join(sorted(word))
            # if key in d:
            #     d[key].append(word)
            # else:
            #     d[key] = [word]
            d.setdefault(key, []).append(word) # ONE LINER FOR ABOVE FOUR LINES
        anagrams = []
        for key in d:
            anagrams.append(d[key])
        return anagrams
    
#############################################################

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # BRUTE FORCE: ONE PASS THROUGH ARRAY O(N)
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        n = len(nums)
        l = 0
        r = n-1
        while l <= r: # REMEMBER
            m = (l + r ) // 2 # REMEMBER
            if nums[m] == target:
                return m
            if nums[m] >=  nums[l]: # // ROUNDS DOWN SO MIDDLE CAN LAND ON LEFT BUT NOT ON RIGHT (OBVIOUSLY NOT TRUE FOR SINGLE ELEMENT)
                # THE LEFT SIDE IS SORTED
                if  nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m
            else:
                # RIGHT SORTED
                if  nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m 
        return -1
    
#############################################################
    
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # [4,11,20,23,30] 
        def feasible(m):
            t = 0
            for pile in piles:
                t +=  (pile + m - 1) // m
            return t <= h
        piles = sorted(piles)
        # BRUTE FORCE: FOR EACH VALUE IN 1-MAX(PILES) FIND HOURS NEEDED FOR EACH VALUE TO EAT ALL BANANAS. O(KN)
        l = 1
        r = piles[-1]
        # BINARY SEARCH, WHILE MAKING SURE THAT WE END UP ON THE SMALLEST VALUE
        while l <= r:
            m = (l + r ) // 2
            if feasible(m):
                r = m - 1
            else:
                l = m + 1

        return l
    
#############################################################
 
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def feasible(m):
            s = 0
            t = 1
            for weight in weights:
                if s + weight > m:
                    t  += 1
                    s = weight
                else:
                    s = s + weight
            return t <= days

        # LEAST WEIGHT CAP
        t = sum(weights)
        l = max(weights)
        r = t
    
        while l <= r:
            m = (l + r) // 2
            if feasible(m): # ABLE TO SHIP
                r = m - 1
            else:
                l = m + 1
        return l

