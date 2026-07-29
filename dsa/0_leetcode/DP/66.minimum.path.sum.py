class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dmin = [[float('inf')]*n for _ in range(m)] # will store min distance from [0][0]
        dmin[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                a = dmin[i-1][j] if i-1>=0 else float('inf')
                b = dmin[i][j-1] if j-1>=0 else float('inf')
                dmin[i][j] = min(a+grid[i][j],b+grid[i][j])
        return dmin[-1][-1]