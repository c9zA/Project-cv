class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rct = len(grid)
        cct = len(grid[0])
        q = deque()
        directions = [(0,1), (0, -1), (-1,0),(1,0)]
        for r in range(rct):
            for c in range(cct):
                if grid[r][c]==0:
                    q.append((0,r,c))
        while q:
            dist, r,c = q.popleft()
            if grid[r][c]<dist:
                continue
            for dr, dc in directions:
                nr, nc = dr+r,dc+c
                if -1<nr<rct and -1<nc<cct and grid[nr][nc]>0 and grid[nr][nc]>dist+1:
                    grid[nr][nc]=dist+1
                    q.append((dist+1, nr, nc))