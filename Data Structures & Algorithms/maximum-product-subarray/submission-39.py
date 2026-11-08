class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        p,n = 0,0
        for i in range(len(nums)):
            pos = nums[i] if nums[i]>=0 else None
            neg = nums[i] if nums[i]<=0 else None
            ans = max(ans, nums[i])
            if i>0:
                tempP, tempN = pos,neg
                if tempP and p:
                    pos = max(pos, p*tempP)
                    ans = max(ans, pos)
                if tempN and n:
                    pos = max(pos, tempN*n) if pos else tempN*n
                    ans = max(ans, pos)
                if tempP and n:
                    neg = min(neg, tempP*n) if neg else tempP*n
                    ans = max(ans, neg)
                if tempN and p:
                    neg = min(neg, tempN*p)
                    ans = max(ans, neg)
            p,n = pos, neg
        return ans
       