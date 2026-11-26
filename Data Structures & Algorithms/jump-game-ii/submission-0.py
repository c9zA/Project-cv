class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        idx = 0
        n = len(nums)
        if n==1:
            return 0
        while idx<n:
            ans += 1
            if idx+nums[idx]>=n-1:
                return ans
            temp = 1
            mx = 0
            oldIdx = idx
            while temp<=nums[oldIdx]:
                if nums[oldIdx+temp]+temp>mx:
                    idx = oldIdx+temp
                    mx = nums[idx]+temp
                temp+=1