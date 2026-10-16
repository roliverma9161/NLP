from nltk import ngrams
from nltk.tokenize import wordpunct_tokenize
text = "I love machine learning"
words = wordpunct_tokenize(text)
# unigram (N-1)
unigrams = list(ngrams(words, 1))
print("Unigrams:" , unigrams)
#biagram (N-2)
bigrams = list(ngrams(words, 2))
print("Bigrams:" , bigrams)
#trigram (N-3)
trigrams = list(ngrams(words, 3))
print("Trigrams:" , trigrams)