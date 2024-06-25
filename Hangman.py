import random
import linecache

HANGMAN = [
    '________',
    '|       |',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|       |',
    '|      / \ '
]

with open("words.txt", "r") as f:
    random_num = random.randint(0, 852)
    WORD = linecache.getline('words.txt', random_num)

"""
Player 1
Player 2
How many points to win
correct or wrong
check the word
"""


class Hangman:
    def __init__(self, word_to_guess):
        self.attempts = 9
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def __str__(self):
        return f"""This is a Hangman Game. The players {self.player1} and {self.player2}. 
        The person to guess is {self.current_player}. He has {self.attempts} attempts left! {self.game_progress}"""

    @property
    def player1(self):
        return self._player1

    @player1.setter
    def player1(self, value):
        self._player1 = value

    @property
    def player2(self):
        return self._player2

    @player2.setter
    def player2(self, value):
        self._player2 = value


x = Hangman(word_to_guess="WORD")
print(x)
print(x.player1)
x.player1 = "Ahmd"
print(x.player1)