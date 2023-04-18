from Utils.constants import *
class Dot():
    def __init__(self, board, row, col):
        self.board = board
        self.r = row
        self.c = col
        self.width = self.board.dot_width
        self.height = self.board.dot_width
        self.color = DOT_COLOR
    def __str__(self):
        return "Dot"