class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        box_set = set()

        for row in range(9):
            for col in range(9):
                row_item = board[row][col]
                col_item = board[col][row]
                box_item = board[(row // 3) * 3 + col // 3][(row % 3) * 3 + col % 3]
                if row_item != ".":
                    if row_item in row_set:
                        return False
                    else:
                        row_set.add(row_item)
                if col_item != ".":
                    if col_item in col_set:
                        return False
                    else:
                        col_set.add(col_item)
                if box_item != ".":
                    if box_item in box_set:
                        return False
                    else:
                        box_set.add(box_item)
            row_set.clear()
            col_set.clear()
            box_set.clear()
        return True
