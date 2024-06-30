import random
import linecache

HANGMAN: list = [
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
    random_num: int = random.randint(0, 852)
    WORD: str = linecache.getline('words.txt', random_num).strip('\n')

"""
Player 1
Player 2
How many points to win
correct or wrong
check the word
"""


class Hangman:
    def __init__(self, word_to_guess: str):
        self.attempts: int = len(HANGMAN)
        self._word_to_guess: str = word_to_guess
        self.game_progress: list = list('_' * len(self._word_to_guess))
        self._player1 = None

    @property
    def player1(self) -> str:
        return self._player1

    @player1.setter
    def player1(self, value) -> None:
        self._player1 = value

    def __str__(self):
        return f"""This is a Hangman Game. The players are {self.player1} and {self.player2}.
                Attempts left: {self.attempts}.
                Progress: {''.join(self.game_progress)}"""

    def display(self) -> None:
        print(f"Number of Attempts: {self.attempts}\nGame Progress: {''.join(self.game_progress)}")

    def validate_character(self, guess: str) -> bool:
        if guess in self._word_to_guess and len(guess) == 1:
            self.game_progress[self._word_to_guess.index(guess)] = guess
            return True
        return False

    def play(self) -> None:
        self._player1: str = input("Enter Player Name: ")

        while self.attempts > 0 and ("_" in self.game_progress):
            self.display()
            guess: str = str(input("Enter the character: ").strip().lower())

            if self.validate_character(guess):
                print(f"Correct guess, GOOD JOB {self._player1}!")
            elif self.attempts >= 1:
                if self.attempts == 1:
                    self.attempts -= 1
                    print(f"Opps, Wrong guess... YOU LOST {self._player1}!!")
                    print(f"The word was: {self._word_to_guess}")
                else:
                    self.attempts -= 1
                    hangman_progress: list = HANGMAN[:9 - self.attempts]
                    print("Opps! WRONG Guess... Try Again!")
                    print(*hangman_progress, sep="\n")
                    print("___________________________________")

        if '_' not in self.game_progress:
            print(f"Congratulations! You've guessed the word: {self._word_to_guess}")


x = Hangman(word_to_guess=WORD)
x.play()
