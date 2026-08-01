# initially thought greedy: that at any row there are nine subcases and 
# trying to maximise total point picked by both would eventually lead to the optimal answer
# but a local optimal choice might lead us on a path that is not globally optimal. 
# points you currently choose will affect future points. so no greedy. 
# it would be like the dungeon problem. so we start from the last row,
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        c1 = 0 # robot 1 init position
        c2 = n-1 # robot 2 init position
        points = [[[0]*n for _ in range(n)] for _ in range(m)] # points[r][c1][c2] stores maximum cherries collectible from row r to final row finish when robot1 is at c1 and robot2 is at c2
        # for the last row:
        for i1 in range(n):
            for i2 in range(n):
                points[m-1][i1][i2] = grid[-1][i1] + (grid[-1][i2] if i1 != i2 else 0)
                
        for row in range(m-2, -1, -1):
            for i1 in range(n):
                for i2 in range(n):
                    # next set of possibilities
                    # r1 -> i1+1,i1-1,i1
                    # r2 -> i2+1,i2-1,i2
                    for rr1 in (-1,0,1):
                        for rr2 in (-1,0,1):
                            r1_next = i1 + rr1
                            r2_next = i2 + rr2
                            if r1_next < 0 or r1_next > n-1 or r2_next < 0 or r2_next > n-1:
                                continue
                            
                            points[row][i1][i2] = max(points[row][i1][i2],
                                grid[row][i1] + (grid[row][i2] if i1 != i2 else 0) + points[row+1][r1_next][r2_next]
                            )
                        
        return points[0][0][n-1]
        