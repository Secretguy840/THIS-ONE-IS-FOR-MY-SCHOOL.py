# String reversal
print("Palindrome Checker")
print("==================")

text = input("Enter a word or phrase: ")
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print(f"'{text}' is a Palindrome!")
else:
    print(f"'{text}' is not a Palindrome!")
