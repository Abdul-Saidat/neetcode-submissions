class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val == ".":
                    continue
                if val in seen:
                    return False
                else:
                    seen.add(val)

        for column in range(len(board)):
            seen = set()
            for row in range(len(board)):
                val = board[row][column]
                if val == ".":
                    continue
                if val in seen:
                    return False
                else:
                    seen.add(val)

        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                seen = set()
                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        val = board[row][col]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        else:
                            seen.add(val)
                            
        return True