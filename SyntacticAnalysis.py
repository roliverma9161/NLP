import spacy

# 1. Spacy ka English language model load karein
nlp = spacy.load("en_core_web_sm")

# 2. Input Sentence
text = "The quick brown fox jumps over the lazy dog."

# 3. Text ko process karein (Tokenization, POS tagging, Parsing)
doc = nlp(text)

print("=" * 65)
print(f"{'Text (Token)':<12} | {'POS Tag':<10} | {'Grammar Category':<15} | {'Dependency'}")
print("=" * 65)

# 4. Sentence ke har token ki grammatical structure analyze karein
for token in doc:
    print(f"{token.text:<12} | {token.pos_:<10} | {spacy.explain(token.pos_):<15} | {token.dep_}")

print("=" * 65)