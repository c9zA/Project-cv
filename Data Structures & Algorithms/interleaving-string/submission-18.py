class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        dp = [[False] * (l2 + 1) for _ in range(2)]
        dp[0][0] = True
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i==0 and j==0:
                    continue
                cur = False
                if i>0 and dp[(i-1)%2][j] and s1[i-1]==s3[i+j-1]:
                    cur = True
                if j>0 and dp[i%2][j-1] and s2[j-1]==s3[i+j-1]:
                    cur = True
                dp[i%2][j] = cur
        return dp[l1%2][-1]