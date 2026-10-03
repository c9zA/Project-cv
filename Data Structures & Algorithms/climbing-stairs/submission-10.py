class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        def dfs(n):
            if n==1:
                dp[n-1]=1
            if n==2:
                dp[n-1]=2
            if dp[n-1]==0:
                dp[n-1]=dfs(n-1)+dfs(n-2)
            return dp[n-1]
        dfs(n)
        return dp[n-1]