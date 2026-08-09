class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        
        dp = [-1]*(amount+1)
        dp[0] = 0
        
        for amt in range(1,amount+1):
            for coin in coins:
                rem = amt - coin
                if rem >=0 and dp[rem] != -1:
                    dp[amt] = min(dp[amt],dp[rem]+1) if dp[amt] !=-1 else dp[rem]+1
        return dp[amount]