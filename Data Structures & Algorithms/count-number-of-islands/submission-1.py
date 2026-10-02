class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        directions = [(0,1), (0,-1), (-1,0),(1,0)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1':
                    ans += 1
                    q = deque([(r,c)])
                    while q:
                        i,j = q.popleft()
                        for di, dj in directions:
                            ni, nj = i+di, j+dj
                            if -1<ni<len(grid) and -1<nj<len(grid[0]) and grid[ni][nj]=='1':
                                grid[ni][nj]='0'
                                q.append((ni,nj))
        return ans