import pygame
from Board import Board
from Player import Player
from Buttons.MenuIconButton import MenuIconButton
from Buttons.ResetButton import ResetButton
from Shapes.Line import Line
from Utils.constants import *

class DotsAndBoxes():
    def __init__(self, g, width, main_menu): # g passed for graphics
        self.g = g
        self.main_menu = main_menu
        self.display = g.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = g.clock
        self.players = [Player("Blue", BLUE), Player("Red", RED)]
        self.current_player = self.players[0]
        self.board = Board(width)
        self.upper_menu = [
        MenuIconButton(self.board.menu_origin[0], self.board.menu_origin[1],
            self.board.origin[1]-2*self.board.menu_origin[1], self.quit_to_menu, WHITE),
        ResetButton(DISPLAY_WIDTH-self.board.menu_origin[0]-(self.board.origin[1]-2*self.board.menu_origin[1]), self.board.menu_origin[1],
            self.board.origin[1]-2*self.board.menu_origin[1], self.reset, WHITE)
        ]
        self.highlighted_object = None

    def pos_in_object(self, pos, obj):
        """
        returns if given position is inside borders of object
        -> bool
        """
        if (pos[0] >= obj.x and pos[0] <= obj.x+obj.width
            and pos[1] >= obj.y and pos[1] <= obj.y+obj.height): return True
        else: return False

    def reset(self):
        """
        inisializes with current graphics and width
        """
        self.__init__(self.g, self.board.width)
    def quit_game():
        pygame.quit()
        quit()
    def quit_to_menu(self):
        self.main_menu.run()


    def run(self, width):
        """
        runs menu with user interaction, pygame GUI
        """
        self.__init__(self.g, width, self.main_menu)
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if self.running == False:
                    break
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.board.reset()
                        self.running = False
                        break
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked_object = self.board.get_object_at_pos(pos)
                    if clicked_object:
                        #print("click: (",pos,clicked_object, clicked_object.r, clicked_object.c,")") # DEBUG
                        if type(clicked_object) == Line:
                            # line is filled
                            clicked_object.filled = True
                            # check if box is last line filled
                            boxes = clicked_object.get_boxes()
                            filled_boxes = []
                            for box in boxes:
                                lines = box.get_lines()
                                filled_counter = 0 # how many lines are filled in box
                                for line in lines:
                                    if line.filled: filled_counter += 1
                                if filled_counter == len(lines): filled_boxes.append(box)
                            if filled_boxes: # if any filled boxes
                                # fill boxes with color
                                for box in filled_boxes:
                                    self.current_player.score += 1
                                    box.color = self.current_player.color
                                # check win condition
                                total_score = 0
                                for player in self.players:
                                    total_score += player.score
                                if total_score == self.board.width**2:
                                    # game done
                                    # DEBUG
                                    print("WIN: ( ",end="")
                                    for player in self.players:
                                        box_percentage = (player.score/(self.board.width**2))*100
                                        print(player.score, " (", "%.1f" % box_percentage, " %)", end=" ")
                                    print(")")
                            else:
                                # next player's turn if no boxes filled
                                self.current_player = self.players[(
                                    self.players.index(self.current_player) + 1) % len(self.players)]
                    else:
                        for o in self.upper_menu:
                            if self.pos_in_object(pos,o):
                                if o.action: o.action()
                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    new_highlighted_object = self.board.get_object_at_pos(pos)
                    if new_highlighted_object != self.highlighted_object:
                        if type(self.highlighted_object) == Line:
                            self.highlighted_object.base_color = LINE_COLOR
                        if type(new_highlighted_object) == Line:
                            new_highlighted_object.base_color = self.current_player.color
                        self.highlighted_object = new_highlighted_object


            self.display.fill(BACKGROUND_COLOR)
            self.board.draw(self.display)
            for item in self.upper_menu:
                item.draw(self.display)
            pygame.display.update()
            self.clock.tick(30)