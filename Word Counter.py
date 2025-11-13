# String methods
print("Word Counter")
print("============")

sentence = input("Enter a sentence: ")

words = sentence.split()
characters = len(sentence)
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"\nNumber of words: {len(words)}")
print(f"Number of characters: {characters}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
