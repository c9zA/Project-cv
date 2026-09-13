class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        rct = len(heights)
        cct = len(heights[0])
        possible = [[[-1, -1] for _ in range(cct)] for _ in range(rct)]
        directions = [[0, -1], [-1, 0], [1,0],[0,1]]
        def dfs(r,c,b):
            if b==1:
                if possible[r][c][0]==1:
                    ans.append([r,c])
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if -1<nr<rct and -1<nc<cct and possible[nr][nc][b]==-1 and heights[nr][nc]>=heights[r][c]:
                    possible[nr][nc][b]=1
                    dfs(nr,nc, b)
        for r in range(rct):
            if possible[r][0][0]==-1:
                possible[r][0][0]=1
                dfs(r, 0, 0)
        for c in range(cct):
            if possible[0][c][0]==-1:
                possible[0][c][0]=1
                dfs(0,c,0)
        for r in range(rct):
            if possible[r][cct-1][1]==-1:
                possible[r][cct-1][1]=1
                dfs(r, cct-1, 1)
        for c in range(cct-1):
            if possible[rct-1][c][1]==-1:
                possible[rct-1][c][1]=1
                dfs(rct-1,c,1)
        return ans
