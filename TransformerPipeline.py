from transformers import pipeline

# Load a pre-trained summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

article = """
Natural Language Processing (NLP) is a field of artificial intelligence where computers are 
trained to understand, process, and generate human language. Modern NLP relies heavily on 
Transformer architectures, which use self-attention mechanisms to understand complex context 
across long paragraphs of text.
"""

summary = summarizer(article, max_length=45, min_length=15, do_sample=False)
print("Summary:", summary[0]["summary_text"])