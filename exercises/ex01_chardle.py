"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730550997"


# Ask user for word and letter
word = input("Enter a 5 letter word: ") 
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for", letter, "in", word)

# Check if letter is in the word
count = 0

if letter == word[0]:
    print(letter, 'found at index 0')
    count += 1
if letter == word[1]:
    print(letter, 'found at index 1')
    count += 1
if letter == word[2]:
    print(letter, 'found at index 2')
    count += 1
if letter == word[3]:
    print(letter, 'found at index 3')
    count += 1
if letter == word[4]:
    print(letter, 'found at index 4')
    count += 1

# Print num of instances
if count == 0:
    print("No instances of", letter, "found in", word)
if count == 1:
    print("1 instance of", letter, "found in", word)
if count > 1:
    print(count, "instances of", letter, "found in", word)