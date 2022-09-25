from bulls_cows import compare_numbers, Game
import pytest

data_for_test_simple = [
    ((1234, 6789),(0, 0)),
    ((1234, 5671),(0, 1)),
    ((6789, 7238),(0, 2)),
    ((6789, 1678),(0, 3)),
    ((6789, 9678),(0, 4)),
    ((1234, 5278),(1, 0)),
    ((1234, 1527),(1, 1)),
    ((4257, 7154),(1, 2)),
    ((9347, 4379),(1, 3)),
    ((7596, 3526),(2, 0)),
    ((8321, 8271),(2, 1)),
    ((3659, 3956),(2, 2)),
    ((3590, 3570),(3, 0)),
    ((6532, 6532),(4, 0))
]


@pytest.mark.parametrize("test_input,expected", data_for_test_simple)
def test_compare_simple(test_input, expected):
    """
    Checks if the compare_numbers function returns expected numbers
    :return:
    """
    assert compare_numbers(*test_input) == expected

"""
TODO:
1. Test consistency of results 
"""


def test_check_user_input_4digit():
    """
    Checks if ValueError is raised when guess is not a 4-digit number
    :return:
    """
    game = Game()
    for n in range(0, 1000):
        with pytest.raises(ValueError):
            game.check_user_input(n)
    for n in range(10000, 100000):
        with pytest.raises(ValueError):
            game.check_user_input(n)
    for p in range(5, 10):
        with pytest.raises(ValueError):
            game.check_user_input(10**p)


def test_check_user_input_repeated_digits():
    """
    Checks if ValueError is raised when guess contains repeated digits
    :return:
    """
    game = Game()
    for n in range(1000,10000):
        if len(set(list(str(n)))) < 4:
            with pytest.raises(ValueError):
                game.check_user_input(n)


def test_secret_valid_number():
    for i in range(100000):
        game = Game()
        assert 1000 <= game.secret <= 9999


def test_move():
    """
    TODO:
    :return:
    """
    game = Game()
    for n in range(0, 1000):
        assert game.move(n) == "Number must contain 4 digits"
    for n in range(10000, 100000):
        assert game.move(n) == "Number must contain 4 digits"
    for p in range(5, 10):
        assert game.move(n) == "Number must contain 4 digits"


def test_move_win():
    """
    Testing win situation
    :return:
    """
    game = Game()
    assert game.move(game.secret) == 'YOU WIN!'
    assert game.game_over == True

data_for_test_no_win = [
    (1234, 6789, '0 bulls, 0 cows'),
    (1234, 5671, '0 bulls, 1 cow'),
    (6789, 7238, '0 bulls, 2 cows'),
    (6789, 1678, '0 bulls, 3 cows'),
    (6789, 9678, '0 bulls, 4 cows'),
    (1234, 5278, '1 bull, 0 cows'),
    (1234, 1527, '1 bull, 1 cow'),
    (4257, 7154, '1 bull, 2 cows'),
    (9347, 4379, '1 bull, 3 cows'),
    (7596, 3526, '2 bulls, 0 cows'),
    (8321, 8271, '2 bulls, 1 cow'),
    (3659, 3956, '2 bulls, 2 cows'),
    (3590, 3570, '3 bulls, 0 cows')
]


@pytest.mark.parametrize("secret,number,expected_message", data_for_test_no_win)
def test_move_no_win(secret, number, expected_message):
    """
    Testing no-win situation
    :return:
    """
    game = Game()
    game.secret = secret
    assert game.move(number) == expected_message
    assert game.game_over == False
