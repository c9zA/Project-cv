class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        idx = 0
        while idx<n:
            if s[idx] == '0':
                return 0
            if 1+idx<n and s[1+idx]=='0':
                if int(s[idx:idx+2])<27:
                    dp[idx+1] = dp[idx-1] if idx>0 else 1
                    dp[idx] = dp[idx+1]
                else:
                    return 0
                idx += 1
            else:
                if idx>0:
                    dp[idx] = dp[idx-1]
                    if int(s[idx-1:idx+1])<27 and s[idx-1]!='0':
                        dp[idx] += dp[idx-2] if idx>1 else 1
                else:
                    dp[idx] = 1
            idx += 1
        return dp[-1]