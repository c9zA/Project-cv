class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        mn,mx = min(0,nums[0]), max(0, nums[0])
        for i in range(1,n):
            temp = mn
            mn = min(mn*nums[i],mx*nums[i], nums[i])
            mx = max(temp*nums[i],mx*nums[i], nums[i])
            ans = max(ans, mx if mx!=0 else mn)
        return ans