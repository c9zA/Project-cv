class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tlset = set([(0,0)])
        brset = set([(n-1,n-1)])
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        timeMap = {}
        time = max(grid[0][0], grid[-1][-1])
        if time==n**2-1:
            return time
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                timeMap[grid[i][j]] = (i,j)
        qu = deque([(0,0)])
        grid[0][0] = -1
        def bfs(q, addSet, other):
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if -1<nr<n and -1<nc<n and grid[nr][nc]!=-1 and grid[nr][nc]<=time:
                        addSet.add((nr,nc))
                        grid[nr][nc] = -1
                        q.append((nr,nc))
                        if (nr,nc) in other:
                            return True
            return False
        if bfs(qu, tlset, brset):
            return time
        qu.append((n-1, n-1))
        grid[-1][-1] = -1
        bfs(qu, brset, tlset)
        time += 1
        while time<n**2-1:
            r,c = timeMap[time]
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if -1<nr<n and -1<nc<n and grid[nr][nc]==-1:
                    grid[r][c]=-1
                    if (nr, nc) in tlset:
                        tlset.add((r,c))
                    else:
                        brset.add((r,c))
                    if (r,c) in tlset and (r,c) in brset:
                        return time
            if grid[r][c]==-1:
                qu.append((r,c))
            while qu:
                i,j = qu.popleft()
                for di, dj in directions:
                    ni, nj = di+i, dj+j
                    if -1<ni<n and -1<nj<n and grid[ni][nj]<=time and grid[ni][nj]!=-1:
                        grid[ni][nj]=-1
                        if (i, j) in tlset:
                            tlset.add((ni,nj))
                        else:
                            brset.add((ni,nj))
                        if (ni,nj) in tlset and (ni,nj) in brset:
                            return time
                        qu.append((ni,nj))
            time+=1
        return time