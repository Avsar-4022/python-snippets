# Function to check if the character is a vowel
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels


# Input from the user
char = input("Enter a character: ")

# Check if the input is a single alphabetic character
if len(char) == 1 and char.isalpha():
    if is_vowel(char):
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Please enter a single alphabetic character.")
