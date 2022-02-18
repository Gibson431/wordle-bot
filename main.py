from SourceData import possible_answers
from CustomCaches import *
from Game import Controller
import pandas as pd

letter_cache = LetterCache()
word_cache = WordCache(possible_answers)
gameController = Controller(letter_cache, word_cache)


def load_cache():
    gameController.letter_cache.update_scores(possible_answers)
    return

def init():
    load_cache()
    gameController.last_guess = gameController.word_cache.get_best_answer(gameController.letter_cache)[0]
    # letter_cache.export()

def main():
    while True:
        print(f'All words:')
        df = pd.DataFrame.from_dict(gameController.word_cache.available_words)
        print(df)
        print(f"Possible words left: {len(gameController.word_cache.available_words)}")
        print(f"Next Suggested word: {gameController.next_word()}")
        # gameController.print_info()

if __name__ == "__main__":
    init()
    main()
