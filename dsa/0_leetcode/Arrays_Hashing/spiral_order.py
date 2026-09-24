class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []
        m, n = len(matrix), len(matrix[0])
        visited = set()
        move = 1
        r = 0
        c = 0
        while len(visited) != m * n:
            if move == 1:
                while (r, c) not in visited and 0 <= r < m and 0 <= c < n:
                    visited.add((r, c))
                    spiral.append(matrix[r][c])
                    c = c + 1
                    
                r = r + 1
                c = c - 1
                move = 2
                
            elif move == 2:
                while (r, c) not in visited and 0 <= r < m and 0 <= c < n:
                    visited.add((r, c))
                    spiral.append(matrix[r][c])
                    r = r + 1
                    
                move = 3
                c = c - 1
                r = r - 1
                
            elif move == 3:
                while (r, c) not in visited and 0 <= r < m and 0 <= c < n:
                    visited.add((r, c))
                    spiral.append(matrix[r][c])
                    c = c - 1 
                move = 4
                c = c + 1 
                r = r - 1

            elif move == 4:
                while (r, c) not in visited and 0 <= r < m and 0 <= c < n:
                    visited.add((r, c))
                    spiral.append(matrix[r][c])
                    r = r - 1
                    
                move = 1
                c = c + 1
                r = r + 1
                
        return spiral