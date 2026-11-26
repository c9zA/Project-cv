class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = 1
        n = len(nums)
        for i in range(n-1):
            maxStep -= 1
            maxStep = max(maxStep, nums[i])
            if maxStep==0:
                return False
        return True