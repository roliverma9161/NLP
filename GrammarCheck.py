from textblob import TextBlob

wrong_text = "I have good intentioons, but I make misstakes in speling."

blob = TextBlob(wrong_text)

print("Wrong text:", wrong_text)
print("right text:", blob.correct())