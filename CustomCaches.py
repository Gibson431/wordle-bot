from zoneinfo import available_timezones
from SourceData import possible_answers
import pandas as pd


class LetterCache:
    """
    Cache of letters and their frequency within the possible answers left 
    - includes their placment
    """

    def __init__(self):
        self.scores = [{}, {}, {}, {}, {}]
        self.clear_scores()
        return

    def sort(self):
        """sorts the letters from most frequent to least"""
        for i in range(0, 5):
            self.scores[i] = sorted(
                self.scores[i].items(), key=lambda item: item[1], reverse=True)
        return

    def update_scores(self, words):
        """updates scores using a list of words"""
        count = 0
        self.clear_scores()
        for word in words:
            for i in range(0, 5):
                self.scores[i][word[i]+""] += 1
            count += 1
        return count

    def clear_scores(self):
        """clears scores for new game case"""
        for i in self.scores:
            for num in range(0, 26):
                i[chr(num+97)+""] = 0
        return

    def export(self):
        """Exports cache to a csv file for viewing"""
        df = pd.DataFrame.from_dict(self.scores)
        df = df.transpose()
        df.to_csv(r'outputs/letters.csv', index=True, header=True)
        return


class WordCache():
    def __init__(self, word_list=possible_answers):
        self.available_words = {}
        self.update_words(word_list)
        return

    def update_words(self, words=possible_answers):
        self.available_words = dict({})
        for word in words:
            self.available_words[f'{word}'] = 0
        return len(self.available_words)

    def clear_weights(self):
        self.available_words = dict(self.available_words)
        for word in self.available_words:
            self.available_words[f'{word}'] = 0
        return

    def calc_weights(self, letters):
        self.clear_weights()
        self.available_words = dict(self.available_words)
        for word in self.available_words:
            for k, v in enumerate(word):
                scores = dict(letters.scores[k])

                self.available_words[f'{word}'] += scores[v]
        return

    def get_best_answer(self, letters):
        if len(self.available_words) == 0: return "no words left"
        self.calc_weights(letters)
        self.available_words = sorted(
                self.available_words.items(), key=lambda item: item[1], reverse=True)
        return self.available_words[0]

    def export(self):
        df = pd.DataFrame.from_dict(self.available_words)
        print(df)
        df.to_csv(r'outputs/words.csv', index=True, header=True)
        return