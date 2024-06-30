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
        self._player1, self._player2 = None, None

    @property
    def player1(self) -> str:
        return self._player1

    @player1.setter
    def player1(self, value) -> None:
        self._player1 = value

    @property
    def player2(self) -> str:
        return self._player2

    @player2.setter
    def player2(self, value) -> None:
        self._player2 = value

    def display(self):
        print(f"Number of Attempts: {self.attempts}\nGame Progress: {self.game_progress}")

    def validate_character(self, guess):
        if guess not in self._word_to_guess and len(guess) > 0:
            return False
        elif guess in self._word_to_guess and len(guess) > 0:
            self.game_progress[self._word_to_guess.index(guess)] = guess
            return True

    def play(self):
        self._player1 = input("Enter Player 1 Name: ")
        self._player2 = input("Enter Player 2 Name: ")

        while self.attempts and ("_" in self.game_progress):
            self.display()
            guess = input("Enter the character: ")
            if self.validate_character(guess):
                print("Guess correct, GOOD JOB!")
            else:
                if self.attempts >= 1:
                    if self.attempts == 1:
                        self.attempts -= 1
                        print("Opps! WRONG Guess, YOU LOST!")
                        print(f"The word was: {self._word_to_guess}")
                    else:
                        self.attempts -= 1
                        hangman_progress = HANGMAN[:9 - self.attempts]
                        print("Opps! WRONG Guess, Try Again!")
                        print(*hangman_progress, sep="\n")
                        print("___________________________________")

    def __str__(self):
        return f"""This is a Hangman Game. The players {self.player1} and {self.player2}. 
        The person to guess is {self.current_player}. He has {self.attempts} attempts left! {self.game_progress}"""


x = Hangman(word_to_guess=WORD)
x.play()
