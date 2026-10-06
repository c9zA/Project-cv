class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        hset = set()
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
            hset.add(word)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(max(0,i-maxlen), i):
                if dp[j] and s[j:i] in hset:
                    dp[i] = True
        return dp[-1]