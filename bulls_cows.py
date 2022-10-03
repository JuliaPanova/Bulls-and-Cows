"""
This code can be used to play the Bulls and Cows game.
See the game rules at:
https://en.wikipedia.org/wiki/Bulls_and_Cows
"""
import random


def compare_numbers(secret: int, guess: int):
    """
    Compares secret and guess numbers and returns the number of bulls and cows
    :param secret: a 4-digit number
    :param guess: a 4-digit number
    :return: number of bulls and cows
    """
    s_secret = str(secret)
    s_guess = str(guess)
    bulls, cows = 0, 0
    for i in range(len(s_guess)):
        if s_guess[i] == s_secret[i]:
            bulls += 1
        elif s_guess[i] in s_secret:
            cows += 1
    return bulls, cows


class Game:
    def __init__(self):
        secret_list = random.sample(range(10), 4)
        while secret_list[0] == 0:
            # Generates a new secret list if the previous one begins with 0
            secret_list = random.sample(range(10), 4)
        self.secret = int("".join(str(x) for x in secret_list))
        self.game_over = False

    def move(self, num_input: int) -> str:
        try:
            self.check_user_input(num_input)
        except ValueError as e:
            return str(e)
        bulls, cows = compare_numbers(self.secret, num_input)
        if bulls == 4:
            self.game_over = True
            return 'YOU WIN!'
        else:
            return f'{bulls} bull{"s"*int(bulls!=1)}, {cows} cow{"s"*int(cows!=1)}'

    def check_user_input(self, num_input: int):
        if not 1000 <= num_input <= 9999:
            raise ValueError("Number must contain 4 digits")
        if len(set(list(str(num_input)))) < 4:
            raise ValueError("All digits must be different")

def run():
    game = Game()
    while not game.game_over:
        while True:
            s = input('Input a 4-digit number: ')
            try:
                num = int(s)
                break
            except:
                print('This is not a number')
        print(game.move(num))


if __name__ == '__main__':
    run()
