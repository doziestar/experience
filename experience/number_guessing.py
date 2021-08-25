import random

# global secret number
secret_number = random.randrange(20)


class GuessGame:
    """creating a guessing game"""

    def __init__(self, **kwargs):
        """setup the parameter of the game"""
        self._human_score = 0
        self._computer_score = 0
        self._number_of_guesses = 0
        self._guess_limit = int(input("how many times do want the guess to be? "))

    def engine(self):
        """this where the actual game logic lies"""
        while self._number_of_guesses < self._guess_limit:
            guess = int(input("guess the secret_number number: "))
            if guess == secret_number:
                print("that's the correct answer")
                self._human_score += 1
                break
            elif secret_number > guess:
                print("Your guess is low")
            elif secret_number < guess:
                print("your guess is high")
            self._number_of_guesses += 1
        else:
            print("your guess is incorrect! Try again")
            self._computer_score += 1
        context = {
            "human_score": self._human_score,
            "computer_score": self._computer_score,
        }

        return context

    # def start_and_calculate_score(self):
    #     """ start the game by calling the engine method calculate the score function"""
    #     played = 0
    #     computer_score = 0
    #     human_score = 0
    #     game_repetition = int(input("How many times do you wish to play the game? "))
    #     while played < game_repetition:
    #         # for i in range(game_repetition):
    #         action = self.engine()
    #         human_score += action["human_score"]
    #         computer_score += action["computer_score"]
    #         played += 1
    #         return action


if __name__ == '__main__':
    guessing_game = GuessGame()
    print(guessing_game.engine())
