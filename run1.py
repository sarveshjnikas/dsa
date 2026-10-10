# MOST QUESTIONS IN THIS RUN ARE ALREADY SOLVED ONCE. THIS IS REVISION RUN. 

############################################################# 
# TWO POINTERS AND HASHMAPS
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
# BINARY SEARCH
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



#############################################################
# STACKS
#############################################################


class Solution:
    def isValid(self, s: str) -> bool:
        opp = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack or stack.pop() != opp[c]: # if not stack is true --> return false right away so code will enter or only if stack is there. also stack.pop() removes and then checks. 
                    return False
        return not stack
    
#############################################################

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # BRUTE FORCE IS SIMPLY ITERATE TWICE IN O(N^2)

        stack = [] # INDICES OF THE UNRESOLVED TEMPERATURES
        warmer = [0] * len(temperatures)
        # FOR EACH TEMPERATURE WHICH PREVIOUS INDICES DOES THIS TEMPERATURE RESOLVE?
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                j = stack.pop()
                warmer[j] = i - j
            stack.append(i)
        return warmer

#############################################################

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        alive = True
        stack = []
        for i in range(len(asteroids)):
            alive = True
            a = asteroids[i]
            
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:  # TOP IS DESTROYED
                    stack.pop()
                elif stack[-1] == -a:  # BOTH ARE DESTROYED
                    stack.pop()
                    alive = False
                else:  # A IS DESTROYED
                    alive = False
        
            if alive:
                stack.append(a)
        return stack


#############################################################
# LINKED LIST
#############################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None # DRAW INITAL AND FINAL LISTS AND THIS STEP BECOMES OBVIOUS. 
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    
    
#############################################################
# DYNAMIC PROGRAMMING
#############################################################

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <=2:
            return max(nums)

        coins = [0]*len(nums) # AT i, BEST POSSIBLE MONEY i ONWARDs
        coins[-1] = nums[-1]
        coins[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, -1, -1):
            coins[i] = max(nums[i]+ coins[i+2], coins[i+1])
        return coins[0]
    
#############################################################

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1) # ith ENTRY, LEAST NUMBER OF COINS NEEDED TO MAKE AMOUNT i
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                a = dp[amt-coin] + 1 if amt -coin >= 0 else float("inf")
                dp[amt] = min(dp[amt], a)
        return dp[amount] if dp[amount] != float('inf') else -1

#############################################################

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.ans = {}
        def dfs(s):
            if s in wordDict:
                return True

            if s in self.ans:
                return self.ans[s]

            x = False
            for word in wordDict:
                if s.startswith(word):
                    x = x or dfs(s[len(word):])
            self.ans[s] = x
            return x
        return dfs(s)