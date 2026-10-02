class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0
                    q = deque([(i,j)])
                    temp = 1
                    while q:
                        r,c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if -1<nr<len(grid) and -1<nc<len(grid[0]) and grid[nr][nc]==1:
                                grid[nr][nc]=0
                                temp+=1
                                q.append((nr, nc))
                    ans = max(ans, temp)
        return ans