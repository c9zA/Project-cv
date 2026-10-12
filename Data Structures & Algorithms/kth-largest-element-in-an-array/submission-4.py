class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums)-1, k)
    
    def median(self, nums, st, end):
        m = (st+end)>>1
        if nums[m]>nums[st] and nums[m]>nums[end]:
            return m
        elif nums[st]>nums[m] and nums[st]>nums[end]:
            return st
        else:
            return end

    def select(self, nums, st, end, k):
        pivot = (st+end)>>1
        if end-st>2:
            pivot = self.median(nums, st, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        l, r = st, end
        while l<r:
            if nums[l]<=nums[end]:
                l+=1
            elif nums[r]>=nums[end]:
                r-=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
        nums[r], nums[end] = nums[end], nums[r]
        if r+k==len(nums):
            return nums[r]
        if len(nums)-k>r:
            return self.select(nums, r+1, end, k)
        else:
            return self.select(nums, st, r-1, k)
