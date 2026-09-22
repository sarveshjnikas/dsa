from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # IF WE START FROM i AND j element of s1 and s2, due to interleaving, s3[:k = i + j] can we make remaining s3

        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            k = i + j

            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j):
                return True

            if j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1):
                return True

            return False

        return dfs(0, 0)


sol = Solution()
sol.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
