import yake

text = """
Artificial intelligence and machine learning are revolutionizing modern technology. 
Data science relies heavily on Python for analyzing complex datasets and building neural networks.
"""

# Keyword extractor 
kw_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, top=5)
keywords = kw_extractor.extract_keywords(text)

print("--- main keywords ---")
for kw, score in keywords:
    print(f"Keyword: {kw:<25} (Score: {score:.4f})")