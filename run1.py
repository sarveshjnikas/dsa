# MOST QUESTIONS IN THIS RUN ARE ALREADY SOLVED ONCE. THIS IS REVISION RUN. 

############################################################# 
# TWO POINTERS AND HASHMAPS AND BASICS
############################################################# 

from typing import List

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
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]
            d[nums[i]] = i
            
#############################################################
          
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # ASK AT i WHAT THE THE SUBARRAY WITH THE LARGET SUM ENDING AT i
        curr = best = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            best = max(curr, best)
        return best
 
#############################################################
# APPROACH 1: O(N) TIME AND SPACE
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        # MAX HEIGHT LEFT TO THE BAR AND RIGHT TO THE BAR
        left = [0]*n
        right = [0]*n

        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])

        for j in range(n-2, -1, -1):
            right[j] = max(right[j+1], height[j+1])
        
        water = 0 
        for i in range(n):
            water += max(0, min(left[i], right[i])-height[i])
        return water  
     
# APPROACH 2: O(N) TIME AND O(1) SPACE
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        left_max = 0
        right_max = 0
        # AT ANY POINT, WHAT ARE WE LOOKING FOR? TALLEST WALL ON THE RIGHT AND ON THE LEFT
        # FOR THE LEFT POINTER I CAN NOT ANSWER WHAT IS THE TALLEST WALL ON THE RIGHT
        # FOR THE RIGHT POINTER I CAN NOT ANSWER WHAT IS THE TALLEST WALL ON THE LEFT
        water = 0
        while l <= r:
            # IF THE LEFT MAXIMUM IS < RIGHT MAXIMUM
            if left_max < right_max:
                # WE CAN BE CERTAIN ABOUT THAT IT IS LEFT MAXIMUM WALL LIMITING THE LEFT POINTER
                # CALCULATE WATER AT LEFT
                water += max(0, left_max-height[l])
                left_max = max(left_max, height[l])
                l += 1 
            else:
            # WE CAN BE CERTAIN ABOUT THAT IT IS RIGHT MAXIMUM WALL LIMITING THE RIGHT POINTER
                # CALCULATE WATER AT 
                water += max(0, right_max-height[r])
                right_max = max(right_max, height[r])
                r -= 1 
        return water            
        
#############################################################
# SLIDING WINDOW
#############################################################
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        t = 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                t = max(t, r-l+1)
            else:
                # MOVE LEFT SO THAT seen no longer has s[r]
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l = l + 1 
        return t
   
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
   
#############################################################
 
class Solution:
    def numDecodings(self, s: str) -> int:
        ans = {}
        def dfs(s):
            if s in ans:
                return ans[s]

            if s[0] == "0":
                ans[s] = 0
                return 0

            if len(s) == 1:
                ans[s] = 1
                return 1

            if len(s) == 2:
                if int(s) % 10 == 0:
                    t =  1 if int(s) in (10,20) else 0
                    ans[s] = t
                    return t

                t = 2 if 11<= int(s) <= 26 else 1
                ans[s] = t
                return t

            
            a = dfs(s[1:]) if int(s[0]) != 0 else 0
            b = dfs(s[2:]) if int(s[:2]) <= 26 else 0
            ans[s] = a + b
            return a + b

        return dfs(s)

#############################################################

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        possible = [0]*(int(half)+1)
        possible[0] = 1

        for i in range(len(nums)):
            for j in range(len(possible)-1, -1, -1):
                if possible[j] == 1 and j+ nums[i] < len(possible):
                    possible[j + nums[i]] = 1

        return possible[-1] == 1

#############################################################
# BACKTRACKING
#############################################################

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):      # BASE CASE
                res.append(subset.copy())
                return
            subset.append(nums[i])  # MAKE THE CHOICE
            dfs(i+1)                # EXPLORE
            subset.pop()            # UNDO
            dfs(i+1)                # EXPLORE WITHOUT THE CHOICE

        dfs(0)
        return res

