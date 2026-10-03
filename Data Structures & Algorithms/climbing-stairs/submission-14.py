class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        def dfs(i):
            if i>=n:
                return i==n
            if dp[i]==0:
                dp[i] = dfs(i+1)+dfs(i+2)
            return dp[i]
        return dfs(0)
