import pygame

pygame.init()
pygame.display.set_caption('Blocks')

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60


class Game:
    score_font = pygame.font.Font('freesansbold.ttf', 15)
    font = pygame.font.Font('freesansbold.ttf', 20)
    crash_sound = pygame.mixer.Sound("crash.wav")
    high_score_file = 'high_score.txt'

    def __init__(self, pause=False, screen_display=None):
        self.running = True
        self.pause = pause
        self.points = 0
        self.enemy_count = 10
        self.enemy_list = []
        self.enemy_size = 5
        self.high_score = self.get_high_score()
        self.screen = screen_display

    def stop_screen(self, display_text, text_x, text_y):
        self.screen.blit(self.font.render(display_text, True, 'red'), (text_x, text_y))
        pygame.display.update()

    def display_score(self):
        if self.pause:
            self.stop_screen("Dodge the Blocks", 100, 160)
            self.stop_screen(f"Points: {self.points}", 100, 200)
            self.stop_screen(f"High Score: {self.high_score}", 100, 240)
        else:
            text = self.score_font.render(f"Points: {self.points}", True, 'green')
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 10))
            self.screen.blit(text, text_rect)
            text = self.score_font.render(f"High Score: {self.high_score}", True, 'green')
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20))
            self.screen.blit(text, text_rect)

    def get_high_score(self):
        try:
            with open(self.high_score_file, 'r') as f:
                return f.readlines()[0]
        except FileNotFoundError:
            with open(self.high_score_file, 'w') as f:
                f.write('0')
                return 0

    def move_enemies(self):
        new_enemies = []
        for enemy in self.enemy_list:
            new_enemy = (enemy[0] + enemy[2], enemy[1] + enemy[3], enemy[2], enemy[3])
            if 0 < new_enemy[0] < SCREEN_WIDTH and 0 < new_enemy[1] < SCREEN_HEIGHT:
                new_enemies.append(new_enemy)
        self.enemy_list = new_enemies

    def draw_enemies(self, screen):
        enemy_squares = []
        for enemy in self.enemy_list:
            enemy_squares.append(
                pygame.draw.rect(screen, 'red', [enemy[0], enemy[1], self.enemy_size, self.enemy_size]))
        return enemy_squares

    def check_highscore(self):
        if self.points > int(self.high_score):
            self.high_score = self.points
            with open(self.high_score_file, 'w') as f:
                f.write(str(self.high_score))
