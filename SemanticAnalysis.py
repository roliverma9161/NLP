import spacy

# 1. spaCy model load karein
nlp = spacy.load("en_core_web_sm")

# 2. Input text jisme entities hain
text = "Apple Inc. was founded by Steve Jobs in California on April 1, 1976."

# 3. Text ko process karein
doc = nlp(text)

print("=" * 65)
print(f"{'Entity Text':<18} | {'Entity Type (Label)':<15} | {'Description'}")
print("=" * 65)

# 4. Semantic entities ko extract karein
for ent in doc.ents:
    description = spacy.explain(ent.label_)
    print(f"{ent.text:<18} | {ent.label_:<15} | {description}")

print("=" * 65)