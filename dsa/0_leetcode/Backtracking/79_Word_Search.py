class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        built = []
        def dfs(m, n):
            if M < m or N < n:
                return 
            built.append(board[m][n])
            # built_word = "".join(built)
            
            # if built_word == word:
            #     return True
            
        dfs(0,0)
        return False
        

sol = Solution()

sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
