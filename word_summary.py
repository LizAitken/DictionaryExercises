#Word Summary Exercise- Will take the inputed sentence, divvy up the words, place them in the library, and count how many words are in the sentence. 

from collections import Counter, OrderedDict

sentence = str(input("Please enter a sentence: "))
words = sentence.split()
word_count = Counter(words)
word_histogram = OrderedDict(word_count)
print(word_histogram)