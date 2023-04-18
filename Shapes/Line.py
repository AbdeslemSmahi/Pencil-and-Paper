from Utils.constants import *

class Line():
    def __init__(self, board, row, col, horizontal = True):
        self.board = board
        if horizontal:
            self.is_horizontal = True
            self.width = self.board.box_width
            self.height = self.board.dot_width
        else:
            self.is_horizontal = False
            self.width = self.board.dot_width
            self.height = self.board.box_width
        self.r = row
        self.c = col
        self.filled = False
        self.base_color = LINE_COLOR
    def __str__(self):
        return "Line"
    @property
    def color(self):
        """
        if line is selected: returns global color for line highlighting
        """
        if self.filled:
            return FILLED_LINE_COLOR
        else:
            return self.base_color

    def get_boxes(self):
        """
        returns tuple of the Line's neighbouring boxes if there are any,
        otherwise returns empty tuple
        """
        board = self.board
        out = []
        if self.is_horizontal:
            if self.r != 0: out.append(board[self.r-1][self.c])
            if self.r < len(board)-1: out.append(board[self.r+1][self.c])
        else:
            if self.c != 0: out.append(board[self.r][self.c-1])
            if self.c < len(board)-1: out.append(board[self.r][self.c+1])
        return tuple(out)