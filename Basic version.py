def word_to_binary_basic():
    print("=== WORD TO BINARY CONVERTER ===")
    print("Enter a word or phrase to convert to binary\n")
    
    # Get input from user
    word = input("Enter your word: ")
    
    print(f"\nOriginal: '{word}'")
    print("Binary:   ", end="")
    
    # Convert each character to binary
    for char in word:
        # Get ASCII value and convert to 8-bit binary
        binary = format(ord(char), '08b')
        print(binary, end=" ")
    
    print("\n")

# Run the program
word_to_binary_basic()
