class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 3 1 5 2 3 4
        # 1 1 2 2 3 4
        # 3
        n = len(nums)
        dp = [nums[0]]
        for i in range(1,n):
            l = 0
            h = len(dp)-1
            while h>=l:
                m= (h+l)>>1
                if dp[m]>=nums[i]:
                    h=m-1
                else:
                    l=m+1
            if l>=len(dp):
                dp.append(nums[i])
            else:
                dp[l] = nums[i]
        return len(dp)