from Buttons.SquareButton import SquareButton
from Utils.constants import *

class MenuIconButton(SquareButton):
    def draw(self, display):
        self.draw_base(display)
        inner_width = self.width - 2*self.border_width
        inner_origin = (self.x+self.border_width, self.y+self.border_width)
        # draw the three bars
        # inner_width divided into 7ths to create three bars symmetrically
        display.fill(self.design_color,
            rect = [int(inner_origin[0]+(1/7)*inner_width), int(inner_origin[1]+(1/7)*inner_width),
            inner_width-2*self.border_width, int((1/7)*inner_width)])
        display.fill(self.design_color,
            rect = [int(inner_origin[0]+(1/7)*inner_width), int(inner_origin[1]+(3/7)*inner_width),
            inner_width-2*self.border_width, int((1/7)*inner_width)])
        display.fill(self.design_color,
            rect = [int(inner_origin[0]+(1/7)*inner_width), int(inner_origin[1]+(5/7)*inner_width),
            inner_width-2*self.border_width, int((1/7)*inner_width)])