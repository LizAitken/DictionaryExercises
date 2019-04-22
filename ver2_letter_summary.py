#Letter Summary - Dictionary Exercise version 2- Will do the same thing as Letter Summary without importing functions.
user_input = str(input("Please enter a word: "))
dict = {}

def letter_histogram(user_input, dict):
    count = 1
    for letter in user_input:
        if letter in dict:
            dict[letter] += count
        else:
              dict[letter] = count
    return dict

print(letter_histogram(user_input, dict))