import pygame
from Utils.constants import *
from Buttons.SquareButton import SquareButton

class Menu():
    side_padding = int((1/5)*DISPLAY_WIDTH)
    button_width = DISPLAY_WIDTH - 2*side_padding
    button_height = int((1/8)*DISPLAY_HEIGHT)
    button_padding = int((1/7)*button_height)
    left_offset = int((1/2)*(DISPLAY_WIDTH - button_width+ side_padding))  
    FONT_SIZE = int((3/10)*button_height)
    FONT_FAMILY = "Arial"
    FONT_COLOR = BLACK
    class MenuButton(SquareButton):
        def __init__(self,x,y,width,height,text,action, parameter, background_color = None,
            border_color = None, font_family = None, font_color = None, font_size = None):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.action = action
            self.action_parameter = parameter
            self.border_width = int((1/9)*self.height)
            if border_color:
                self.border_color = border_color
            else:
                self.border_color = LINE_COLOR
            if background_color:
                self.background_color = background_color
            else:
                self.background_color = BOX_COLOR
            if font_color:
                self.font_color = font_color
            else:
                self.font_color = Menu.FONT_COLOR
            if font_family:
                self.font_family = font_family
            else:
                self.font_family = Menu.FONT_FAMILY
            if font_size:
                self.font_size = font_size
            else:
                self.font_size = Menu.FONT_SIZE
            self.font = pygame.font.SysFont(self.font_family, self.font_size)

        def draw(self, display):
            self.draw_base(display)
            # draw text onto middle of button
            text_surface = self.font.render(self.text, 1, self.font_color)
            rect = text_surface.get_rect()
            x = self.x + int((self.width - rect.width) / 2)
            y = self.y + int((self.height - rect.height) / 2)
            display.blit(text_surface, (x, y))

    def __init__(self, g, menu_items):
        self.g = g
        self.display = g.display
        self.clock = g.clock
        self.menu_items = []
        number_menu_items = len(menu_items)
        pos = [self.side_padding + self.left_offset, int((DISPLAY_HEIGHT-number_menu_items*(self.button_height + self.button_padding-1))/2)] # origin position
        for name, action, parameter in menu_items:
            self.menu_items.append(self.MenuButton(pos[0], pos[1], self.button_width, self.button_height, name, action, parameter))
            pos[1] += self.button_height + self.button_padding
        self.running = False

    def draw(self, display):
        for item in self.menu_items:
            item.draw(display)

    def back(self):
        self.running = False
    def quit_game():
        pygame.quit()
        quit()
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if self.running == False: break
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.back()
                        break
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for item in self.menu_items:
                        if (pos[0] >= item.x and pos[0] <= item.x + item.width
                        and pos[1] >= item.y and pos[1] <= item.y + item.height):
                            if item.action:
                                if item.action_parameter:
                                    item.action(item.action_parameter)
                                else:
                                    item.action()
            self.display.fill(BACKGROUND_COLOR)
            self.draw(self.display)
            pygame.display.update()
            self.clock.tick(30)