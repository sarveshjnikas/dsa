class Solution:
    def countArrangement(self, n: int) -> int:
        # THIS IS BACKTRACKING: ASSIGN, DOES NOT SATISFY, REMOVE. TRY SOMETHING ELSE

        res = 0
        subset = []

        def backtrack(options):
            if len(subset) == n:
                nonlocal res
                res = res + 1
                return

            for idx in range(len(options)):
                i = len(subset) + 1
                num = options[idx]
                if num % i == 0 or i % num == 0:
                    subset.append(options[idx])
                    backtrack(options[:idx] + options[idx + 1 :])
                    subset.pop()

        backtrack([i + 1 for i in range(n)])
        return res


sol = Solution()
sol.countArrangement(2)
