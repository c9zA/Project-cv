class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = -prices[0]
        no = 0
        cool = 0
        ans = 0
        for i in range(1,n):
            nh = max(no-prices[i], hold)
            nn = max(no, cool)
            nc = hold+prices[i]
            ans = max(nh, nn, nc)
            hold, no, cool = nh, nn, nc
        return ans