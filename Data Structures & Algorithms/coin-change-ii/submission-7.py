class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(amount+1):
                left = dp[j-coins[i]] if j-coins[i]>-1 else 0
                dp[j] += left
        return dp[-1]