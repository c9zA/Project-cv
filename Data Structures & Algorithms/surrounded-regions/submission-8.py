class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rct, cct = len(board), len(board[0])
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque()
        for r in range(rct):
            if board[r][0]=='O':
                board[r][0] = 'K'
                q.append((r,0))
            if board[r][-1]=='O':
                board[r][-1] = 'K'
                q.append((r, cct-1))
        for c in range(1,cct-1):
            if board[0][c]=='O':
                board[0][c] = 'K'
                q.append((0, c))
            if board[-1][c]=='O':
                board[rct-1][c] = 'K'
                q.append((rct-1, c))
        while q:
            r,c = q.popleft()
            for dr, dc in direction:
                nr, nc = dr+r, dc+c
                if -1<nr<rct and -1<nc<cct and board[nr][nc]=='O':
                    q.append((nr,nc))
                    board[nr][nc] = 'K'
        for r in range(rct):
            for c in range(cct):
                if board[r][c]=='K':
                    board[r][c]='O'
                elif board[r][c]=='O':
                    board[r][c]= 'X'