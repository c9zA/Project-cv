class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rct, cct = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = set()

        for sr in range(1, rct - 1):
            for sc in range(1, cct - 1):
                if board[sr][sc] != 'O' or (sr, sc) in seen:
                    continue

                region = [(sr, sc)]          # doubles as the BFS queue
                seen.add((sr, sc))
                safe = False
                i = 0

                while i < len(region):
                    r, c = region[i]
                    i += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if not (-1 < nr < rct and -1 < nc < cct) or board[nr][nc] != 'O':
                            continue
                        if nr in (0, rct - 1) or nc in (0, cct - 1):
                            safe = True
                        elif (nr, nc) not in seen:
                            seen.add((nr, nc))
                            region.append((nr, nc))

                if not safe:
                    for r, c in region:
                        board[r][c] = 'X'