#############################################################

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        subset = []
        def dfs(t, i):              # i IS NEEDED TO HANDLE DUPLICATES IN RES
            print(t)
            if t < 0:
                return
            if t == 0:              # BASE CASE
                res.append(subset.copy())
                return

            for j in range(i, len(candidates)):
                cd = candidates[j]
                subset.append(cd)   # MAKE THE CHOICE
                dfs(t- cd, j)       # EXPLORE. WITH ONLY CANDIDATES AT AND AFTER j
                subset.pop()        # UNDO THE CHOICE

        dfs(target, 0)
        return res
    
# candidates = [2, 3, 5], target = 5.
# - After choosing 2, you can choose 2, 3, or 5.
# - After choosing 3, you can choose 3 or 5 — not 2 anymore. ALL BH*** BH**** BEFORE THAT IS ALREADY HANDLE IN 2 CASE
# - After choosing 5, you can choose only 5.

#############################################################

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(pos, w, path):
            r, c = pos[0], pos[1]
            
            if board[r][c] != w[0]:
                return False
            
            if len(w) == 1:
                return True

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in path:
                    path.add((nr, nc))
                    if dfs((nr, nc), w[1:], path):
                        return True
                    path.remove((nr, nc))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs((i, j), word, path={(i, j)}):
                        return True
        return False

#############################################################

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()

        def dfs(pos):
            r, c = pos[0], pos[1]
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0<= nc < n and (nr,nc) not in seen and  grid[nr][nc] == "1" :
                    seen.add((nr, nc))
                    dfs((nr, nc))

        ct = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in seen:
                    ct +=1
                    seen.add((i,j))
                    dfs((i,j))
        return ct
    
#############################################################
# TREES
#############################################################

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node): # RETURN MAXIMUM LEFT SUBTREE LENGHT AND RIGHT SUBTREE LENGTH
            nonlocal diameter
            if not node:
                return -1

            # HOW FAR CAN I GO THROUGH THE LEFT SUBTREE 
            left = dfs(node.left)
            right = dfs(node.right)
            
            diameter = max(diameter, left+right+2)

            return 1 + max(left, right)
            
        dfs(root)
        return diameter
    
#############################################################

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = {}
        def dfs(node, l):
            nonlocal ans

            if not node:
                return
            
            ans.setdefault(l,[]).append(node.val)  
            dfs(node.left, 1+l)
            dfs(node.right, 1+l)

        dfs(root, 0)
        return list(ans.values())
#############################################################

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # WE NEED TO SORT OF PASS WHAT VALUES EACH TREE IS ALLOWED TO HAVE

        def dfs(node, maxi, mini):
            if not node:
                return True

            if not node or not (mini < node.val < maxi):
                return False

            return dfs(node.left, node.val, mini) and  dfs(node.right, maxi, node.val)

        return dfs(root,float('inf'),float('-inf'))

#############################################################

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node):
            if not node:
                return (0, None)

            ld, l_lca = dfs(node.left) # DEPTH OF DEEPEST LEFT NODES, ANSWER
            rd, r_lca = dfs(node.right) # DEPTH OF DEEPEST RIGHT NODES, ANSWER

            # AT THE NODE HOW DEEP IS EACH LEFT AND RIGHT SUBTREE?
            # IF EQUAL --> CURRENT NODE IS THE THE ANSWER
            # IF LEFT/RIGHT IF DEEPER ANSWER IS THE DFS(NODE)
            
            if ld == rd:
                return (ld + 1, node)
            elif (ld > rd):
                return (ld + 1, l_lca)
            else:
                return (rd + 1, r_lca)

        return dfs(root)[1]
    
#############################################################
# HEAPS
#############################################################
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [] # O(N)
        heapq.heapify(heap)
        for i in range(len(nums)): # O(N)
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                if nums[i] > heap[0]:
                    heapq.heappop(heap) # O(logK)
                    heapq.heappush(heap, nums[i])
        return heap[0]
    
    # ABOVE IS THE GENERAL PATTERN FOR K LARGEST. WE KEEP ONLY TOP K ELEMENTS WITH MIN HEAP. 

