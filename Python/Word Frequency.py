from collections import Counter

text = "python is fun and python is easy"
counts = Counter(text.split())
print(counts)  # Counter({'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'easy': 1})