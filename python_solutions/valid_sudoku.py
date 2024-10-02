class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        square_dict = {}
        for row in range(9):
            row_dict[row] = set()
            for col in range(9):
                n = board[row][col]
                if n == ".":
                    continue

                if n in row_dict[row]:
                    return False
                row_dict[row].add(n)

                if col not in col_dict:
                    col_dict[col] = set()
                if n in col_dict[col]:
                    return False
                col_dict[col].add(n)

                row_square = row//3
                col_square = col//3 
                if (row_square,col_square) not in square_dict:
                    square_dict[(row_square,col_square)] = set()
                if n in square_dict[(row_square,col_square)]:
                    return False
                square_dict[(row_square,col_square)].add(n)
        return True 