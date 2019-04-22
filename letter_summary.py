#Letter Summary - Dictionary Exercise- Will take the inputed word, divvy up the letters, place them in the library, and count how many letters are in the word.

from collections import Counter, OrderedDict

user_input = str(input("Please enter a word: "))
letter_count = Counter(user_input)
letter_histogram = OrderedDict(letter_count)
print(letter_histogram)