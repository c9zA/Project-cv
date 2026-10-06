class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm%2!=0:
            return False
        dp = [False]*(sm//2+1)
        dp[0] = True
        runningSum = 0
        for num in nums:
            runningSum+=num
            temp = dp[:]
            for i in range(min(len(dp), runningSum+1)):
                if dp[i] and i+num<len(dp):
                    temp[i+num] = True
            dp = temp
            if dp[-1]:
                return True
        return False
        # 1 5 11 3
        #T T F