#############################################################
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x, y = point
            dist = (x**2 + y**2) ** 0.5
            if len(heap) < k:
                heapq.heappush(heap, [-dist, point])
            else:
                if -dist > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-dist, point])
                    
        return [pt for d, pt in heap]
    # ABOVE IS THE GENERAL PATTERN FOR K SMALLEST. WE KEEP ONLY SMALLEST K ELEMENTS WITH MIN HEAP AND NEGATIVE TRICK.
    
        
#############################################################
# GRAPHS
#############################################################

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set() # ADD TO SEEN WHILE ENQUEUEING THE NODE
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(0,1), (0,-1), (1,0),(-1,0)]
        minutes = 0
        while q and fresh:
            for _ in range(len(q)): 
                # ONE CAN DO WITHOUT THIS, BUT THIS TRICK IS TO SKIP TRACKING LEVELS
                # THIS IS LIKE ADD FIRST BFS LEVEL PROCESS IT COMPLETELY. THEN PROCESS NEXT. 
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        seen.add((nr,nc))

            minutes += 1
        return minutes if fresh == 0 else -1

#############################################################

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m,n  = len(heights), len(heights[0])

        A = [[0]*n for _ in range(m)]
        P = [[0]*n for _ in range(m)]

        A[-1]= [1]*n
        P[0] = [1]*n

        for i in range(m):
            P[i][0] = 1
            A[i][-1] = 1

        p_seen = set()
        a_seen = set()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(node, M, seen):
            r, c = node
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                    M[nr][nc] = 1
                    seen.add((nr, nc))
                    dfs((nr,nc), M, seen)
                    
        for i in range(m):
            for j in range(n):
                if P[i][j] == 1:
                    p_seen.add((i,j))
                    dfs((i,j), P, p_seen)

                if A[i][j] == 1:
                    a_seen.add((i,j))
                    dfs((i,j), A, a_seen)        
        both = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and P[i][j] == 1:
                    both.append([i,j])
        return both
    
#############################################################

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        d = {i: [] for i in range(numCourses)} # STORES WHICH COURSES ARE DEPENDENT OF A COURSE
        p = {i: set() for i in range(numCourses)} 
        for pr in prerequisites:
            ai, bi = pr
            d[bi].append(ai)
            p[ai].add(bi)

        dq = deque()
        seen = set()
        for course in p:
            if not p[course]:
                dq.append(course)
                seen.add(course)

        # HERE dq STORES ALL COURSES THAT HAVE NO PREREQ
        while dq:
            c = dq.popleft()
            for dp in d[c]: # ALL COURSES WHERE THAT COURSE WAS NEEDED
                p[dp].remove(c)
                if not p[dp] and dp not in seen:
                    dq.append(dp)
                    seen.add(dp)
                    
        for j in p:
            if p[j]:
                return False
        return True

#############################################################

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n  = len(isConnected)
        seen = set()
        provinces = 0
        for i in range(n):
            if i in seen:
                continue
            provinces +=1
            q = deque([i])
            while q:
                node = q.popleft()
                for j in range(n):
                    if isConnected[node][j] == 1 and j not in seen:
                        q.append(j)
                        seen.add(j)        
        return provinces 
    
#############################################################


#############################################################
# TRIES
#############################################################





#############################################################
# PREFIX SUM
#############################################################

# PREFIX_SUM[i] INCLUDES THE ELEMENT AT i
# pre[i] - pre[j] = SUM OF SUBARRAY ENDING AT i AND BEGIN AT j+

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        out = 0
        cur = 0
        
        for num in nums:
            cur = cur + num                     # CURRENT PREFIX SUM
            out = out + seen.get(cur-k, 0) 
            seen[cur] = seen.get(cur, 0) + 1    # .GET IS SUITS BETTER FOR COUNTS AND FOR ARRAY ETC:
                                                # .setdefault("x", []).append(2) IF x not in DICT SET IT [] AND THEN APPEND 2 ELSE JUST APPEND 2. 
        return out