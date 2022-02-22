import nltk
from nltk.corpus import words
from itertools import combinations

# download the list of all english words
nltk.download('words')
word_list = words.words()

# hashmaps of word combinations
combinations_map = {}
common_letters = {}

# update the relevant hashmap
def updateMap(word):
  if len(word) > 1:
    combinations_map[word] = combinations_map[word] + 1 if word in combinations_map else 1
  else:
    common_letters[word] = common_letters[word] + 1 if word in common_letters else 1

for word in word_list:
  if len(word) == 5:
    [updateMap(word[x:y]) for x, y in combinations(range(len(word) + 1), r=2)]

print(sorted(combinations_map.items(), key=lambda x: x[1], reverse=True))
print(sorted(common_letters.items(), key=lambda x: x[1], reverse=True))

