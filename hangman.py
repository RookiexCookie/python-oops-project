import random


class Hangman:
    def __init__(self):
        word_list = [
            "PYTHON",
            "CASA",
            "CARRO",
            "MONO",
            "DJANGO",
            "LOGIC",
            "UNITTESTING",
        ]
        self.word_to_guess = random.choice(word_list)  # random words
        self.failed_attempts = 0
        self.game_progress = ["_" for i in range(len(self.word_to_guess))]
        self.guessed_letters = set()
        self.max_attempts = 7
        self.user_input = ""
        self.stages = [
            r"""
                     _______
                    |/      |
                    |
                    |
                    |
                    |
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |
                    |
                    |
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |       |
                    |
                    |
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |       |
                    |       |
                    |
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |      \|
                    |       |
                    |
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |      \|/
                    |       |
                    |
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |      \|/
                    |       |
                    |      /
                  __|___
            """,
            r"""
                     _______
                    |/      |
                    |      (_)
                    |      \|/
                    |       |
                    |      / \
                  __|___
            """,
        ]

    def find_indexes(self, letter):
        index = []
        for i, char in enumerate(self.word_to_guess):
            if char == letter.upper():
                index.append(i)
        return index

    def is_invalid_letter(self, input):
        if len(input) == 1 and input.isalpha():
            return False
        return True

    def update_progress(self, letter, indexes):
        for i in indexes:
            self.game_progress[i] = letter

    def get_user_input(self):
        self.user_input = input("Enter A Letter:").upper()

    def print_game_status(self):
        print(self.stages[self.failed_attempts])
        print(" ".join(self.game_progress))
        print(f"Attempts Left: {self.max_attempts - self.failed_attempts}")

    def play(self):
        while self.failed_attempts < self.max_attempts:
            if "_" in self.game_progress:
                self.print_game_status()
                self.get_user_input()

                if self.is_invalid_letter(self.user_input):
                    print("Enter Valid Character Please!")
                    continue
                if self.user_input in self.guessed_letters:
                    print("You already guessedit")
                    continue
                self.guessed_letters.add(self.user_input)
                index = self.find_indexes(self.user_input)
                if index:
                    self.update_progress(self.user_input, index)
                else:
                    print("Wrong Choice")
                    self.failed_attempts += 1
            else:
                self.print_game_status()
                print("Yay Congratulations!!!!")
                break

        if self.failed_attempts == self.max_attempts:
            print(self.print_game_status())
            print(f"GAME OVER! The word was: {self.word_to_guess}")


hangman = Hangman()
hangman.play()
