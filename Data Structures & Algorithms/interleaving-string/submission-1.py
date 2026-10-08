class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1,n2,n3 = len(s1), len(s2), len(s3)
        if n3!=n1+n2:
            return False
        part1, part2 = 0,0
        dp = [[False]*(1+n2) for _ in range(1+n1)]
        dp[0][0] = True
        for i in range(n1+1):
            for j in range(n2+1):
                top = dp[i-1][j] if 0<i else False
                left = dp[i][j-1] if 0<j else False
                if top and s1[i-1]==s3[i+j-1]:
                    dp[i][j]=True
                elif left and s2[j-1]==s3[i+j-1]:
                    dp[i][j]=True
        return dp[-1][-1]