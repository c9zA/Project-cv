class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]
        for num in nums:
            l = 0
            r = len(dp)-1
            while l<=r:
                m = (l+r)>>1
                if dp[m]>=num:
                    r= m-1
                else:
                    l = m+1
            if r+1<len(dp):
                dp[r+1] = num
            else:
                dp.append(num)
        return len(dp)