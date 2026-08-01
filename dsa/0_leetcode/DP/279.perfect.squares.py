class Solution:
    def numSquares(self, n: int) -> int:
        ans = [0]*(n+1)
        ans[0] = 0
        for i in range(1, n+1):
            min_i = float('inf')
            for j in range(1,int(i**0.5)+1):
                min_i = min(min_i, ans[i-j*j]+1)
            ans[i] = min_i
        print(ans)
        return ans[-1]