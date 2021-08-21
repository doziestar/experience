import random


class GuessGame:
    """creating a guessing game"""

    def __init__(self, **kwargs):
        self._human_score = 0
        self._computer_score = 0
        self._guess_limit = 0
        self._number_of_guesses = 0
        self._secret_number = 0

    def setup(self):
        """this will enable the user setup the game the she wants to play
        it with the number of duration and range she want her guess"""
        self._human_score = 0
        self._computer_score = 0
        self._number_of_guesses = 0
        self._guess_limit = int(input("how many times do want the guess to be? "))
        self._secret_number = random.randint(int(input("enter either 1 or 10: ")), int(input("enter a number greater than 10: ")))
        context = {
            "human_score": self._human_score,
            "computer_score": self._computer_score,
            "number_of_guesses": self._number_of_guesses,
            "guess_limit": self._guess_limit,
            "secret_number": self._secret_number,

        }
        return context

    def engine(self):
        """this where the actual game logic lies"""
        setup = self.setup()
        while setup["number_of_guesses"] < setup["guess_limit"]:
            guess = int(input("guess the secret_number number: "))
            if guess == setup["secret_number"]:
                print("that's the correct answer")
                setup["human_score"] += 1
            elif setup["secret_number"] > guess:
                print("Your guess is low")
            elif setup["secret_number"] < guess:
                print("your guess is high")
            else:
                print( "your guess is incorrect")
                setup["computer_score"] += 1
            context = {
                "human_score":setup["human_score"],
                "computer_score":setup["computer_score"],
            }
        return context


    def score(self):
        """checking the score and knowing the winner"""
        return f"total score: {'human': self.engine()['human_score']} vs {'computer': self.engine()['computer_score']}"

    def reset(self):
        """starting a new game"""
        return self.engine()


if __name__ == '__main__':
    guessing_game = GuessGame()
    print(guessing_game.engine())

