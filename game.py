import random
from os import system
from os import walk
from sys import platform

HEADER_GUI = """*** HANGMAN GAME ***
Select a category:
"""

HANGMAN_GUI = ["""




""",
"""





=======""",
"""
|
|
|
|
|
=======""",
"""
+-----+
|
|
|
|
|
=======""",
"""
+-----+
|
|  O
|
|
|
=======""",
"""
+-----+
|
|  O
|  |
|
|
=======""",
"""
+-----+
|
|  O
| /|
|
|
=======""",
"""
+-----+
|
|  O
| /|\\
|
|
=======""",
"""
+-----+
|
|  O
| /|\\
| /
|
=======""",
"""
+-----+
|
|  O
| /|\\
| / \\
|
=======""",
"""
+-----+
|  |
|  O
| /|\\
| / \\
|
======="""]


def clear_gui():
    if platform == "linux":
        system("clear")
    else:
        system("cls")


def wrap_word(word):
    word_wrapper = ''
    for i in word:
        if i == " ":
            word_wrapper += " "
        else:
            word_wrapper += "_"                          
    return word_wrapper


def match_letter(word, word_wrapper, letter):
    index = word.find(letter)
    temp = list(word_wrapper)
    while not index == -1:        
        temp[index] = letter
        index = word.find(letter, index + 1)
        
    return "".join(temp)
    

def start_hangman(word):   
    word_wrapper = wrap_word(word)
    index = 0
    while True:
        try:
            clear_gui()
            print(HANGMAN_GUI[index])
            print(word_wrapper)

            if word_wrapper == word:
                print("You win!")
                break            

            letter = input("Please enter a letter: ").lower()

            if letter not in word:
                index += 1
                if index > len(HANGMAN_GUI) - 1:
                    raise
                continue

            word_wrapper = match_letter(word, word_wrapper, letter)                    

        except:
            print(f'You lost! The word was: {word}')
            break


def get_aleatory_word(category):
    path = "./bd/" + category + ".txt"
    with open(path, "r") as f:
        all_text = f.read()
        words = list(map(str, all_text.split()))
        return random.choice(words).lower()


def get_categories():
    categories = []
    for root, dirs, files in walk("./bd/"):
        for filename in files:
            categories.append(filename.split(".")[0])
    return categories


def get_category():    
    categories = get_categories()
    option = 1

    for i in categories:
        print(f'{option} - {i.capitalize()}')
        option += 1

    try:
        option = int(input(""))
        if option > len(categories) or option < 1:
            raise ValueError
        return categories[option - 1]
    except ValueError:
        clear_gui()
        print("Oops!  That was no valid number.  Try again...")
        return get_category()


def run():
    print(HEADER_GUI)
    category = get_category()
    word = get_aleatory_word(category)
    start_hangman(word)


if __name__ == "__main__":
    run()