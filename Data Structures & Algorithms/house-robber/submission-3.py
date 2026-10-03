class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]
        if n>1:
            dp[1] = max(nums[0], nums[1])
        def dfs(i):
            if i<2:
                return dp[i]
            if dp[i]<0:
                dp[i] = max(dfs(i-2)+nums[i], dfs(i-1))
            return dp[i]
        return dfs(n-1)