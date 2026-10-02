class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0,1], [0,-1],[-1,0], [1,0]]
        distance = [[float('inf')]* n for _ in range(n)]
        pq = []
        pq.append((grid[0][0], 0,0))
        distance[0][0] = grid[0][0]
        while pq:
            time, r, c = heapq.heappop(pq)
            if time<=distance[r][c]:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if -1<nr<n and -1<nc<n:
                        temp = max(time, grid[nr][nc])
                        if temp<distance[nr][nc]:
                            heapq.heappush(pq, (temp, nr, nc))
                            distance[nr][nc] = temp
        return distance[-1][-1]