class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distance = [float('inf')]*n
        seen = set()
        seen.add(0)
        cur = 0
        distance[0] = 0
        ans = 0
        while len(seen)<n:
            xi, yi = points[cur]
            mn = float('inf')
            for i in range(n):
                if i not in seen:
                    xj,yj = points[i]
                    distance[i] = min(distance[i], abs(xi-xj)+abs(yi-yj))
                    if mn>distance[i]:
                        mn = distance[i]
                        cur = i
            seen.add(cur)
            ans += distance[cur]
        return ans
