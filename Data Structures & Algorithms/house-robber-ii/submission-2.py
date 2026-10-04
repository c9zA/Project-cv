class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        first = [-1]*n
        second = [-1]*n
        first[0] = nums[0]
        if n==1:
            return nums[0]
        first[1] = max(nums[0], nums[1])
        second[1] = nums[1]
        if n>2:
            second[2] = max(nums[1], nums[2])
        for i in range(2,n-1):
            first[i] = max(first[i-2]+nums[i], first[i-1])
            second[i+1] = max(second[i-1]+nums[i+1], second[i])
        return max(second[-1], first[-2])