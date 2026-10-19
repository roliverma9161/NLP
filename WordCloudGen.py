import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = """
Natural language processing is a subfield of linguistics, computer science, and artificial intelligence 
concerned with the interactions between computers and human language. Processing natural language data 
enables computers to analyze, understand, and derive meaning from human speech and text.
"""

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
    text
)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()