from langdetect import detect

texts = [
    "Hello, How are you?",
    "Hello, how are you doing today?",
    "Bonjour tout le monde",
    "Hola, ¿cómo estás?",
]

for text in texts:
    lang = detect(text)
    print(f"Text: '{text}' --> Language Code: {lang}")