import random
import os
from itertools import islice

turns_taken = 0

# Hangman Game

#Game start
def start_game():
    print("Welcome to Hangman!")
    print("Select a language for words to guess:")
    print("1. English")
    print("2. Español")
    print("3. Deutsch")
    language = input("Enter the number of your choice: ")
    if language == "1":
        print("You chose English.")
    elif language == "2":
        print("You chose Español.")
    elif language == "3":
        print("You chose Deutsch.")
    else:
        print("Invalid choice. Please try again.")

    print("Select a difficulty:")
    print("1. Baby")
    print("2. Easy")
    print("3. Medium")
    print("4. Hard")
    mode = input("Enter the number of your choice: ")
    if mode == "1":
        print("You chose Baby mode.")
    elif mode == "2":
        print("You chose Easy mode.")
    elif mode == "3":
        print("You chose Medium mode.")
    elif mode == "4":
        print("You chose Hard mode.")
    else:
        print("Invalid choice. Please try again.")
        return  
    return language, mode

def play_game(language, mode):
    word_bank = []
    if language == "1":
        if mode == "1":
            print("Starting Baby mode in English...")
            with open("./en_words.txt", "r") as lines:
                for line in islice(lines, 2, 9):
                    word_bank.append(line.strip())
        elif mode == "2":
            print("Starting Easy mode in English...")
            with open("./en_words.txt", "r") as lines:
                for line in islice(lines, 13, 20):
                    word_bank.append(line.strip())
        elif mode == "3":
            print("Starting Medium mode in English...")
            with open("./en_words.txt", "r") as lines:
                for line in islice(lines, 24, 31):  
                    word_bank.append(line.strip())
        else:
            print("Starting Hard mode in English...")
            with open("./en_words.txt", "r") as lines:
                for line in islice(lines, 35, 42):
                    word_bank.append(line.strip())
    elif language == "2":
        if mode == "1":
            print("Starting Baby mode in Español...")
            with open("./es_words.txt", "r") as lines:
                for line in islice(lines, 2, 8):
                    word_bank.append(line.strip())
        elif mode == "2":
            print("Starting Easy mode in Español...")
            with open("./es_words.txt", "r") as lines:
                for line in islice(lines, 14, 19):
                    word_bank.append(line.strip())
        elif mode == "3":
            print("Starting Medium mode in Español...")
            with open("./es_words.txt", "r") as lines:
                for line in islice(lines, 25, 31):
                    word_bank.append(line.strip())
        else:
            print("Starting Hard mode in Español...")
            with open("./es_words.txt", "r") as lines:
                for line in islice(lines, 36, 41):
                    word_bank.append(line.strip())
    elif language == "3":
        if mode == "1":
            print("Starting Baby mode in Deutsch...")
            with open("./de_words.txt", "r") as lines:
                for line in islice(lines, 2, 7):
                    word_bank.append(line.strip())
        elif mode == "2":
            print("Starting Easy mode in Deutsch...")
            with open("./de_words.txt", "r") as lines:
                for line in islice(lines, 13, 19):
                    word_bank.append(line.strip())
        elif mode == "3":
            print("Starting Medium mode in Deutsch...")
            with open("./de_words.txt", "r") as lines:
                for line in islice(lines, 24, 30):
                    word_bank.append(line.strip())
        else:
            print("Starting Hard mode in Deutsch...")
            with open("./de_words.txt", "r") as lines:
                for line in islice(lines, 35, 42):
                    word_bank.append(line.strip())
    else:
        print("Invalid language choice. Please try again.")
        return  
    return word_bank
    
def hangman(turns_taken):
    if turns_taken == 0:
        print("  ______")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print(" _|_")
    elif turns_taken == 1:
        print("  ______")
        print("  |    |")
        print("  |")
        print("  |")
        print("  |")
        print(" _|_")
    elif turns_taken == 2:
        print("  ______")
        print("  |    |")
        print("  |    O")
        print("  |")
        print("  |")
        print(" _|_")
    elif turns_taken == 3:
        print("  ______")
        print("  |    |")
        print("  |    O")
        print("  |    |")
        print("  |")
        print(" _|_")   
    elif turns_taken == 4:
        print("  ______")
        print("  |    |")
        print("  |    O")
        print("  |   /|")
        print("  |")
        print(" _|_")  
    elif turns_taken == 5:
        print("  ______")
        print("  |    |")
        print("  |    O")
        print("  |   /|\\")
        print("  |")
        print(" _|_")  
    elif turns_taken == 6:
        print("  ______")
        print("  |    |")
        print("  |    O")
        print("  |   /|\\")
        print("  |   /")
        print(" _|_")  
    elif turns_taken == 7:
        print("  ______")
        print("  |    |")
        print("  |    O")
        print("  |   /|\\")
        print("  |   / \\")
        print(" _|_")  


# Start the game with the selected language and mode
language, mode = start_game()
word_bank = play_game(language, mode)

# Randomly select a word from the word bank#
current_word = random.choice(word_bank)

#Game variables
incorrect_guesses = []
correct_guesses = []
max_turns = 7

print("Your word has", len(current_word), "letters.")
print("You have " + str(max_turns) + " incorrect guesses in total.")

#Game loop
while turns_taken < max_turns:
    #Player input
    guess = input("Guess a letter: ").upper()
    if not guess.isalpha():
        print("Please enter a valid letter.")
        continue
    if guess in current_word:
        print("Correct! :)")
        correct_guesses.append(guess)


    else:
        print("Incorrect! :(")
        incorrect_guesses.append(guess)
    turns_taken = len(incorrect_guesses)

    print("Correct guesses: " + str(correct_guesses))
    print("Incorrect guesses: " + str(incorrect_guesses))

#Print correct letters but cover non guessed letters
    word = list(current_word)
    for i in range(len(word)):
        if word[i].upper() in correct_guesses:
            pass
        else:
            word[i] = "_"
    word = "".join(word)
    print(word)
    hangman(turns_taken)
    if word == current_word:
        print("Well done!")
        break
    else:
        continue


if turns_taken == max_turns:
    print("Incorrect guesses:" + str(incorrect_guesses))
    print("Correct guesses: " + str(correct_guesses))
    print("Your word was " + str(current_word))


#  ______
#  |    |
#  |    O
#  |   /|\
#  |   / \
# _|_