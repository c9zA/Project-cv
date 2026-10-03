class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        def dfs(i):
            if i==0:
                return 1
            if i==1:
                return 2
            if dp[i]==0:
                dp[i] = dfs(i-1)+dfs(i-2)
            return dp[i]
                
        return dfs(n-1)