class Alien(object):
    def __init__(self, movement):
        self.x = 0
        self.y = 0
        self.movement = movement

    def update(self):
        self.movement.update(self)

    def draw(self):
        print("%d, %d" % (self.x, self.y))

class Strafe(object):
    def update(self, obj):
        obj.x = obj.x + 5

class Diagonal(object):
    def update(self, obj):
        obj.x = obj.x + 5
        obj.y = obj.y + 5

alien1 = Alien(Strafe())
alien2 = Alien(Diagonal())

alien1.update()
alien1.update()

alien2.update()
alien2.update()

alien1.draw()
alien2.draw()
