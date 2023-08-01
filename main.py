import time

import pygame
import random



# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
BLACK = (0, 0, 0)
BLUE = (0, 0, 180)
RED = (255, 0, 0)
GREEN = (0, 230, 10)

# Game Init
pygame.init()
timer = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blocks')
font = pygame.font.Font('freesansbold.ttf', 20)
score_font = pygame.font.Font('freesansbold.ttf', 15)
crash_sound = pygame.mixer.Sound("crash.wav")

# Game Variables
running = True
player_x = 200
player_y = 200
player_size = 20
movement_speed = 3
movement_x, movement_y = 0, 0
enemy_speed = 3
enemy_count = 10
enemy_size = 10
enemy_list = []
pause = True
points = 0
with open('high_score.txt', 'r') as f:
    high_score = f.readlines()[0]


def generate_enemy():
    # Returns starting x, y, x movement, y movement
    spawn_location = random.choice(["top", "bottom", "left", "right"])
    if spawn_location == "top":
        return random.randrange(SCREEN_WIDTH), 0, random.randrange(-enemy_speed, enemy_speed), random.randrange(enemy_speed)
    elif spawn_location == "bottom":
        return random.randrange(SCREEN_WIDTH), SCREEN_HEIGHT, random.randrange(-enemy_speed, enemy_speed), random.randrange(-enemy_speed, 0)
    if spawn_location == "left":
        return 0, random.randrange(SCREEN_HEIGHT), random.randrange(enemy_speed), random.randrange(-enemy_speed, enemy_speed)
    if spawn_location == "right":
        return random.randrange(SCREEN_HEIGHT), SCREEN_WIDTH, random.randrange(-enemy_speed, enemy_speed), random.randrange(enemy_speed)

def move_enemies(enemies):
    new_enemies = []
    for enemy in enemies:
        new_enemy = (enemy[0] + enemy[2], enemy[1] + enemy[3], enemy[2], enemy[3])
        if 0 < new_enemy[0] < SCREEN_WIDTH and 0 < new_enemy[1] < SCREEN_HEIGHT:
            new_enemies.append(new_enemy)
    return new_enemies


def draw_enemies(enemies):
    enemy_squares = []
    for enemy in enemies:
        enemy_squares.append(pygame.draw.rect(screen, RED, [enemy[0], enemy[1], enemy_size, enemy_size]))
    return enemy_squares


def collide_enemies(player, enemy_boxes):
    for enemy in enemy_boxes:
        if player.colliderect(enemy):
            return True
    return False

def stop_screen(display_text, text_x, text_y):
    screen.blit(font.render(display_text, True, RED), (text_x, text_y))
    pygame.display.update()

while running:
    timer.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and pause is False:
            if event.key == pygame.K_SPACE:
                movement_x = 0
                movement_y = 0
            if event.key == pygame.K_LEFT:
                movement_x = -movement_speed
            if event.key == pygame.K_RIGHT:
                movement_x = movement_speed
            if event.key == pygame.K_UP:
                movement_y = -movement_speed
            if event.key == pygame.K_DOWN:
                movement_y = movement_speed
        if event.type == pygame.KEYDOWN and pause is True:
            # Restart game
            if event.key == pygame.K_SPACE:
                pause = False
                points = 0
                enemy_list = []
                player_x = 200
                player_y = 200
                movement_x, movement_y = 0, 0
    if pause:
        stop_screen("Dodge the Blocks", 100, 160)
        stop_screen(f"Points: {points}", 100, 200)
        stop_screen(f"High Score: {high_score}", 100, 240)
        time.sleep(1)
        continue
    else:
        text = score_font.render(f"Points: {points}", True, GREEN)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 10))
        screen.blit(text, text_rect)
        text = score_font.render(f"High Score: {high_score}", True, GREEN)
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20))
        screen.blit(text, text_rect)

    player_x += movement_x
    player_y += movement_y

    # Player and Enemy
    player = pygame.draw.rect(screen, BLUE, [player_x, player_y, player_size, player_size])
    if len(enemy_list) < enemy_count:
        enemy_list.append(generate_enemy())
        points += 1
        enemy_size = max(points//5, 3)
    enemy_list = move_enemies(enemy_list)
    enemy_hitboxes = draw_enemies(enemy_list)
    if collide_enemies(player, enemy_hitboxes):
        pause = True
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.stop()
        if points > int(high_score):
            high_score = points
            with open('high_score.txt', 'w') as f:
                f.write(str(high_score))

    # Handle edges
    if player_x <= 0:
        player_x = 0
    if player_x >= SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size
    if player_y <= 0:
        player_y = 0
    if player_y >= SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    pygame.display.update()


pygame.quit()
