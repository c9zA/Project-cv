class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        hset = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in hset:
                    dp[i] = True
        return dp[-1]