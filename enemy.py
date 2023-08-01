from game import *
import random


class Enemy:
    def __init__(self, speed=3):
        self.enemy_speed = speed

    def generate_enemy(self):
        # Returns starting x, y, x movement, y movement
        spawn_location = random.choice(["top", "bottom", "left", "right"])
        if spawn_location == "top":
            return random.randrange(SCREEN_WIDTH), 0, random.randrange(-self.enemy_speed,
                                                                       self.enemy_speed), random.randrange(
                self.enemy_speed)
        elif spawn_location == "bottom":
            return random.randrange(SCREEN_WIDTH), SCREEN_HEIGHT, random.randrange(-self.enemy_speed,
                                                                                   self.enemy_speed), random.randrange(
                -self.enemy_speed, 0)
        if spawn_location == "left":
            return 0, random.randrange(SCREEN_HEIGHT), random.randrange(self.enemy_speed), random.randrange(
                -self.enemy_speed,
                self.enemy_speed)
        if spawn_location == "right":
            return random.randrange(SCREEN_HEIGHT), SCREEN_WIDTH, random.randrange(-self.enemy_speed,
                                                                                   self.enemy_speed), random.randrange(
                self.enemy_speed)
