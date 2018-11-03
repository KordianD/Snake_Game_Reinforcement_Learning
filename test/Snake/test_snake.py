from src.Snake import Snake


def test_empty_snake_has_zero_length():
    snake = Snake()
    assert snake.length == 0
