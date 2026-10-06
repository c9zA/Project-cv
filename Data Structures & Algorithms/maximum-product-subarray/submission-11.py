class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(min(0,nums[0]), max(0, nums[0]))]
        ans = dp[0][1] if dp[0][1]!=0 else dp[0][0]
        for i in range(1,n):
            pp, pn = dp[i-1][1], dp[i-1][0]
            dp.append((min(0, pp*nums[i], pn*nums[i], nums[i]), max(0, pp*nums[i], pn*nums[i], nums[i])))
            ans = max(ans, dp[i][1] if dp[i][1]!=0 else dp[i][0])
        return ans