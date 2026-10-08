class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        n =len(nums)
        dp = [[0]*(2*sm+1) for _ in range(n)]
        dp[0][nums[0]+sm]+=1
        dp[0][-nums[0]+sm]+=1
        for i in range(1,n):
            for j in range(2*sm+1):
                if dp[i-1][j]>0:
                    if -1<j+nums[i]<len(dp[0]):
                        dp[i][j+nums[i]] += dp[i-1][j]
                    if -1<j-nums[i]<len(dp[0]):
                        dp[i][j-nums[i]] += dp[i-1][j]
        return dp[-1][target+sm] if target+sm<len(dp[0]) else 0