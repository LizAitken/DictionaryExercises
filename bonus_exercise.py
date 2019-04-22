# #Bonus- Find top three histogram word tally
from collections import Counter, OrderedDict

sentence = str(input("Please enter a sentence: "))
words = sentence.split()
word_count = Counter(words)

print(word_count.most_common(3))