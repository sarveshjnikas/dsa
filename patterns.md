# LeetCode Patterns — Interview Revision

> One file. Every major pattern, when to use it, and concrete Python code.

---

## Table of Contents

1. [Arrays & Hashing](#1-arrays--hashing)
2. [Two Pointers](#2-two-pointers)
3. [Sliding Window](#3-sliding-window)
4. [Prefix Sum](#4-prefix-sum)
5. [Binary Search](#5-binary-search)
6. [Linked List](#6-linked-list)
7. [Stacks & Intervals](#7-stacks--intervals)
8. [Trees](#8-trees)
9. [Graphs](#9-graphs)
10. [Heaps](#10-heaps)
11. [Backtracking](#11-backtracking)
12. [Dynamic Programming](#12-dynamic-programming)
13. [Greedy](#13-greedy)
14. [Bit Manipulation](#14-bit-manipulation)
15. [Strings](#15-strings)
16. [Python Cheatsheet](#16-python-cheatsheet)

---

## 1. Arrays & Hashing

### When to use
- Need O(1) lookup / count / dedup
- "Two sum", frequency count, grouping, detecting duplicates
- Any time brute force is O(n²) and you want O(n)

### Pattern: frequency map

```python
# Count occurrences
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)   # {3:3, 2:2, 1:1}
count[3]                # 3
count.most_common(2)    # [(3,3), (2,2)]

# Manual
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
```

### Pattern: two sum (hash map)

```python
def two_sum(nums, target):
    seen = {}  # value → index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
```

### Pattern: group anagrams

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))   # "eat" → ('a','e','t')
        groups[key].append(s)
    return list(groups.values())
```

### Pattern: detect duplicate

```python
def has_duplicate(nums):
    return len(nums) != len(set(nums))
```

### Pattern: top K frequent

```python
def top_k_frequent(nums, k):
    count = Counter(nums)
    return [x for x, _ in count.most_common(k)]

# Or bucket sort O(n):
def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
```

**Time:** O(n) | **Space:** O(n)

---

## 2. Two Pointers

### When to use
- Sorted array, find pair/triplet with a target sum
- In-place operations (remove duplicates, reverse)
- One pointer from each end, or both moving same direction

### Pattern: opposite ends (sorted array)

```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
```

### Pattern: three sum

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:  # skip duplicates
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return result
```

### Pattern: remove duplicates in-place

```python
def remove_duplicates(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return l
```

### Pattern: container with most water

```python
def max_area(heights):
    l, r = 0, len(heights) - 1
    max_water = 0
    while l < r:
        water = min(heights[l], heights[r]) * (r - l)
        max_water = max(max_water, water)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_water
```

**Time:** O(n) | **Space:** O(1)

---

## 3. Sliding Window

### When to use
- Subarray / substring problem with a constraint (max, min, exactly k, at most k)
- "Longest/shortest window that satisfies X"
- Contiguous elements

### Fixed window size

```python
# Max sum of subarray of size k
def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]  # slide: add right, remove left
        best = max(best, window)
    return best
```

### Variable window — expand/shrink

```python
# Longest substring without repeating characters
def length_of_longest_substring(s):
    seen = set()
    l = 0
    best = 0
    for r in range(len(s)):
        while s[r] in seen:       # shrink until valid
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        best = max(best, r - l + 1)
    return best
```

### Variable window with count

```python
# Longest repeating character replacement (at most k replacements)
def character_replacement(s, k):
    count = {}
    l = 0
    max_freq = 0
    best = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(max_freq, count[s[r]])
        # window size - most frequent char = chars to replace
        if (r - l + 1) - max_freq > k:
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
```

### Template

```python
l = 0
for r in range(len(s)):
    # 1. expand: add s[r] to window state

    while <window is invalid>:
        # 2. shrink: remove s[l] from window state
        l += 1

    # 3. update answer with current valid window (r - l + 1)
```

**Time:** O(n) | **Space:** O(1) or O(k)

---

## 4. Prefix Sum

### When to use
- Range sum queries: "sum of elements from index i to j"
- Subarray sum equals k
- 2D grid sum queries

### Build prefix sum

```python
nums = [1, 2, 3, 4, 5]
prefix = [0] * (len(nums) + 1)
for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]
# prefix = [0, 1, 3, 6, 10, 15]

# Sum from i to j (inclusive):
def range_sum(i, j):
    return prefix[j+1] - prefix[i]
```

### Subarray sum equals k

```python
def subarray_sum(nums, k):
    # prefix_sum → how many times seen
    count = {0: 1}   # empty prefix
    total = 0
    prefix = 0
    for n in nums:
        prefix += n
        # if (prefix - k) was seen before, there's a subarray summing to k
        total += count.get(prefix - k, 0)
        count[prefix] = count.get(prefix, 0) + 1
    return total
```

**Time:** O(n) | **Space:** O(n)

---

## 5. Binary Search

### When to use
- Sorted array, find target in O(log n)
- "Search in rotated array", find boundary
- Answer is monotonic — "find minimum X such that condition holds"

### Standard binary search

```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

### Find leftmost / rightmost position

```python
def search_range(nums, target):
    def find_left():
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                idx = mid
                r = mid - 1   # keep going left
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return idx

    def find_right():
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                idx = mid
                l = mid + 1   # keep going right
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return idx

    return [find_left(), find_right()]
```

### Search in rotated sorted array

```python
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        # left half is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # right half is sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
```

### Binary search on answer (most powerful form)

```python
# "Find minimum capacity such that you can ship all packages in D days"
def ship_within_days(weights, days):
    def can_ship(capacity):
        trips, load = 1, 0
        for w in weights:
            if load + w > capacity:
                trips += 1
                load = 0
            load += w
        return trips <= days

    l, r = max(weights), sum(weights)
    while l < r:
        mid = (l + r) // 2
        if can_ship(mid):
            r = mid       # try smaller
        else:
            l = mid + 1   # need more
    return l
```

**Template for "minimum X where condition holds":**
```python
l, r = min_possible, max_possible
while l < r:
    mid = (l + r) // 2
    if condition(mid):
        r = mid
    else:
        l = mid + 1
return l
```

**Time:** O(log n)

---

## 6. Linked List

### When to use
- In-place reversal, cycle detection, merge, find middle
- Almost always: two pointers (slow/fast)

### Reverse a linked list

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

### Find middle (slow/fast pointers)

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # slow is at middle
```

### Detect cycle

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Find cycle start

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # move one pointer to head, advance both one step at a time
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

### Merge two sorted lists

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

### Reverse k-group / in-groups

```python
def reverse_k_group(head, k):
    # count k nodes
    count, node = 0, head
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return head
    # reverse k nodes
    prev, curr = None, head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head.next = reverse_k_group(curr, k)
    return prev
```

**Time:** O(n) | **Space:** O(1)

---

## 7. Stacks & Intervals

### Stack: when to use
- "Next greater/smaller element"
- Matching brackets / valid parentheses
- Evaluate expressions
- Monotonic stack: maintain increasing or decreasing order

### Valid parentheses

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in mapping:
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return not stack
```

### Monotonic stack — next greater element

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # stores indices, decreasing values
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            idx = stack.pop()
            result[idx] = n
        stack.append(i)
    return result
```

### Largest rectangle in histogram

```python
def largest_rectangle(heights):
    stack = []  # (index, height) — monotonic increasing
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))
    return max_area
```

### Intervals: when to use
- Merge overlapping intervals
- Meeting rooms (can attend all? min rooms needed?)
- Always sort by start time first

### Merge intervals

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:           # overlaps
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Meeting rooms II (minimum rooms)

```python
import heapq

def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []  # end times of ongoing meetings
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)  # reuse room
        else:
            heapq.heappush(heap, end)     # new room
    return len(heap)
```

---

## 8. Trees

### When to use
- DFS (preorder/inorder/postorder) for path problems, structure checks
- BFS (level order) for shortest path, level-by-level problems
- Most tree problems = recursion with return values

### DFS templates

```python
# Recursive DFS
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)

# Max depth
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Path sum
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))
```

### BFS — level order

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):   # process entire level
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

### Validate BST

```python
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if not (lo < root.val < hi):
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))
```

### Lowest Common Ancestor

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left  = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root   # p and q are on different sides
    return left or right
```

### Diameter of tree

```python
def diameter(root):
    best = [0]
    def depth(node):
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        best[0] = max(best[0], l + r)
        return 1 + max(l, r)
    depth(root)
    return best[0]
```

### Inorder iterative (common pattern)

```python
def inorder(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
```

---

## 9. Graphs

### When to use
- Connected components, islands
- Shortest path (BFS = unweighted, Dijkstra = weighted)
- Cycle detection, topological sort
- Always need visited set to avoid infinite loops

### DFS — iterative and recursive

```python
# Recursive
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterative
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### BFS — shortest path (unweighted)

```python
from collections import deque

def bfs(graph, start, end):
    visited = {start}
    queue = deque([(start, 0)])  # (node, distance)
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1
```

### Number of islands (grid DFS)

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'   # mark visited by sinking
        dfs(r+1, c); dfs(r-1, c)
        dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

### Topological sort (DFS)

```python
def topo_sort(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    cycle = set()
    order = []

    def dfs(node):
        if node in cycle:   return False  # cycle detected
        if node in visited: return True
        cycle.add(node)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        cycle.remove(node)
        visited.add(node)
        order.append(node)
        return True

    for i in range(n):
        if not dfs(i):
            return []   # cycle exists
    return order[::-1]
```

### Topological sort (Kahn's BFS — in-degree)

```python
from collections import deque

def topo_sort_kahn(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == n else []  # [] means cycle
```

### Dijkstra (weighted shortest path)

```python
import heapq

def dijkstra(graph, start):
    # graph[u] = [(weight, v), ...]
    dist = {start: 0}
    heap = [(0, start)]   # (cost, node)
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist.get(node, float('inf')):
            continue
        for weight, neighbor in graph[node]:
            new_cost = cost + weight
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist
```

### Union Find (Disjoint Set)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

# Use: detect cycle, number of connected components
```

---

## 10. Heaps

### When to use
- K largest / K smallest elements
- Continuously get min or max as elements are added
- Merge K sorted lists
- Top K frequent

### Min heap basics (Python's heapq is min heap by default)

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappop(heap)    # 1 — always pops minimum
heap[0]                # peek min without popping

# Max heap — negate values
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# Build from list
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)    # O(n)
```

### K largest elements

```python
def k_largest(nums, k):
    # min heap of size k — anything smaller than heap[0] is not top k
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap

# Or simply:
import heapq
heapq.nlargest(k, nums)   # O(n log k)
```

### K smallest

```python
heapq.nsmallest(k, nums)  # O(n log k)
```

### Kth largest element

```python
def find_kth_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

### Merge K sorted lists

```python
def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = curr = ListNode(0)
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

### Median from data stream

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (lower half) — store negated
        self.large = []  # min heap (upper half)

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        # ensure small's max <= large's min
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

---

## 11. Backtracking

### When to use
- Generate all combinations / permutations / subsets
- Constraint satisfaction (N-queens, Sudoku)
- "All possible ways to..."
- Key: choose → explore → unchoose

### Template

```python
def backtrack(state, choices):
    if is_solution(state):
        result.append(state[:])  # add copy
        return
    for choice in choices:
        if is_valid(choice, state):
            state.append(choice)        # choose
            backtrack(state, next_choices)
            state.pop()                 # unchoose
```

### Subsets

```python
def subsets(nums):
    result = []
    def backtrack(start, curr):
        result.append(curr[:])
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return result
```

### Combinations

```python
def combine(n, k):
    result = []
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(1, [])
    return result
```

### Permutations

```python
def permutations(nums):
    result = []
    def backtrack(curr, remaining):
        if not remaining:
            result.append(curr[:])
            return
        for i in range(len(remaining)):
            curr.append(remaining[i])
            backtrack(curr, remaining[:i] + remaining[i+1:])
            curr.pop()
    backtrack([], nums)
    return result
```

### Combination sum (reuse allowed)

```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, curr, remaining):
        if remaining == 0:
            result.append(curr[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            curr.append(candidates[i])
            backtrack(i, curr, remaining - candidates[i])  # i not i+1 (reuse)
            curr.pop()
    backtrack(0, [], target)
    return result
```

### Word search (grid backtracking)

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        temp = board[r][c]
        board[r][c] = '#'   # mark visited
        found = (backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or
                 backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1))
        board[r][c] = temp  # unmark
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False
```

---

## 12. Dynamic Programming

### When to use
- Optimal substructure: solution built from subproblem solutions
- Overlapping subproblems: same subproblem solved multiple times
- "Max/min/count ways/is it possible"
- Keywords: "number of ways", "maximum profit", "minimum cost", "can you reach"

### Two approaches

```
Top-down (memoization): recursive + cache results
Bottom-up (tabulation): fill table iteratively

Both have same complexity. Bottom-up usually has less overhead.
```

### 1D DP — Climbing Stairs

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space optimized:
def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```

### 1D DP — House Robber

```python
def rob(nums):
    if not nums:
        return 0
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1
```

### 2D DP — Unique Paths

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
```

### 0/1 Knapsack

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]   # don't take item i
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[n][capacity]
```

### Coin Change (min coins)

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

### Longest Common Subsequence

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### Longest Increasing Subsequence

```python
def lis(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# O(n log n) with binary search:
import bisect
def lis(nums):
    sub = []
    for n in nums:
        pos = bisect.bisect_left(sub, n)
        if pos == len(sub):
            sub.append(n)
        else:
            sub[pos] = n
    return len(sub)
```

### Word Break

```python
def word_break(s, wordDict):
    words = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]
```

### DP decision framework

```
1. Define dp[i] or dp[i][j] clearly
2. Find recurrence relation
3. Base cases
4. Fill order (ensure dependencies are computed first)
5. Answer is usually dp[n] or max(dp)
```

---

## 13. Greedy

### When to use
- Local optimal choice leads to global optimum
- Scheduling, intervals, jumps
- When you can prove: always take the best available option now
- If greedy seems wrong → try DP

### Jump Game

```python
def can_jump(nums):
    max_reach = 0
    for i, n in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + n)
    return True
```

### Jump Game II (minimum jumps)

```python
def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```

### Gas Station

```python
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start
```

### Partition Labels

```python
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result
```

---

## 14. Bit Manipulation

### When to use
- "Single number" (XOR)
- Count bits, check power of 2
- Subsets using bitmask
- Space-efficient flags

### Core operations

```python
n = 0b1010   # 10

n & 1        # check last bit (0 or 1) — is odd?
n >> 1       # right shift (divide by 2)
n << 1       # left shift  (multiply by 2)
n & (n-1)    # clear lowest set bit
n ^ n        # 0 — XOR with self
a ^ b ^ a    # b — XOR cancels pairs

# Check if bit i is set:
(n >> i) & 1

# Set bit i:
n | (1 << i)

# Clear bit i:
n & ~(1 << i)
```

### Single Number (XOR)

```python
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n   # duplicates cancel out, single remains
    return result
```

### Count set bits (Hamming weight)

```python
def hamming_weight(n):
    count = 0
    while n:
        n &= (n - 1)   # clears lowest set bit
        count += 1
    return count
```

### Power of two

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
    # power of 2 has exactly one set bit
    # n-1 flips all bits below it → AND = 0
```

### Generate all subsets with bitmask

```python
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):   # 0 to 2^n - 1
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result
```

### Reverse bits

```python
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

---

## 15. Strings

### When to use
- Palindrome checks
- Anagram / character frequency
- Pattern matching, parsing
- Most string problems → two pointers or sliding window

### Check palindrome

```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1; r -= 1
    return True

# Alphanumeric only:
def is_palindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    return s == s[::-1]
```

### Longest palindromic substring (expand around center)

```python
def longest_palindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    best = ""
    for i in range(len(s)):
        odd  = expand(i, i)      # odd length
        even = expand(i, i + 1)  # even length
        best = max(best, odd, even, key=len)
    return best
```

### Anagram check

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
    # or: sorted(s) == sorted(t)
```

### String to integer (atoi)

```python
def my_atoi(s):
    s = s.lstrip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] in '+-':
        sign = -1 if s[0] == '-' else 1
        i = 1
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    result *= sign
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    return max(INT_MIN, min(INT_MAX, result))
```

### Encode / Decode strings

```python
def encode(strs):
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    result, i = [], 0
    while i < len(s):
        j = s.index('#', i)
        length = int(s[i:j])
        result.append(s[j+1:j+1+length])
        i = j + 1 + length
    return result
```

---

## 16. Python Cheatsheet

### Data structures

```python
# List
nums = [1, 2, 3]
nums.append(4)         # O(1)
nums.pop()             # O(1) — last
nums.pop(0)            # O(n) — first, use deque for this
nums.insert(0, x)      # O(n)
nums.sort()            # O(n log n) in-place
sorted(nums)           # returns new list
nums[::-1]             # reverse copy
nums.index(val)        # first occurrence

# Deque (double-ended queue) — O(1) both ends
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.popleft()
dq.append(4)
dq.pop()

# Dict
d = {}
d.get(key, default)
d.setdefault(key, []).append(val)

from collections import defaultdict
d = defaultdict(list)     # d[missing_key] → []
d = defaultdict(int)      # d[missing_key] → 0

from collections import Counter
c = Counter([1,1,2,3])    # {1:2, 2:1, 3:1}
c.most_common(2)           # [(1,2), (2,1)]

# Set
s = set()
s.add(x)
s.remove(x)
x in s                    # O(1)
s1 & s2                   # intersection
s1 | s2                   # union
s1 - s2                   # difference

# Heap (min heap)
import heapq
h = []
heapq.heappush(h, val)
heapq.heappop(h)           # smallest
h[0]                       # peek
heapq.heapify(list)        # O(n)
heapq.nlargest(k, iterable)
heapq.nsmallest(k, iterable)
```

### Useful one-liners

```python
# Infinity
float('inf')
float('-inf')

# Swap
a, b = b, a

# Integer division
7 // 2    # 3
-7 // 2   # -4 ← floors toward negative infinity

# Modulo
-1 % 5    # 4  ← always positive in Python

# String
s.split()                  # split on whitespace
' '.join(list)
s.strip()
s.isdigit() / s.isalpha() / s.isalnum()
ord('a')   # 97
chr(97)    # 'a'
ord(c) - ord('a')  # 0-25 index

# List comprehension
[x*2 for x in nums if x > 0]

# Enumerate
for i, val in enumerate(nums):

# Zip
for a, b in zip(list1, list2):

# Sort by key
intervals.sort(key=lambda x: x[0])
words.sort(key=lambda w: len(w))

# Max/min with key
max(nums, key=abs)

# Binary search
import bisect
bisect.bisect_left(arr, x)   # leftmost position to insert x
bisect.bisect_right(arr, x)  # rightmost position
bisect.insort(arr, x)        # insert and keep sorted
```

### Complexity quick reference

| Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Array/List | O(1) | O(n) | O(n) | O(n) |
| HashMap | - | O(1) | O(1) | O(1) |
| Set | - | O(1) | O(1) | O(1) |
| Heap | O(1) min | O(n) | O(log n) | O(log n) |
| Sorted array | O(1) | O(log n) | O(n) | O(n) |

### Recognizing the pattern

| Signal in problem | Pattern |
|---|---|
| Sorted array, find target | Binary search |
| Pair/triplet with target sum | Two pointers |
| Subarray / substring constraint | Sliding window |
| Range sum queries | Prefix sum |
| K largest / smallest | Heap |
| All combinations / permutations | Backtracking |
| Max/min/count ways, overlapping subproblems | DP |
| Local optimal = global optimal | Greedy |
| Islands, connected components, shortest path | Graph BFS/DFS |
| Next greater element, matching brackets | Stack |
| Duplicates, frequency count | HashMap / Set |
| Pairs that cancel out | XOR / Bit manipulation |

---

*Patterns internalized = interview confidence. Good luck.*
