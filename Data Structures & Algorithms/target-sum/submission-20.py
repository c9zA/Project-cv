class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        dp = [[0]*(sm*2+1) for _ in range(2)]
        row = 1
        dp[0][sm] = 1
        for i in range(len(nums)):
            for j in range(2*sm+1):
                left = dp[row%2-1][j-nums[i]] if -1<j-nums[i]<sm*2+1 else 0
                right = dp[row%2-1][j+nums[i]] if -1<j+nums[i]<sm*2+1 else 0
                dp[row%2][j] = left+right
            row+=1
        return dp[row%2-1][target+sm] if abs(target)<=sm else 0
        # f(idx, target)
        # idx=n and target=0:
        # 1
        # idx=n 
        # 0
        # f(idx+1, target+n[idx])
        # f(idx+1, target-n[idx])
        # dp = len*(sm*2+1)