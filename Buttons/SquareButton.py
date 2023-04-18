from Utils.constants import *

class SquareButton():
    rect_design = None
    def __init__(self, x, y, width, action, background_color = None,
        border_color = None, design_color = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.action = action
        self.border_width = int((1/9)*width)
        if border_color:
            self.border_color = border_color
        else:
            self.border_color = BLACK
        if background_color:
            self.background_color = background_color
        if design_color:
            self.design_color = design_color
        else:
            self.design_color = BLACK
    def draw_base(self, display):
        inner_width = self.width-2*self.border_width
        inner_height = self.height-2*self.border_width
        # draw outlines
        display.fill(self.border_color,
            rect=[self.x, self.y, self.width, self.border_width])
        display.fill(self.border_color,
            rect=[self.x, self.y+self.border_width,
            self.border_width, inner_height])
        display.fill(self.border_color,
            rect=[self.x+self.width-self.border_width, self.y+self.border_width,
            self.border_width, inner_height])
        display.fill(self.border_color,
            rect=[self.x, self.y+self.height-self.border_width,
            self.width, self.border_width])
        # draw background
        if self.background_color:
            display.fill(self.background_color,
                rect = [self.x+self.border_width, self.y+self.border_width,
                inner_width, inner_height])
    def draw(self, display):
        self.draw_base(display)