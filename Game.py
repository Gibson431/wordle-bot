class Controller():
    """
    Controls the gameplay
    """

    def __init__(self, LetterCache, WordCache):
        self.letter_cache = LetterCache
        self.word_cache = WordCache
        self.found_letters = []
        self.blacklist = []
        self.found_letters_strict = ["", "", "", "", ""]
        self.blacklist_location = [[], [], [], [], []]
        return

    def vet_words(self):
        """
        vets all current words with new list of needed letters
        """
        self.vet_words_strict()
        new_words = []
        if (not len(self.found_letters)) and (not len(self.blacklist)):  # if no letters have been found
            # return all previous words
            return list(dict(self.word_cache.available_words).keys())

        for word in list(dict(self.word_cache.available_words).keys()):
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

        # return list of new available words
        return list(dict(self.word_cache.available_words).keys())

    def vet_words_strict(self):
        """
        Vets the words based of letters with known locations
        """
        new_words = []
        if self.found_letters_strict != ["", "", "", "", ""]:
            for word in list(dict(self.word_cache.available_words).keys()):
                isViable = True
                for index, letter in enumerate(self.found_letters_strict):
                    if letter == "":  # skip if location is empty
                        continue

                    if word[index] != letter:
                        isViable = False

                if isViable:
                    new_words.append(word)
        else:
            new_words = list(dict(self.word_cache.available_words).keys())

        # TODO vet words with letter placements already guessed
        if self.blacklist_location != [[], [], [], [], []]:
            words_to_remove = []
            for word in new_words:
                for place, letters in enumerate(self.blacklist_location):
                    for letter in letters:
                        if letter == word[place]:
                            words_to_remove.append(word)
                            break
                    else:
                        continue
                    break

            for word in words_to_remove:
                new_words.remove(word)

        self.word_cache.update_words(new_words)
        return list(dict(self.word_cache.available_words).keys())

    def calc_result(self, result):
        """
        calculates letter placement based on wordle results\n
        n - grey letter here\n
        y - yellow letter here\n
        g - green letter here\n
        ⬛🟩🟩🟨⬛ = 'nggyn'
        """
        if result == "clear" or result == "c":
            self.clear_game()
            print("~~~~~~~~~~~~~~~~\nClearing game...\n~~~~~~~~~~~~~~~~")
            return

        for i in result:
            if i not in "nyg":
                self.next_word()
                return

        for index, letter in enumerate(result):
            if letter == "n":
                self.blacklist.append(self.last_guess[index])
            elif letter == "y":
                self.found_letters.append(self.last_guess[index])
                self.blacklist_location[index].append(self.last_guess[index])
            elif letter == "g":
                self.found_letters.append(self.last_guess[index])
                self.found_letters_strict[index] = self.last_guess[index]
        return

    def check_letters(self):
        for letter in self.found_letters:
            if letter in self.blacklist:
                self.blacklist.remove(letter)
        return None

    def sort(self):
        self.check_letters()
        self.vet_words()
        return None

    def next_word(self):
        result = input(f"last result based on guess '{self.last_guess}': ")
        self.calc_result(result)
        self.sort()
        suggested_word = self.word_cache.get_best_answer(self.letter_cache)
        self.last_guess = suggested_word[0]
        return suggested_word
    
    def clear_game(self):
        self.last_guess = ""
        self.found_letters = []
        self.blacklist = []
        self.found_letters_strict = ["", "", "", "", ""]
        self.blacklist_location = [[], [], [], [], []]
        self.word_cache.update_words()

    def print_info(self):
        print(self.last_guess)
        print(self.found_letters)
        print(self.blacklist)
        print(self.found_letters_strict)
        print(self.blacklist_location)
