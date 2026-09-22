class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # what is the longest palindrome ending at j and starting at i
        n = len(s)
        sol = [[0] * n for _ in range(n)]

        for i in range(n):
            sol[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    sol[i][j] = 2 + sol[i + 1][j - 1]
                else:
                    sol[i][j] = max(sol[i + 1][j], sol[i][j - 1])
        return sol[0][n - 1]


sol = Solution()
sol.longestPalindromeSubseq("bbbab")
