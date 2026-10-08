class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount+1):
                if dp[i]>0 and i+coin<=amount:
                    dp[i+coin]+=dp[i]
        return dp[-1]