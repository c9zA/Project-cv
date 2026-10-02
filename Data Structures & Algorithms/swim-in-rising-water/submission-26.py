class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==1:
            return 0
        timeSort = []
        for i in range(n):
            for j in range(n):
                timeSort.append(grid[i][j])
        timeSort.sort()
        r = n**2-1
        l = max(grid[0][0], grid[-1][-1])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        def bfs(time):
            q = deque()
            q.append((0,0))
            seen = set()
            seen.add((0,0))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if -1<nr<n and -1<nc<n and (nr, nc) not in seen and grid[nr][nc]<=time:
                        if nr==n-1 and nc==n-1:
                            return True
                        q.append((nr,nc))
                        seen.add((nr, nc))

            return False
        while r>=l:
            m = (r+l)>>1
            time = timeSort[m]
            if not bfs(time):
                l = m+1
            else:
                r = m-1
        return r+1