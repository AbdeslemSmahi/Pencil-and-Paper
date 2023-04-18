from Utils.constants import *

class Box():
    def __init__(self, board, row, col):
        self.board = board
        self.width = self.board.box_width
        self.height = self.board.box_width
        self.r = row
        self.c = col
        self.color = BOX_COLOR
    def __str__(self):
        return "Box"
    def get_lines(self):
        board = self.board
        return (board[self.r-1][self.c], board[self.r][self.c+1], board[self.r+1][self.c], board[self.r][self.c-1])
 