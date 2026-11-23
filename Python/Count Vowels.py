sentence = "Hello Python World"
vowel_count = sum(1 for ch in sentence.lower() if ch in "aeiou")
print(vowel_count)  # 4