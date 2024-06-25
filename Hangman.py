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
    WORD = linecache.getline('words.txt', random_num).strip('\n')

"""
Player 1
Player 2
How many points to win
correct or wrong
check the word
"""


class Hangman:
    def __init__(self, word_to_guess):
        self.attempts = len(HANGMAN)
        self._word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self._word_to_guess))
        self._player1, self._player2 = None, None
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

    def display(self):
        print(f"It is {self.current_player}'s turn! Attempts: {self.attempts} left!")
        print(f"Guess the word {self.game_progress}")

    def validate_character(self, guess):
        if guess not in self._word_to_guess:
            return False
        self.game_progress[self._word_to_guess.index(guess)] = guess
        return True

    def play(self):
        self._player1 = input("Enter Player 1 Name: ")
        self._player2 = input("Enter Player 2 Name: ")
        print(self.attempts, len(HANGMAN), self.game_progress)
        while self.attempts and ("_" in self.game_progress):
            self.display()
            guess = input("Enter the character: ")
            if self.validate_character(guess):
                print("Guess correct, GOOD JOB!")
            else:
                self.attempts -= 1
                print("Opps! WRONG Guess, Try Again!")


x = Hangman(word_to_guess=WORD)
x.play()
