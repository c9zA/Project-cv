class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        b,s,ans = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            currentB,currentS = max(nums[i], nums[i]*b, nums[i]*s),min(nums[i], nums[i]*b, nums[i]*s)
            b,s = currentB, currentS
            ans = max(ans, b)
        return ans