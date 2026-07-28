class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ways = [[0]*n for _ in range(m)]
        ways[0][0] = 1
       
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] ==1:
                    ways[i][j] = 0
                else:
                    a = ways[i-1][j] if i-1 >= 0 else 0
                    b = ways[i][j-1] if j-1 >= 0 else 0
                    ways[i][j] = ways[i][j]+ a + b
        
        return ways[-1][-1]