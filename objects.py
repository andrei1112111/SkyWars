import pygame as pg
import numpy as np
import math


class Player:
    def __init__(self):
        self.pos = np.array([0, 0], dtype=float)
        self.angle = math.pi / 4
        self.height = 270
        self.pitch = 40
        self.angle_vel = 0.005
        self.vel_pos_change = 4
        self.vel_height_change = 2
        self.clock = pg.time.Clock()
        self.acceleration = 20 / 1000
        self.time_ws = 1
        self.time_ad = 0
        self.time_qe = 0

    def update(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        pressed_key = pg.key.get_pressed()
        if pressed_key[pg.K_UP]:
            self.pitch += self.vel_pos_change
        elif pressed_key[pg.K_DOWN]:
            self.pitch -= self.vel_pos_change

        if pressed_key[pg.K_a] and abs(self.time_ad) < 0.006:
            self.time_ad -= self.acceleration * self.angle_vel
        elif pressed_key[pg.K_d] and abs(self.time_ad) < 0.006:
            self.time_ad += self.acceleration * self.angle_vel
        else:
            if self.time_ad < 0 and abs(self.time_ad) > 0.001:
                self.time_ad += self.acceleration * self.angle_vel * 2
            elif self.time_ad > 0 and abs(self.time_ad) > 0.001:
                self.time_ad -= self.acceleration * self.angle_vel * 2
            else:
                self.time_ad = 0

        if pressed_key[pg.K_q] and abs(self.time_qe) < 2:
            self.time_qe += self.acceleration * self.vel_height_change
        elif pressed_key[pg.K_e] and abs(self.time_qe) < 2:
            self.time_qe -= self.acceleration * self.vel_height_change
        else:
            if self.time_qe < 0 and abs(self.time_qe) > 0.001:
                self.time_qe += self.acceleration * self.vel_height_change
            elif self.time_qe > 0 and abs(self.time_qe) > 0.001:
                self.time_qe -= self.acceleration * self.vel_height_change
            else:
                self.time_qe = 0

        if pressed_key[pg.K_w] and self.time_ws < 2:
            self.time_ws += self.acceleration
        elif pressed_key[pg.K_s] and self.time_ws > 1:
            self.time_ws -= self.acceleration

        print(self.time_ad, self.time_ws, self.time_qe)
        self.height += self.time_qe
        self.angle += self.time_ad
        self.pos[0] += self.time_ws * cos_a
        self.pos[1] += self.time_ws * sin_a
