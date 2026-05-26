from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        print(q, fresh)
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        while q and fresh > 0:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] ==1:
                    grid[nr][nc] = 2
                    fresh = fresh -1
                    q.append((nr,nc))
            minutes += 1
        return minutes if fresh == 0  else -1


sol = Solution()
sol.orangesRotting(grid=[[2,1,0],
                         [1,0,0],
                         [0,1,2]
                         ])
