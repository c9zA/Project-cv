class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rct,cct = len(matrix),len(matrix[0])
        dp = [[0]*cct for _ in range(rct)]
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        ans = 0
        def dfs(r,c):
            if dp[r][c]!=0:
                return dp[r][c]
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if -1<nr<rct and -1<nc<cct and matrix[nr][nc]>matrix[r][c]:
                    dp[r][c] = max(dfs(nr,nc)+1, dp[r][c])
            dp[r][c] = 1 if dp[r][c]==0 else dp[r][c]
            return dp[r][c]
        for i in range(rct):
            for j in range(cct):
                ans = max(ans, dfs(i,j))
        return ans
    # 2 3
    # 4 5

    # 0 0 
    # 0 0
    # dfs(0,0)->dfs(1,0)->dfs(1,1)
        
            