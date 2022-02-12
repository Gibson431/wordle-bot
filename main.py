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


def calc_best_answer():
    answer = gameController.word_cache.get_best_answer(gameController.letter_cache)
    return answer


def main():
    load_cache()
    best = calc_best_answer()
    print(best)
    # print(gameController.word_cache.available_words)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    gameController.vet_words()
    best = calc_best_answer()
    print(f"Words left: {len(gameController.word_cache.available_words)}")
    print(f'Suggested word: {best}')
    print(f'All words:')
    df = pd.DataFrame.from_dict(gameController.word_cache.available_words)
    print(df)
    # print(gameController.word_cache.available_words)
    # letter_cache.export()
    # word_cache.export()

    return


if __name__ == "__main__":
    main()
