def move():
    print("move")


def draw():
    print("draw")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(10, 20)
point.x = 11
print(point.x)
