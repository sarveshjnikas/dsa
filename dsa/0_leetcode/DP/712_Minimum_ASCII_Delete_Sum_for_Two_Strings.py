class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # d[i][j] = what is the BIGGEST ascii sum if we consider first i,j characters of s1,s2 respectively
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ts1 = sum([ord(c) for c in s1])
        ts2 = sum([ord(c) for c in s2])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (
                    s1[i - 1] == s2[j - 1]
                ):  # consider d[1][1] means take one chars of s1 and s2 but they are at 0,0!
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return ts1 + ts2 - 2 * dp[m][n]


sol = Solution()
sol.minimumDeleteSum(s1="sea", s2="eat")
