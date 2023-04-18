import pygame
import random
import string
import time
from Utils.constants import *

class CategoriesGame:
    def __init__(self,g, main_game):
        self.main_game = main_game
        self.graphics = g

        self.font = pygame.font.Font(None, 36)
        pygame.init()

        

        self.categories = ['Boys name', 'Girls name', 'Country', 'Animal', 'Fruit', 'Vegetable']
        self.step = 180
    def compute_scores(self, answers, chosen_letter, round_num):
        score = 0
        print(f"Answers: {answers}, round: {round_num}, letter: {chosen_letter}")
        for index, answer in enumerate(answers):
            if answer[round_num] == '':
                continue
            if answer[round_num][0].lower() != chosen_letter.lower():
                continue
            if answer[round_num].lower() in ANSWERS_LIST[index]:
                score += 1
        print(f"Chosen letter: {chosen_letter}, score: {score}")
        return score
    def draw_categories_and_separators(self):
        x = 50
        for category in self.categories:
            text = self.font.render(category, True, BLACK)
            self.screen.blit(text, (x, 50))
            x += self.step

        for i in range(1, len(self.categories)):
            pygame.draw.line(self.screen, BLACK, (i * self.step + 20, 50), (i * self.step + 20, self.screen_height - 50), 3)

    def run(self):
        self.screen_width, self.screen_height = WIDTH_CAT, HEIGHT_CAT
        self.graphics.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen = self.graphics.display
        pygame.display.set_caption('Categories Game')
        player_scores = [0, 0]
        round_num = 1
        current_player = 0

        input_string = ''
        all_answers = [[[] for _ in self.categories] for _ in range(2)]

        while round_num <= ROUNDS:
            answers = all_answers[current_player]
            chosen_letter = random.choice(string.ascii_uppercase)
            text = self.font.render(f"Round {round_num}: Player {current_player + 1}, your letter is '{chosen_letter}'.", True, BLACK)

            start_time = time.time()
            time_limit = 30  # seconds

            current_category = 0
            while current_category < len(self.categories):
                elapsed_time = time.time() - start_time
                if elapsed_time >= time_limit:
                    break

                remaining_time = time_limit - elapsed_time
                timer_text = self.font.render(f"Time left: {remaining_time:.1f}s", True, BLACK)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            answers[current_category].append(input_string)
                            current_category += 1
                            input_string = ''
                        elif event.key == pygame.K_BACKSPACE:
                            input_string = input_string[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            self.main_game.run()
                        else:
                            input_string += event.unicode

                self.screen.fill(BACKGROUND_COLOR)
                self.draw_categories_and_separators()
                self.screen.blit(text, (50, 10))
                self.screen.blit(timer_text, (800, 10))

                input_surface = self.font.render(input_string, True, BLUE)
                self.screen.blit(input_surface, (50 + current_category * self.step, 100))

                for player in range(2):
                    for i, category_answers in enumerate(all_answers[player]):
                        y = self.step + player * 200
                        for answer in category_answers:
                            answer_text = self.font.render(answer, True, BLACK)
                            self.screen.blit(answer_text, (50 + i * self.step, y))
                            y += 40

                pygame.display.update()
            
            player_scores[current_player] += self.compute_scores(answers, chosen_letter, round_num-1)#sum(len(a) for a in answers)
            current_player = (current_player + 1) % 2

            if current_player == 0:
                round_num += 1

        winner = 0 if player_scores[0] > player_scores[1] else 1
        text = self.font.render(f"Player {winner + 1} wins with {player_scores[winner]} points!", True, BLACK)
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_categories_and_separators()
        self.screen.blit(text, (50, 10))

        for player in range(2):
            for i, category_answers in enumerate(all_answers[player]):
                y = self.step + player * 200
                for answer in category_answers:
                    answer_text = self.font.render(answer, True, BLACK)
                    self.screen.blit(answer_text, (50 + i * self.step, y))
                    y += 40

        pygame.display.update()
        pygame.time.delay(3000)
        self.main_game.run()


