from textblob import TextBlob

reviews = [
    "The product works wonderfully! I love the modern design.",
    "Worst experience ever. It broke on the very first day.",
]

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity  # Range: -1.0 (negative) to +1.0 (positive)

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Review: '{review}'\n -> Sentiment: {sentiment} (Score: {polarity:.2f})\n")