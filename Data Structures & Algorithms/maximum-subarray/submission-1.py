class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        runningSum = 0
        for num in nums:
            if runningSum<0:
                runningSum = num
            else:
                runningSum += num
            ans = max(ans, runningSum)
        return ans