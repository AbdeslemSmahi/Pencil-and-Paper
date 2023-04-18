import pygame
from Utils.constants import *

class TicTacToe:
    def __init__(self, width, height, grid_size, top_offset, g, main_game):
        pygame.init()
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.top_offset = top_offset
        self.graphics = g
        self.main_game = main_game
        

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_turn = 0

    def draw_grid(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, BLACK, (i * self.grid_size, self.top_offset), (i * self.grid_size, self.height), 5)
            pygame.draw.line(self.screen, BLACK, (0, i * self.grid_size + self.top_offset), (self.width, i * self.grid_size + self.top_offset), 5)

    def draw_board(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 'X':
                    pygame.draw.line(self.screen, RED, (x * self.grid_size + self.grid_size // 4, y * self.grid_size + self.grid_size // 4 +self.top_offset), ((x + 1) * self.grid_size - self.grid_size // 4, (y + 1) * self.grid_size - self.grid_size // 4 + self.top_offset ), 5)
                    pygame.draw.line(self.screen, RED, ((x + 1) * self.grid_size - self.grid_size // 4, y * self.grid_size + self.grid_size // 4 + self.top_offset), (x * self.grid_size + self.grid_size // 4, (y + 1) * self.grid_size - self.grid_size // 4 + self.top_offset), 5)
                elif self.board[y][x] == 'O':
                    pygame.draw.circle(self.screen, BLUE, (x * self.grid_size + self.grid_size // 2, y * self.grid_size + self.top_offset + self.grid_size // 2), self.grid_size // 3, 5)

    def make_move(self, x, y):
        if self.board[y][x] == ' ':
            self.board[y][x] = 'X' if self.player_turn == 0 else 'O'
            self.player_turn = (self.player_turn + 1) % 2

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        if ' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]:
            return 'Tie'
        return None
    def render_text(self, text, font_size, color, pos):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, pos)

    def run(self):
        self.screen = self.graphics.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe")
        running = True
        while running:
            self.screen.fill(BACKGROUND_COLOR)
            self.draw_grid()
            self.draw_board()
            pygame.display.update()

            winner = self.check_winner()

            if winner:
                if winner == 'Tie':
                    self.render_text("It's a tie!", 48, BLACK, (self.width // 2 - 75, 10))
                else:
                    self.screen.fill(BACKGROUND_COLOR)
                    self.draw_grid()
                    self.draw_board()
                    self.render_text(f"Player {winner} wins!", 48, BLACK, (self.width // 2 - 100, 10))
                pygame.display.update()
                pygame.time.delay(3000)
                running = False
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x, grid_y = mouse_x // self.grid_size, (mouse_y-self.top_offset) // self.grid_size
                    self.make_move(grid_x, grid_y)
                    
        self.main_game.run()

"""if __name__ == "__main__":
    WIDTH = 600
    HEIGHT = 650
    GRID_SIZE = WIDTH // 3
    TOP_OFFSET = 50

    tic_tac_toe = TicTacToe(WIDTH, HEIGHT, GRID_SIZE,TOP_OFFSET)
    tic_tac_toe.game_loop()
"""