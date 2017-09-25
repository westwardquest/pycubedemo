import cubehelper
import random
import math

class Pattern(object):
    def init(self):
        self.iter = 1
        self.delta = 1
        self.sinwidth = 0.4
        self.color = cubehelper.random_color()
        self.prevColor = cubehelper.random_color()
        self.inv = 1
        self.widthincrementor = 0.01
        return 1.0/10

    def tick(self):
        self.cube.clear()
        color = cubehelper.mix_color(self.prevColor, self.color, (math.sin(self.sinwidth*self.iter) + 1 )/2)
        ran = random.randrange(100)

        if ran < 3:
            self.inv = -self.inv
        for x in range(0, self.cube.size):
            for y in range(0, self.cube.size):
                z = math.floor(math.sin(self.sinwidth*(self.iter+(self.inv*(x+y))))*3.5+4)
                self.cube.set_pixel((x, y, z), color)
        self.iter += self.delta
        if (math.sin(self.sinwidth*self.iter)+1)/2 < 0.1:
            self.prevColor = self.color
            self.color = cubehelper.random_color()
