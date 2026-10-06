class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0]*n2 for _ in range(n1)]
        for r in range(n1):
            for c in range(n2):
                top = dp[r-1][c] if -1<r-1 else 0
                left = dp[r][c-1] if -1<c-1 else 0
                diag = dp[r-1][c-1] if -1<r-1 and -1<c-1 else 0
                if text1[r]==text2[c]:
                    dp[r][c] = diag+1
                else:
                    dp[r][c] = max(left, top)
        return dp[-1][-1]