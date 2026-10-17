from fastcoref import FCoref

# 1. Pre-trained Coreference Model load karein
model = FCoref(device='cpu')

# 2. Input Paragraph (multiple sentences with pronouns)
text = "Elon Musk founded SpaceX. He is also the CEO of Tesla. The company builds rockets."

# 3. Predict Coreferences (Pronouns/References linking)
preds = model.predict(texts=[text])

# 4. Resolve text (pronouns ko unke main noun se replace karke print karein)
resolved_text = preds[0].get_resolved_text()

print("=" * 65)
print("Original Text:")
print(text)
print("-" * 65)
print("Discourse Resolved Text (Context Integrated):")
print(resolved_text)
print("=" * 65)