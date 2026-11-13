class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        l, r = 0,1
        while l<len(intervals):
            s, e = intervals[l][0], intervals[l][1]
            while r<len(intervals) and intervals[r][0]<=e:
                e = max(e, intervals[r][1])
                r+=1
            l = r
            r+=1
            ans.append([s,e])
        return ans