# i know that this is graph traversal. either dfs or bfs. i have obviously forgotten about them. 
# let's see.
# how do we know when we have started exploring a new island, or are exploring an old one, when do we say that this island is explored? 

from collections import deque
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [
            (0,1),(1,0),(0,-1),(-1,0)
        ]
        seen = set()
        max_area = 0
        def bfs(node):
            nonlocal max_area
            area = 1
            q = deque()
            q.append(node)
            seen.add(node)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc <n and grid[nr][nc]==1 and (nr,nc) not in seen:
                        area += 1
                        q.append((nr,nc))
                        seen.add((nr,nc))
            return area
            
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    max_area = max(max_area, bfs((i,j)))
        return max_area