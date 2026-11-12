class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        l, r = 0, len(intervals) - 1
        while l <= r:                      # r = last interval with start <= s
            m = (l + r) >> 1
            if intervals[m][0] <= s:
                l = m + 1
            else:
                r = m - 1

        if r >= 0 and intervals[r][1] >= s:   # overlaps the interval before it
            i = r
            s = intervals[r][0]
            e = max(e, intervals[r][1])
        else:                                  # no overlap: new interval goes at r+1
            i = r + 1

        j = r + 1
        while j < len(intervals) and intervals[j][0] <= e:   # absorb following overlaps
            e = max(e, intervals[j][1])
            j += 1

        return intervals[:i] + [[s, e]] + intervals[j:]