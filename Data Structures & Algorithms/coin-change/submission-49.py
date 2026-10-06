class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        def dfs(i):
            if dp[i]!=float('inf'):
                return dp[i]
            for c in coins:
                if i>=c:
                    prev = dfs(i-c)
                    if prev!=float('inf') and prev!=-1:
                        dp[i] = min(dp[i], prev+1)
            if dp[i]==float('inf'):
                dp[i] = -1
            return dp[i]
        ans = dfs(amount)
        return ans