import spacy

# Load pre-trained English pipeline
nlp = spacy.load("en_core_web_sm")

text = "Apple bought a startup in London for $1 billion in 2024."
doc = nlp(text)

# Extract Named Entities
print("--- Named Entities ---")
for ent in doc.ents:
    print(f"{ent.text:<15} -> {ent.label_}")

# Tokens and Part-of-Speech tags
print("\n--- Tokens & POS ---")
for token in doc[:5]:
    print(f"{token.text:<10} POS: {token.pos_}")