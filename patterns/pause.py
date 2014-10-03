import random
import cubehelper
import os
import math
import pygame

PAUSE = 4.0

class Pattern(object):
    def init(self):
        self.timer = 0.0    
        return 1.0 / 20

    def tick(self):
        self.cube.clear()
        self.timer += 0.05
        if self.timer >= PAUSE:
            raise StopIteration
