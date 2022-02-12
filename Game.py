class Controller():
    """
    Controls the gameplay
    """

    def __init__(self, LetterCache, WordCache):
        self.letter_cache = LetterCache
        self.word_cache = WordCache
        self.found_letters = ["a","t", "l"]
        self.blacklist = ["s", "e", "b", "o"]
        self.found_letters_strict = ["", "l", "", "", ""]
        self.blacklist_location = [[],[],[],[],[]]
        return

    def vet_words(self):
        """
        vets all current words with new list of needed letters
        """
        self.vet_words_strict()
        new_words = []
        if not len(self.found_letters):  # if no letters have been found
            return self.word_cache.available_words  # return all previous words

        for word in list(self.word_cache.available_words):
            isViable = True
            for letter in self.found_letters:
                if letter not in word:

                    isViable = False
                    break
            for letter in self.blacklist:
                if letter in word:
                    isViable = False
                    break
            if isViable == True:
                # if all letters in word, add to list of viable words
                new_words.append(word)
        # print(new_words)
        self.word_cache.update_words(new_words)

        return self.word_cache.available_words  # return list of new available words

    def vet_words_strict(self):
        """
        Vets the words based of letters with known locations
        """
        new_words = []
        if self.found_letters_strict != ["", "", "", "", ""]:
            for word in self.word_cache.available_words:
                isViable = True
                for index, letter in enumerate(self.found_letters_strict):
                    if letter == "": # skip if location is empty
                        continue

                    if word[0][index] != letter:
                        isViable = False

                if isViable:
                    new_words.append(word[0])
        # TODO vet words with letters already guessed

        # print(new_words)
        self.word_cache.update_words(new_words)
        return self.word_cache.available_words

    def next_word(self):
        return self.word_cache.get_best_answer()
