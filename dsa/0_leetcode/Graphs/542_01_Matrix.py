from typing import List
import math
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        updated = [[float("inf")] * COLS for _ in range(ROWS)]
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    updated[r][c] = 0
                    q.append((r, c))


        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if updated[nr][nc] > updated[r][c] + 1:
                        updated[nr][nc] = updated[r][c] + 1
                        q.append((nr, nc))
                        
        return updated


sol = Solution()
sol.updateMatrix(mat=[[0,1,0],
                      [1,1,0],
                      [1,1,1]])
