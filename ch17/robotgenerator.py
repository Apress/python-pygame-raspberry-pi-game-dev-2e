import random
from robotmodel import RobotModel

class RobotGenerator(object):
    def __init__(self, generationTime = 1, maxRobots = 10):
        self.robots = []
        self.generationTime = generationTime
        self.maxRobots = maxRobots
        self.counter = 0

    def getRobots(self):
        return self.robots

    def update(self, deltaTime):
        self.counter += deltaTime

        if self.counter >= self.generationTime and len(self.robots) < self.maxRobots:
            self.counter = 0
            x = random.randint(36, 600)
            y = random.randint(36, 440)
            frame = random.randint(0, 3)
            sx = -50 + random.random() * 100
            sy = -50 + random.random() * 100

            newRobot = RobotModel(x, y, frame, (sx, sy))
            self.robots.append(newRobot)
