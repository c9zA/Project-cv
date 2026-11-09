class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        target = sm//2
        n = len(nums)
        if 2*target!=sm:
            return False
        dp = [False]*(target+1)
        dp[0]=True
        dp[nums[0]] = True
        for i in range(1,n):
            for j in range(target,-1,-1):
                if j-nums[i]>=0:
                    dp[j] = dp[j-nums[i]] or dp[j]
            if dp[-1]:
                return True
        return dp[-1]