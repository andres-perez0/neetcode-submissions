class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        number   = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        offset = 0
        box = 0
        box_base = 0
        for i in range(81):
            # for every 9 counts it changes rows
            # for every 3 counts it changes boxes
            # for every count it changes columns
            if i != 0 and i % 27 == 0:
                offset += 3
                box_base = 0
            elif i != 0 and i % 9 == 0:
                box_base -= 2
            elif i != 0 and i % 3 == 0:
                box_base += 1

            box = box_base + offset

            row = int(i / 9)
            col = i % 9
            
            if board[row][col] in number:
                print(board[row][col])
                if board[row][col] in row_sets[row]:
                    return False
                else: 
                    row_sets[row].add(board[row][col])
                
                if board[row][col] in col_sets[col]:
                    return False
                else: 
                    col_sets[col].add(board[row][col])

                if board[row][col] in box_sets[box]:
                    return False
                else: 
                    box_sets[box].add(board[row][col])

            print(f"i: {i} row: {row} col: {col} box: {box}")

        return True