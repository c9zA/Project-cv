class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp = [float('inf')]*amount
        for val in coins:
            if val-1<amount:
                dp[val-1] = 1
        for i in range(amount):
            if dp[i]!=float('inf'):
                continue
            for val in coins:
                if i-val>-1 and dp[i-val]!=float('inf'):
                    dp[i] = min(dp[i], dp[i-val]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
