import random


class GuessGame:
    """creating a guessing game"""

    def __init__(self, **kwargs):
        """setup the parameter of the game"""
        self._human_score = 0
        self._computer_score = 0
        self._number_of_guesses = 0
        self._guess_limit = int(input("how many times do want the guess to be? "))
        self._secret_number = random.randint(int(input("enter either 1 or 10: ")),
                                             int(input("enter a number greater than 10: ")))

    def engine(self):
        """this where the actual game logic lies"""
        while self._number_of_guesses < self._guess_limit:
            guess = int(input("guess the secret_number number: "))
            if guess == self._secret_number:
                print("that's the correct answer")
                self._human_score += 1
                break
            elif self._secret_number > guess:
                print("Your guess is low")
            elif self._secret_number < guess:
                print("your guess is high")
            self._number_of_guesses += 1
        else:
            print("your guess is incorrect")
            self._computer_score += 1
        context = {
            "human_score": self._human_score,
            "computer_score": self._computer_score,
        }

        return context

    def start_and_calculate_score(self):
        """ start the game by calling the engine method calculate the score function"""
        action = ""
        computer_score = 0
        human_score = 0
        game_repetition = int(input("How many times do you wish to play the game? "))
        for i in range(game_repetition):
            action = self.engine()
            human_score += action["human_score"]
            computer_score += action["computer_score"]
        return f"{'human score': human_score} vs {'computer score': computer_score}"


if __name__ == '__main__':
    guessing_game = GuessGame()
    print(guessing_game.start_and_calculate_score())
