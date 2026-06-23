class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)

                if val == '.':
                    continue
            
                if val in row[r] or val in column[c]:
                    return False
            
                else:
                    row[r].add(val)
                    column[c].add(val)
                
                if val in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(val)
        return True