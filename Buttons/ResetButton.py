from Buttons.SquareButton import SquareButton
from Utils.constants import *

class ResetButton(SquareButton):
    def draw(self, display):
        self.draw_base(display)
        inner_width = self.width - 2*self.border_width
        inner_origin = (self.x+self.border_width, self.y+self.border_width)
        seventh = int((1/7)*inner_width)
        inside_inner = inner_width - 2*seventh # don't worry 'bout it
        arrowhead_width = int((3/14)*inner_width)
        arrowhead_elevation = int((arrowhead_width)/4)-1
        # draw arrow
        display.fill(self.design_color,
            rect=[inner_origin[0]+seventh, inner_origin[1]+3*seventh,
                seventh, inside_inner-2*seventh])
        display.fill(self.design_color,
            rect=[inner_origin[0]+2*seventh, inner_origin[1]+inside_inner,
                inside_inner-2*seventh, seventh])
        display.fill(self.design_color,
            rect=[inner_origin[0]+inside_inner, inner_origin[1]+seventh,
                seventh, inside_inner])
        display.fill(self.design_color,
            rect=[inner_origin[0]+inside_inner-seventh, inner_origin[1]+seventh,
                seventh, seventh])
        # draw arrow head
        height = arrowhead_width
        arrowhead_origin = [inner_origin[0]+inside_inner-seventh-1,
            inner_origin[1]+seventh - arrowhead_elevation]
        for i in range(arrowhead_width):
            display.fill(self.design_color,
                rect = [arrowhead_origin[0], arrowhead_origin[1],
                    1, height])
            arrowhead_origin[0] -= 1
            arrowhead_origin[1] += 1
            height -= 2
