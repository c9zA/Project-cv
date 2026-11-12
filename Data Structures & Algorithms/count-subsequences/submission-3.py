class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*(len(t)+1)
        dp[-1] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)):
                if s[i]==t[j]:
                    dp[j]+=dp[j+1]
        return dp[0]