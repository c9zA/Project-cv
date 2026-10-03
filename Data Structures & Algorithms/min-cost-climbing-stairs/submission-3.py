class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        def dfs(i):
            if i<2:
                return 0
            if dp[i]<0:
                dp[i] = min(cost[i-1]+dfs(i-1),cost[i-2]+dfs(i-2))
            return dp[i]
        return dfs(n)