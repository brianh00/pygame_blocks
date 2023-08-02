import pygame

pygame.init()
pygame.display.set_caption('Blocks')

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60


class Game:
    score_font = pygame.font.Font('freesansbold.ttf', 15)
    font = pygame.font.Font('freesansbold.ttf', 36)
    crash_sound = pygame.mixer.Sound("crash.wav")
    high_score_file = 'high_score.txt'

    def __init__(self, pause=False, screen_display=None, sound=True):
        self.running = True
        self.sound = sound
        self.pause = pause
        self.points = 0
        self.enemy_count = 10
        self.enemy_list = []
        self.enemy_size = 5
        self.high_score = self.get_high_score()
        self.screen = screen_display

    def display_text(self, display_text, text_x, text_y, color='red', display_font=font):
        self.screen.blit(display_font.render(display_text, True, color), (text_x, text_y))

    def display_text_center(self, display_text, text_x_offset, text_y, color='green', display_font=font):
        text = display_font.render(display_text, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2 - text_x_offset, text_y))
        self.screen.blit(text, text_rect)

    def display_info(self):
        if self.pause:
            self.display_text_center("Dodge the Blocks", 0, 60, color='red')
            self.display_text_center("SPACE to start", 0, 200, display_font=self.score_font, color='white')
            if self.sound:
                color = 'green'
            else:
                color = 'red'
            self.display_text_center("S to toggle sound", 0, 230, display_font=self.score_font, color=color)
            self.display_text(f"Points: {self.points}", SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 80, color='white',
                              display_font=self.score_font)
            self.display_text(f"High Score: {self.high_score}", SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 50,
                              color='white', display_font=self.score_font)
            pygame.display.update()
        else:
            self.display_text_center(f"Points: {self.points}", 0, 10, display_font=self.score_font)
            self.display_text_center(f"High Score: {self.high_score}", 0, SCREEN_HEIGHT - 20,
                                     display_font=self.score_font)

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

    def toggle_sound(self):
        self.sound = not self.sound
