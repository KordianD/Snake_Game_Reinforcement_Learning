from src.Position import Position


class Snake:
    def __init__(self, x_position: int, y_position: int):
        self.length = 0
        self.position = Position(x_position, y_position)

    def move_x(self, move_x: int):
        self.position.move_x(move_x)

    def move_y(self, move_y: int):
        self.position.move_y(move_y)
