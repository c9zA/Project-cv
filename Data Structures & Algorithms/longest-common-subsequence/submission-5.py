class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # crabt cat
        # 0 0 0 0 0 0
        # 0 1 1 1 1 1
        # 0 1 1 1 1 2
        # 0 1 1 1 2 2
        l1,l2 = len(text1),len(text2)
        dp = [[0]*(l2+1) for _ in range(2)]
        rowIdx = 1
        for i in range(l1):
            for j in range(l2):
                if text1[i]==text2[j]:
                    dp[rowIdx%2][j+1] = dp[rowIdx%2-1][j]+1
                else:
                    dp[rowIdx%2][j+1] = max(dp[rowIdx%2-1][j+1],dp[rowIdx%2][j])
            rowIdx+=1
        return dp[(rowIdx-1)%2][-1]