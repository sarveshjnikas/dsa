from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        q = deque()
        visited = set()
        directions= [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
            
        for i in range(m):
            for j in range(n):
                if (i == 0 or i ==m-1 or j ==0 or j== n-1) and board[i][j] == "O":
                    q.append((i,j))
                    visited.add((i,j))
                    board[i][j] = "T"              
        while q:
            gr, gc = q.popleft()
            for dr, dc in directions:
                nr, nc = gr+dr, gc+dc
                if 0 <= nr < m and 0<=nc<n and (nr, nc) not in visited and board[nr][nc] =="O":
                    board[nr][nc] = "T"
                    q.append((nr,nc))
                    visited.add((nr,nc))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
                                    