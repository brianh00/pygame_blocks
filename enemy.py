from game import *
import random


class Enemy:
    def __init__(self, speed, size):
        self.enemy_speed = speed
        self.enemy_size = size

    def generate_enemy(self):
        # Returns starting x, y, x movement, y movement
        spawn_location = random.choice(["top", "bottom", "left", "right"])
        if spawn_location == "top":
            return random.randrange(SCREEN_WIDTH), -self.enemy_size, random.randrange(-self.enemy_speed,
                                                                                      self.enemy_speed), random.randrange(
                1,
                self.enemy_speed)
        elif spawn_location == "bottom":
            return random.randrange(SCREEN_WIDTH), SCREEN_HEIGHT, random.randrange(-self.enemy_speed,
                                                                                   self.enemy_speed), random.randrange(
                -self.enemy_speed, -1)
        if spawn_location == "left":
            return -self.enemy_size, random.randrange(SCREEN_HEIGHT), random.randrange(1,
                                                                                       self.enemy_speed), random.randrange(
                -self.enemy_speed,
                self.enemy_speed)
        if spawn_location == "right":
            return random.randrange(SCREEN_HEIGHT), SCREEN_WIDTH, random.randrange(-self.enemy_speed,
                                                                                   self.enemy_speed), random.randrange(
                1, self.enemy_speed)
