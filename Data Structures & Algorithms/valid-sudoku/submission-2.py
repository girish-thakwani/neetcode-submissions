class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            s=set()
            for j in range(0,9):
                if board[i][j]!='.':
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])

        for i in range(0,9):
            s=set()
            for j in range(0,9):
                if board[j][i]!='.':    
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])

        for i in range(0,9):
            s=set()
            for j in range(0,3):
                for k in range(0,3):
                    r=(i//3)*3+j
                    c=(i%3)*3+k
                    if board[r][c]!='.':
                        if board[r][c] in s:
                            return False
                        s.add(board[r][c])
                    
        return True
