from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        p = [[0]*n for _ in range(m)]
        a = [[0]*n for _ in range(m)]
        
        for c in range(n):
            p[0][c] =1
            a[-1][c] =1
            
        for r in range(m):
            p[r][0] = 1
            a[r][-1] = 1
          
        pq = deque()   
        aq = deque()  
        p_visit = set()  
        a_visit = set()    
        for i in range(m):
            for j in range(n):
                if p[i][j] == 1:
                    pq.append((i,j))
                    p_visit.add((i,j))
                    
                if a[i][j] == 1:
                    aq.append((i,j))
                    a_visit.add((i,j))
                    
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while pq:
            r, c = pq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<= nr< m and 0 <= nc <n and heights[nr][nc] >= heights[r][c] and (nr,nc) not in p_visit:
                    p[nr][nc] = 1
                    p_visit.add((nr,nc))
                    pq.append((nr,nc))
                
        while aq:
            r, c = aq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<= nr< m and 0 <= nc <n and heights[nr][nc] >= heights[r][c] and (nr,nc) not in a_visit:
                    a[nr][nc] = 1
                    a_visit.add((nr,nc))
                    aq.append((nr,nc))
            
        result = []
        for i in range(m):
            for j in range(n):
                if p[i][j] == 1 and a[i][j] ==1:
                    result.append((i,j))
    
        return result
        
        
sol = Solution()
sol.pacificAtlantic( heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])