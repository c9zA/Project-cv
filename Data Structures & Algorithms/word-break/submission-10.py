class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp=[]
        words=set(wordDict)
        for i in range(n):
            for j in range(20):
                if i-j==0 or (i-j>0 and dp[i-j-1]==True):
                    if s[i-j:i+1] in words:
                        dp.append(True)
                        break
            else:
                dp.append(False)
        return dp[-1]
