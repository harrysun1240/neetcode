class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row = set(board[r])
            blank = 0
            for c in range(9):
                if board[r][c] == ".":
                    blank += 1
            if len(row) != 10 - blank:
                return False

        for c in range(9):
            col = set()
            blank = 0
            for r in range(9):
                if board[r][c] == ".":
                    blank += 1
                col.add(board[r][c])
            if len(col) != 10 - blank:
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = set()
                blank = 0
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] == ".":
                            blank += 1
                        box.add(board[r + i][c + j])
                if len(box) != 10 - blank:
                    return False

        return True
