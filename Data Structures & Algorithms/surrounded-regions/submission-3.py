class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rct = len(board)
        cct = len(board[0])
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        allseen = set()
        def bfs(q,seen):
            modify=True
            while q:
                oldr, oldc = q.popleft()
                for dr, dc in direction:
                    nr, nc = dr+oldr, dc+oldc
                    if -1<nr<rct and -1<nc<cct and (nr, nc) not in allseen and board[nr][nc]=='O':
                        if nr==0 or nr==rct-1 or nc==0 or nc==cct-1:
                            modify=False
                            allseen.add((nr, nc))
                        else:
                            q.append((nr,nc))
                            seen.add((nr,nc))
                            allseen.add((nr,nc))
            if modify:
                for r, c in seen:
                    board[r][c]='X'

        for r in range(1,rct-1):
            for c in range(1,cct-1):
                if (r,c) not in allseen and board[r][c]=='O':
                    allseen.add((r,c))
                    bfs(deque([(r,c)]), set([(r,c)]))