class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rct, cct = len(matrix), len(matrix[0])
        dp = [[0]*cct for _ in range(rct)]
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        def dfs(r, c):
            if dp[r][c]!=0:
                return dp[r][c]
            best = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if -1<nr<rct and -1<nc<cct and matrix[r][c]<matrix[nr][nc]:
                    best = max(best, 1+dfs(nr, nc))
            dp[r][c] = best
            return dp[r][c]
        ans = 0
        for r in range(rct):
            for c in range(cct):
                if dp[r][c]==0:
                    dp[r][c] = dfs(r,c)
                ans = max(ans, dp[r][c])
        return ans