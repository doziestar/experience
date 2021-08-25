import random
import number_guessing


class WordGuessing(number_guessing.GuessGame):
    """word guessing game"""

    def __init__(self, word, **kwargs):
        super().__init__(**kwargs)
        self._word = word

    def engine(self):
        """overwrite the engine function from the GuessGame"""
        secret = random.choice(self._word)
        while self._number_of_guesses < self._guess_limit:
            guess = input(f"enter a name in {self._word}: ")
            if guess == secret:
                print("guess is correct")
                self._human_score += 1
                break
            elif guess not in self._word:
                print("The choice word is not on the list, kindly choose one of the displayed words: ")
            else:
                print("kindly choose the write word")
            self._number_of_guesses += 1
        else:
            print("you failed to guess the right word")
            self._computer_score += 1
        context = {
            "human_score": self._human_score,
            "computer_score": self._computer_score,
        }

        return context


if __name__ == '__main__':
    word = ["banana", "plantain", "pear", "cashew", "paw paw", "mango"]
    wg = WordGuessing(word)
    print(wg.engine())
