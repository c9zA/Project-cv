class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[-1]*n for _ in range(m)]
        
        def dfs(i,j):
            if j==n:
                return 1
            if i==m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] = 0
            if s[i]==t[j]:
                dp[i][j] = dfs(i+1,j+1)
            dp[i][j]+=dfs(i+1,j)
            return dp[i][j]
        return dfs(0,0)

        # ccbba  cba
        # dfs(0,0)

        # 3 -1 -1
        #  3 -1
        # -1 2 1
        # -1 1 1
        # -1 0 1