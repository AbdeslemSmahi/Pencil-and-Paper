import pygame
from Graphics import Graphics
from Utils.constants import *
from DotsAndBoxes import DotsAndBoxes
from Menu import Menu
from CategoriesGame import CategoriesGame
from TicTacToe import TicTacToe
from Battleships import Battleships

class MainGame:
    def __init__(self):
        self.g = Graphics(DISPLAY_DIMENSIONS)

    def quit_game(self):
        pygame.quit()
        quit()

    def run(self):
        self.g.display = pygame.display.set_mode(DISPLAY_DIMENSIONS)
        self.mp = DotsAndBoxes(self.g, BOARD_WIDTH, self)
        game_menu = Menu(self.g, (
            ("Small", self.mp.run, 3),
            ("Medium", self.mp.run, 5),
            ("Large", self.mp.run, 7),
            ("Back", lambda: None, None)
        ))
        game_menu.menu_items[-1].action = game_menu.back

        menu = Menu(self.g, (
            ("Dots and Boxes", game_menu.run, None),
            ("Categories Game", CategoriesGame(self.g, self).run, None),
            ("Tic Tac Toe",TicTacToe(WIDTH_TIC, HEIGHT_TIC, GRID_SIZE_TIC, TOP_OFFSET_TIC, self.g, self).run, None),
            ("Battle Ship", Battleships(WIDTH_BTS, HEIGHT_BTS, GRID_SIZE_BTS, TOP_OFFSET_BTS, LEFT_OFFSET_BTS, self.g, self).run, None),
            ("Quit", self.quit_game, None)
        ))
        menu.run()

if __name__ == "__main__":
    game = MainGame()
    game.run()
    pygame.quit()
    quit()
