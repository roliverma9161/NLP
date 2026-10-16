from sklearn.feature_extraction.text import CountVectorizer
documents=[
    "i love machine learning", "i love python programming",
    "machine learning is intersting"
]
vectorizer = CountVectorizer()
X=vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print("\nBags of words Matrix")
print(X.toarray())