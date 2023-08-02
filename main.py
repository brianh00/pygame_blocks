from game import *
from player import Player
from enemy import Enemy
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Game(pause=True, screen_display=screen)
playerObj = Player(screen)
timer = pygame.time.Clock()


while game.running:
    timer.tick(FPS)
    screen.fill('black')

    # Event Handling
    pressed = pygame.key.get_pressed()
    if not game.pause:
        playerObj.check_pressed(pressed)
    else:
        if pressed[pygame.K_SPACE]:
            # Restart game
            playerObj = Player(screen)
            game = Game(pause=False, screen_display=screen, sound=game.sound)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            game.toggle_sound()
        if event.type == pygame.KEYUP and game.pause is False:
            playerObj.check_keyup(event.key)

    game.display_info()

    if game.pause:
        continue

    # Generate enemies
    if len(game.enemy_list) < game.enemy_count:
        enemy = Enemy(speed=3)
        game.enemy_list.append(enemy.generate_enemy())
        game.points += 1
        game.enemy_size = max(game.points // 5, 3)
    game.move_enemies()
    enemy_hitboxes = game.draw_enemies(screen)

    # Move Player
    playerObj.move_player()
    playerObj.draw_player(screen)

    pygame.display.flip()

    # Check for collusions
    if playerObj.collide_enemies(enemy_hitboxes):
        if game.sound:
            pygame.mixer.Sound.play(game.crash_sound)
            pygame.mixer.music.stop()
        game.check_highscore()
        game.pause = True

pygame.quit()
