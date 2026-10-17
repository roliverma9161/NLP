from sklearn.feature_extraction.text import TfidfVectorizer
documents =[" i love machine learning", "i love pyhton programming", "machine learning is interesting"]
# create TF-IDF model
vectorizer = TfidfVectorizer()
# Transform documents into TF-IDF matrix
X=vectorizer.fit_transform(documents)
# display vocabulary
print("vocabular:y")
print(vectorizer.get_feature_names_out)
# display TF-IDF values
print("\nTF-IDF matrix:")
print(X.toarray().round(2))