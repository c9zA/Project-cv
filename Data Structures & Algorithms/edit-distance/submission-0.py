class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n2,n1 = len(word2),len(word1)
        dp = [[-1]*n2 for _ in range(n1)]
        def dfs(i,j):
            if i==n1 and j==n2:
                return 0
            if i==n1:
                return n2-j
            if j==n2:
                return n1-i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=dfs(i+1,j+1)
            else:
                dp[i][j]=min(dfs(i,j+1),dfs(i+1,j+1),dfs(i+1,j))+1
            return dp[i][j]
        return dfs(0,0)