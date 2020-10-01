import random
import string



def print_hangman():
    print("H A N G M A N")
    print()


class Hangman:

    def __init__(self):
        self.word_list = ["python", "kotlin", "javascript", "java"]
        self.word_to_guess = self.word_list[random.randint(0, len(self.word_list) - 1)]
        self.hidden_word = "-" * len(self.word_to_guess)

    def menu(self):
        menu_choice = input('Type "play" to play the game, "exit" to quit:')
        if menu_choice == "play":
            self.users_choice()
        else:
            exit()
        self.menu()

    def replace_char(self, pos, input_letter):
        self.hidden_word = self.hidden_word[:pos] + input_letter + self.hidden_word[pos + 1:]

    def users_choice(self):
        count_moves = 0
        lower_case_string = string.ascii_lowercase
        tried_letters = []
        while count_moves < 8 and self.hidden_word != self.word_to_guess:
            print()
            print(self.hidden_word)
            input_letter = input("Input a letter: ")
            if len(input_letter) != 1:
                print("You should input a single letter")
            elif input_letter not in lower_case_string:
                print("It is not an ASCII lowercase letter")
            elif input_letter in self.word_to_guess and input_letter not in self.hidden_word:
                for x in range(0, len(self.word_to_guess)):
                    if self.word_to_guess[x] == input_letter:
                        self.replace_char(x, input_letter)
                        tried_letters.append(input_letter)
            elif input_letter in self.hidden_word or input_letter in tried_letters:
                print("You already typed this letter")
            elif input_letter not in self.word_to_guess:
                print("No such letter in the word")
                tried_letters.append(input_letter)
                count_moves += 1
        if count_moves <= 8 and self.hidden_word == self.word_to_guess:
            print(self.word_to_guess)
            print("You guessed the word!")
            print("You survived!")
        else:
            print("You lost!")


first_try = Hangman()
print_hangman()
first_try.menu()
