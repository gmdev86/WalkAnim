import pygame, sys, glob
from pygame import *
from SpriteStripAnim import SpriteStripAnim

h = 400
w = 800

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()


class player(object):
    def __init__(self):
        self.x = 200
        self.y = 300
        self.anim_speed_init = 10
        self.anim_speed = self.anim_speed_init
        self.anim_walk_down = glob.glob("PDown*.png")
        self.anim_walk_right = glob.glob("PRight*.png")
        self.anim_walk_up = glob.glob("PUp*.png")
        self.anim_walk_left = glob.glob("PLeft*.png")
        self.anim_pos_x = 0
        self.anim_max = 2
        self.img = pygame.image.load(self.anim_walk_down[0])
        self.update(0, 0, "down")

    def update(self, pos_x, pos_y, dir_move):
        if pos_x != 0 and pos_y == 0:
            self.anim_speed -= 1
            if dir_move == "right":
                self.x += pos_x
                if self.anim_speed == 0:
                    self.img = pygame.image.load(self.anim_walk_right[self.anim_pos_x])
                    self.anim_speed = self.anim_speed_init
                    if self.anim_pos_x == self.anim_max:
                        self.anim_pos_x = 0
                    else:
                        self.anim_pos_x += 1
            elif dir_move == "left":
                self.x -= pos_x
                if self.anim_speed == 0:
                    self.img = pygame.image.load(self.anim_walk_left[self.anim_pos_x])
                    self.anim_speed = self.anim_speed_init
                    if self.anim_pos_x == self.anim_max:
                        self.anim_pos_x = 0
                    else:
                        self.anim_pos_x += 1
        elif pos_y != 0 and pos_x == 0:
            self.anim_speed -= 1
            if dir_move == "down":
                self.y += pos_y
                if self.anim_speed == 0:
                    self.img = pygame.image.load(self.anim_walk_down[self.anim_pos_x])
                    self.anim_speed = self.anim_speed_init
                    if self.anim_pos_x == self.anim_max:
                        self.anim_pos_x = 0
                    else:
                        self.anim_pos_x += 1
            elif dir_move == "up":
                self.y -= pos_y
                if self.anim_speed == 0:
                    self.img = pygame.image.load(self.anim_walk_up[self.anim_pos_x])
                    self.anim_speed = self.anim_speed_init
                    if self.anim_pos_x == self.anim_max:
                        self.anim_pos_x = 0
                    else:
                        self.anim_pos_x += 1

        screen.blit(self.img, (self.x, self.y))

player1 = player()
pos_x = 0
pos_y = 0
direction = {
    "UP": "up",
    "DOWN": "down",
    "LEFT": "left",
    "RIGHT": "right"
}

dir_move = ""
pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False

while 1:
    screen.fill((0, 0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
            elif event.key == pygame.K_UP:
                pressed_up = True
            elif event.key == pygame.K_DOWN:
                pressed_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_left = False
            elif event.key == pygame.K_RIGHT:
                pressed_right = False
            elif event.key == pygame.K_UP:
                pressed_up = False
            elif event.key == pygame.K_DOWN:
                pressed_down = False

    if pressed_left:
        pos_x = 1
        pos_y = 0
        dir_move = direction["LEFT"]
    if pressed_right:
        pos_x = 1
        pos_y = 0
        dir_move = direction["RIGHT"]
    if pressed_up:
        pos_x = 0
        pos_y = 1
        dir_move = direction["UP"]
    if pressed_down:
        pos_x = 0
        pos_y = 1
        dir_move = direction["DOWN"]
    if not pressed_left and not pressed_right and not pressed_up and not pressed_down:
        pos_x = 0
        pos_y = 0

    player1.update(pos_x, pos_y, dir_move)

    pygame.display.update()
