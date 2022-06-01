import random


class HangmanGame:
    def __init__(self):
        self.game_words = 'python', 'java', 'kotlin', 'javascript'
        self.random_word = ''
        self.hint = ''
        self.lives = 8
        self.letters_guessed = []
        self.last_input = ''

    def get_word(self):
        self.random_word = self.game_words[random.randrange(len(self.game_words))]
        self.hint = '-' * len(self.random_word)

    def catch_errors(self, user_input):
        if (len(user_input) > 1) or (len(user_input) == 0):
            print('You should input a single letter')
            return -1
        if not(user_input.isalpha()) or user_input.isupper():
            print('Please enter a lowercase English letter')
            return -1
        self.last_input = user_input
        return 0

    def is_guessed(self):
        for letter in self.letters_guessed:
            if self.last_input == letter:
                print("You've already guessed this letter")
                return 1
        return 0

    def search_letter(self):
        hint = list(self.hint)
        flag = 0
        for i in range(len(self.random_word)):
            if self.last_input == self.random_word[i]:
                flag += 1
                hint[i] = self.last_input
        if flag == 0:
            print("That letter doesn't appear in the word")
            self.count_lives(-1)
        self.letters_guessed.append(self.last_input)
        self.list_to_str(hint)

    def count_lives(self, number):
        self.lives += number
        if self.lives <= 0:
            print('You lost!')

    def list_to_str(self, list_):
        str_ = ''
        for letter in list_:
            str_ += letter
        self.hint = str_

    def compare_hint(self):
        if self.hint == self.random_word:
            self.lives = -1
            print(f'You guessed the word {self.random_word}!')
            print('You survived!')

    def play(self):
        if not(self.is_guessed()):
            self.search_letter()
            self.compare_hint()


def main():
    game = HangmanGame()
    game.get_word()
    print('H A N G M A N')
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option != 'exit':
        while game.lives > 0:
            print('\n' + game.hint)
            user_letter = input('Input a letter: ')
            if game.catch_errors(user_letter) != -1:
                game.play()
        option = input('\nType "play" to play the game, "exit" to quit: ')


main()
