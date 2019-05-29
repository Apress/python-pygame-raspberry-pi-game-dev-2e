from robotmodel import RobotModel

class RobotController(object):
    def __init__(self, robots):
        self.robots = robots

    def update(self, deltaTime):
        for robot in self.robots:
            robot.timer += deltaTime
            if robot.getTimer() >= 0.125:
                robot.nextFrame()

            speed = self.multiply(robot.getSpeed(), deltaTime)
            pos = robot.getPosition()

            x, y = self.add(pos, speed)

            sx, sy = robot.getSpeed()

            if x < 0:
                x = 0
                sx *= -1
            elif x > 607:
                x = 607
                sx *= -1

            if y < 0:
                y = 0
                sy *= -1
            elif y > 447:
                y = 447
                sy *= -1

            robot.setPosition((x, y))
            robot.setSpeed((sx, sy))           

    def multiply(self, speed, deltaTime):
        x = speed[0] * deltaTime
        y = speed[1] * deltaTime

        return (x, y)

    def add(self, position, speed):
        x = position[0] + speed[0]
        y = position[1] + speed[1]

        return (x, y)
    