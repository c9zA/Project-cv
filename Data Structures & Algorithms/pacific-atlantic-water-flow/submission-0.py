class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        rct = len(heights)
        cct = len(heights[0])
        possible = [[[-1, -1] for _ in range(cct)] for _ in range(rct)]
        directions = [[0, -1], [-1, 0], [1,0],[0,1]]
        def dfs(r,c,b):
            possible[r][c][b]=2
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if -1<nr<rct and -1<nc<cct and possible[nr][nc][b]!=2 and possible[nr][nc]!=0 and heights[nr][nc]<=heights[r][c]:
                    if possible[nr][nc][b]==-1:
                        possible[nr][nc][b]=2
                        dfs(nr,nc, b)
                    if possible[nr][nc][b]==1:
                        possible[r][c][b]=1
                        break
            if possible[r][c][b]==2:
                possible[r][c][b]=0
        for r in range(rct):
            possible[r][0][0]=1
        for c in range(1, cct):
            possible[0][c][0]=1
        for r in range(1,rct):
            for c in range(1,cct):
                if possible[r][c][0]==-1:
                    dfs(r,c,0)
        for r in range(rct):
            possible[r][cct-1][1]=1
        for c in range(cct-1):
            possible[rct-1][c][1]=1
        for r in range(rct):
            for c in range(cct):
                if possible[r][c][1]==-1:
                    dfs(r,c,1)
        for r in range(rct):
            for c in range(cct):
                if possible[r][c][0]==possible[r][c][1]==1:
                    ans.append([r,c])
        return ans