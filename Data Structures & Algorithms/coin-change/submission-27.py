class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp = [float('inf')]*(amount+1)
        for val in coins:
            if val<amount+1:
                dp[val] = 1
        for i in range(1,amount+1):
            if dp[i]!=float('inf'):
                continue
            for val in coins:
                if i-val>0 and dp[i-val]!=float('inf'):
                    dp[i] = min(dp[i], dp[i-val]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
