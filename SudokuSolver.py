'''
Python Program to solve sudoku game
created by Weerawong Vonggatunyu (Qu1etboy)
date : 4/7/2022
Solution ideas from : "Python Sudoku Solver - Computerphile" video
'''

class Sudoku :
    def __init__(self, board):
        self.board = board
        self.solved = False 
    
    def printBoard(self):
        for i in range(9):
            for j in range(9):
                if j % 3 == 0:
                    print('| ' + str(self.board[i][j]), end=' ')
                else :
                    print(self.board[i][j], end=' ')
            print('|', end='')
            if (i+1) % 3 == 0: 
                print('\n'+'-'*25)
            else :
                print()
            
    def possible(self, x, y, n):
        '''
        This function check if the position is possible
        to put the number in to the grid or not.
        The number can't be the same in row, column, and sub box
        '''
        # check column
        for i in range(9):
            if self.board[i][x] == n:
                return False
        # check row
        for i in range(9):
            if self.board[y][i] == n:
                return False
        # check sub box
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[y//3 * 3 + i][x//3 * 3 + j] == n:
                    return False 
        
        return True 

    def solve(self):
        '''
        Solving the sudoku using the recursive method.
        1. Find the empty grid in the board (0 mean empty grid)
        2. After that we try to put every number (1-9) if it possible then put it in to the board.
        3. Then we call the function again until we solved it.
        '''
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.board[y][x] = n 
                            self.solve()
                            if self.solved:
                                return
                            self.board[y][x] = 0
                    # The number we guess is wrong so we try again
                    return
        # If it come to here mean we already solved it!
        self.solved = True
        return                 

if __name__ == '__main__':
    board = []

    for _ in range(9):
        board.append([int(i) for i in input().split()])

    sudoku_1 = Sudoku(board)

    # before solved
    print('**Sudoku Board**')
    sudoku_1.printBoard()

    # after solved
    print('**Solved Sudoku Board**')
    sudoku_1.solve()
    sudoku_1.printBoard()


'''
sample testcase

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

'''