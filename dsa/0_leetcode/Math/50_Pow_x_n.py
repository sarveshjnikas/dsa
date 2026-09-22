class Solution:
    def myPow(self, x: float, n: int) -> float:
        x, n = (1/x, -n) if n < 0 else (x, n)
        res = {0: 1, 1: x} # THIS ONE WITH PREALLOCATED ARRAY FAILS. MEMORY ISSUE. n CAN BE AS HIGH AS 2^31. IMAGINE ARRAY THAT BIG!
        def recurse(n):
            if n in res:
                return res[n]
            else:
                p = recurse(n // 2)
                q = recurse(n % 2)
                v = p * p * q
                res[n] = v
                return v
        recurse(n)
        return res[n]
        
        
sol = Solution()
sol.myPow(x = 2.00000, n = -2)
