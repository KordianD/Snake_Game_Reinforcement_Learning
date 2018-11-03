class Position:
    def __init__(self, x_position: int, y_position: int):
        self.x_position = x_position
        self.y_position = y_position

    def move_x(self, move_x: int):
        self.x_position += move_x

    def move_y(self, move_y: int):
        self.y_position += move_y
