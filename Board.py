from Shapes.Dot import Dot
from Shapes.Line import Line
from Shapes.Box import Box
from Utils.constants import *

class Board():
    def __init__(self, width):
        self.w = width
        a = (DOT_BOX_RATIO*(self.w + 1) + self.w)
        b = (DISPLAY_WIDTH//a)*a
        self.origin = ((DISPLAY_WIDTH - b)//2,
            (DISPLAY_WIDTH - b)//2 + MENU_HEIGHT)
        self.menu_origin = (self.origin[0], self.origin[0])
        self.dot_width = int((DOT_BOX_RATIO/a)*b)
        self.box_width = int((b/a))
        self.board = self.new_board(width)

    @property
    def width(self):
        return self.w
    @width.setter
    def width(self, value):
        """
        if width is set: reinitializes the board with new width
        """
        self.__init__(value)

    def __str__(self):
        """
        returns string representation of board, appropriate for terminal output
        """
        stboard = ""
        for row in self.board:
            strow = str(row[0])
            for c in row[1:]:
                strow += " " + str(c)
            stboard += strow + "\n"
        stboard = stboard[:-1]
        return stboard

    # the following magic functions make class Board act as the list board
    def __len__(self):
        return self.board.__len__()

    def __getitem__(self,key):
        return self.board.__getitem__(key)

    def __iter__(self):
        return self.board.__iter__()
    def draw(self,display):
        """
        draws the board to pygame display
        """
        pos = self.origin
        for row in self:
            for i, o in enumerate(row):
                display.fill(o.color, rect=[pos[0], pos[1], o.width, o.height])
                if i == len(row)-1:
                    pos = (self.origin[0], pos[1]+o.height)
                else:
                    pos = (pos[0]+o.width, pos[1])

    def get_object_at_pos(self,pos):
        """
        returns object situated at postion (r,c)
        """
        c_pos = self.origin # current position in iteration
        for row in self:
            for i, o in enumerate(row):
                if (c_pos[0] <= pos[0] and pos[0] < c_pos[0] + o.width and
                c_pos[1] <= pos[1] and pos[1] < c_pos[1] + o.height): # pos is in obj
                    return o
                if i == len(row)-1:
                    c_pos = (self.origin[0], c_pos[1]+o.height)
                else:
                    c_pos = (c_pos[0]+o.width, c_pos[1])

    def new_board(self, width):
        """
        returns a board with given width
        """
        board = []
        r = 0
        c = 0
        for a in range(width):
            row1 = []
            row2 = []
            r = 2*a
            for b in range(width):
                c = 2*b
                row1.append(Dot(self, r,c))
                row1.append(Line(self, r,c+1))
                row2.append(Line(self, r+1, c, False)) # False means vertical
                row2.append(Box(self, r+1,c+1))
            c += 2
            row1.append(Dot(self, r,c))
            row2.append(Line(self, r+1, c, False))
            board.append(row1)
            board.append(row2)
        row = []
        r += 2
        for i in range(width):
            c = 2*i
            row.append(Dot(self, r,c))
            row.append(Line(self, r,c+1))
        row.append(Dot(self, r,c+2))
        board.append(row)
        return board

    def reset(self):
        """
        initializes with current width
        """
        self.__init__(self.width)