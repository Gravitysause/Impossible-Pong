from time import clock_getres
from Layout import Layout


class Pong(Layout):
    def __init__(self, surface, colour):
        super().__init__(surface, colour, width=int(WIDTH/9), height=int(WIDTH/9))

        self.speed = 5
        self.directionX = -1
        self.directionY = -1

        self.rect.x = int(WIDTH/2)
        self.rect.y = int(HEIGHT/2)

    def draw(self):
        super().draw()

        self.rect.x += self.speed * self.directionX
        self.rect.y += self.speed * self.directionY

    def wallCollision(self):
        if HEIGHT >= self. b
