#Word Summary Exercise version 2- This will do the same thing as Word Summary Exercise, but without using a bunch of imported functions.

user_input = str(input("Please enter a sentence: "))
words = user_input.split()
dict = {}
def word_summary(user_input, dict):
    count = 1
    for letter in words:
        if letter in dict:
            dict[letter] += count
        else:
              dict[letter] = count
    return dict

print(word_summary(words, dict))