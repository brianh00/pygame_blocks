from game import *


class Player:

    def __init__(self, screen):
        self.player_x = SCREEN_WIDTH / 2
        self.player_y = SCREEN_HEIGHT / 2
        self.player_size = 20
        self.movement_speed = 5
        self.movement_x = 0
        self.movement_y = 0
        self.player_box = None
        self.draw_player(screen)

    def collide_enemies(self, enemy_boxes):
        for enemy in enemy_boxes:
            if self.player_box.colliderect(enemy):
                return True
        return False

    def draw_player(self, screen):
        self.player_box = pygame.draw.rect(screen, 'blue',
                                           [self.player_x, self.player_y, self.player_size, self.player_size])

    def check_pressed(self, pressed):
        if pressed[pygame.K_LEFT]:
            self.movement_x = -self.movement_speed
        if pressed[pygame.K_RIGHT]:
            self.movement_x = self.movement_speed
        if pressed[pygame.K_UP]:
            self.movement_y = -self.movement_speed
        if pressed[pygame.K_DOWN]:
            self.movement_y = self.movement_speed

    def check_keyup(self, event_key):
        if event_key in [pygame.K_LEFT, pygame.K_RIGHT]:
            self.movement_x = 0
        if event_key in [pygame.K_UP, pygame.K_DOWN]:
            self.movement_y = 0

    def move_player(self):
        self.player_x += self.movement_x
        self.player_y += self.movement_y
        # Handle edges
        if self.player_x <= 0:
            self.player_x = 0
        if self.player_x >= SCREEN_WIDTH - self.player_size:
            self.player_x = SCREEN_WIDTH - self.player_size
        if self.player_y <= 0:
            self.player_y = 0
        if self.player_y >= SCREEN_HEIGHT - self.player_size:
            self.player_y = SCREEN_HEIGHT - self.player_size
