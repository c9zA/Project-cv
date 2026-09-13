class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rct, cct = len(board), len(board[0])
        q = deque()

        for r in range(rct):
            for c in (0, cct - 1):
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    q.append((r, c))
        for c in range(cct):
            for r in (0, rct - 1):
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if -1 < nr < rct and -1 < nc < cct and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    q.append((nr, nc))

        for r in range(rct):
            for c in range(cct):
                board[r][c] = 'O' if board[r][c] == '#' else 'X'