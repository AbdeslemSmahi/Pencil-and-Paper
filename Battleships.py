import pygame
import random
from Utils.constants import *

class Battleships:
    def __init__(self, width, height, grid_size, top_offset, left_offset, g, main_game):
        pygame.init()
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.top_offset = top_offset
        self.left_offset = left_offset
        self.graphics = g
        self.main_game = main_game
       

        self.grid = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = [5, 4, 3, 3, 2]
        self.attempts = 10
        self.hits = 0
        self.screen = self.graphics.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Battleships")
        self.place_ships()

    def draw_grid(self):
        for i in range(11):
            pygame.draw.line(self.screen, BLACK, (i * self.grid_size + self.left_offset, self.top_offset), (i * self.grid_size + self.left_offset, len(self.grid) * self.grid_size + self.top_offset), 1)
            pygame.draw.line(self.screen, BLACK, (self.left_offset, i * self.grid_size + self.top_offset), (len(self.grid) * self.grid_size + self.left_offset, i * self.grid_size + self.top_offset), 1)

    def render_text(self, text, font_size, color, pos):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, pos)

    def place_ships(self):
        for ship_size in self.ships:
            placed = False
            while not placed:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                direction = random.choice(["horizontal", "vertical"])

                if direction == "horizontal" and col + ship_size <= 9:
                    if all(self.grid[row][col + i] == ' ' for i in range(ship_size)):
                        for i in range(ship_size):
                            self.grid[row][col + i] = 'S'
                        placed = True
                elif direction == "vertical" and row + ship_size <= 9:
                    if all(self.grid[row + i][col] == ' ' for i in range(ship_size)):
                        for i in range(ship_size):
                            self.grid[row + i][col] = 'S'
                        placed = True

    def run(self):
        running = True
        while running:
            self.screen.fill(BACKGROUND_COLOR)    
            self.draw_grid()
            self.render_text(f"Attempts remaining: {self.attempts}", 24, BLACK, (self.width // 2 - 100, self.top_offset - 50))
            for row in range(10):
                for col in range(10):
                    if self.grid[row][col] == 'X':
                        pygame.draw.rect(self.screen, GREEN, (col * self.grid_size + self.left_offset + 1, row * self.grid_size + self.top_offset + 1, self.grid_size - 2, self.grid_size - 2))
                    elif self.grid[row][col] == 'O':
                        pygame.draw.rect(self.screen, RED, (col * self.grid_size + self.left_offset + 1, row * self.grid_size + self.top_offset + 1, self.grid_size - 2, self.grid_size - 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    row = (y - self.top_offset) // self.grid_size
                    col = (x - self.left_offset) // self.grid_size

                    if 0 <= row < 10 and 0 <= col < 10 and self.grid[row][col] !='X' and self.grid[row][col] != 'O':
                        if self.grid[row][col] == 'S':
                            self.grid[row][col] = 'X'
                            self.hits += 1
                            color = GREEN # Green
                        else:
                            self.grid[row][col] = 'O'
                            color = RED # Red
                            self.attempts -= 1
                        pygame.draw.rect(self.screen, color, (col * self.grid_size + self.left_offset + 1, row * self.grid_size + self.top_offset + 1, self.grid_size - 2, self.grid_size - 2))
                        
                
            if self.hits == sum(self.ships):
                self.render_text("You won!", 36, BLUE, (self.width // 2 - 50, self.top_offset // 2))
                pygame.display.update()
                pygame.time.delay(3000)
                running = False

            if self.attempts == 0:
                self.render_text("Game Over", 36, BLUE, (self.width // 2 - 50, self.height - self.top_offset // 2))
                pygame.display.update()
                pygame.time.delay(3000)
                running = False

        self.main_game.run()

