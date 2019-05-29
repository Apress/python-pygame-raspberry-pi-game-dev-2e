class AlienStrafe(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x = self.x + 5

    def draw(self):
        print("%d, %d" % (self.x, self.y))

class AlienDiagonal(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x = self.x + 5
        self.y = self.y + 5

    def draw(self):
        print("%d, %d" % (self.x, self.y))

alien1 = AlienStrafe()
alien2 = AlienDiagonal()

alien1.update()
alien1.update()

alien2.update()
alien2.update()

alien1.draw()
alien2.draw()