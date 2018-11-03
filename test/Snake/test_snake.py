from src.Snake import Snake

X_POSITION_VALUE = 100
Y_POSITION_VALUE = 200


def test_empty_snake_has_zero_length():
    snake = Snake(X_POSITION_VALUE, Y_POSITION_VALUE)
    assert snake.length == 0
