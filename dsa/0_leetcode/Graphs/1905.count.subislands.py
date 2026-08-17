from collections import deque
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # SEARCH VALID ISLANDS ON GRID 2. MAKE SURE THAT EACH CELL ADDED TO THE ISLAND IS 1 ON GRID 1.
        m, n = len(grid1), len(grid1[0])
        visited = set()
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]
        
        def dfs(node):
            island = set()
            q = deque()
            q.append(node)
            visited.add(node)
            rr = 1
            while q:
                r, c = q.popleft()
                island.add((r,c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        
                        if grid2[nr][nc] == 1 and (nr, nc) not in visited:
                            if grid1[nr][nc] == 0:
                                rr = 0
                            q.append((nr, nc))
                            visited.add((nr,nc))
            return rr
        
        count= 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 1 and (i,j) not in visited:
                    count = count  + dfs((i,j))
        return count