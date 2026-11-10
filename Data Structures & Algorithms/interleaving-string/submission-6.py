class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        for i in range(l1 + 1):
            for k in range(l2 + 1):
                if i > 0 and s1[i-1] == s3[i+k-1]:
                    dp[i][k] |= dp[i-1][k] 
                if k > 0 and s2[k-1] == s3[i+k-1]:
                    dp[i][k] |= dp[i][k-1]
        return dp[l1][l2]