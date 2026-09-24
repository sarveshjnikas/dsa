class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        rows, cols =[], []
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        for i, j in zeros:
            if i not in rows:
                matrix[i] =[0]*n
            if j not in cols:
                for row in matrix: row[j] =0
            rows.append(i)
            cols.append(j)
        