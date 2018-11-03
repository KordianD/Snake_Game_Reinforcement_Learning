from src.Position import Position

X_POSITION_VALUE = 100
Y_POSITION_VALUE = 200
X_MOVE_BY = 5
Y_MOVE_BY = 10


def test_construct_position_object_with_passed_values():
    position = Position(X_POSITION_VALUE, Y_POSITION_VALUE)

    assert position.x_position == X_POSITION_VALUE
    assert position.y_position == Y_POSITION_VALUE


def test_should_change_position_when_move_called():
    position = Position(X_POSITION_VALUE, Y_POSITION_VALUE)
    position.move_x(X_MOVE_BY)
    position.move_y(X_MOVE_BY)

    assert position.x_position == X_POSITION_VALUE + X_MOVE_BY
    assert position.y_position == Y_POSITION_VALUE + Y_MOVE_BY
