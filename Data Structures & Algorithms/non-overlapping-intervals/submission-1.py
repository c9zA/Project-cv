class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        lastEnd = float('-inf')
        ans = 0
        for s, e in intervals:
            if s<lastEnd:
                ans += 1
            else:
                lastEnd = max(lastEnd, e)
        return ans