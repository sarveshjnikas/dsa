# we wanna be thinking in terms of considering (i,j) as bottom right corner
# this is DP. so move in direction of slowly building the answer.
# then to check for square matrix of size  sum(matrix((i,j), (i+k, j)][(i+k,j), (i+k,j+k)]) should be k*k

from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        maximal = [[0]*n for _ in range(m)] # this will store the size of the biggest matrix which ends (bottom right) at (i,j)
        
        # handling the base case
        maximal[0] = [int(x) for x in matrix[0]]
        edge = max(maximal[0])
        for i in range(0,m):
            maximal[i][0] = int(matrix[i][0])
            edge = max(edge, maximal[i][0])
        for i in range(1,m):
            for j in range(1,n): # 1 as we already handled first row and column
                if matrix[i][j] == "0":
                    maximal[i][j] = 0
                else:
                    # matrix[i][j] == "1"
                    maximal[i][j] = 1 + min(maximal[i-1][j-1], maximal[i-1][j], maximal[i][j-1])
                    edge = max(edge, maximal[i][j])
                    continue
                
        return edge*edge