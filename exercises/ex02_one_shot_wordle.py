"""EX02 - One Shot Wordle!"""

__author__ = "730550997"

# Define variables
secret_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Ask user for guess
user_guess = input(f"What is your {len(secret_word)}-letter guess? ")

# While loop to test guess
valid = False
guess_index = 0
emoji_str = ""

while valid is False:
    if len(user_guess) == len(secret_word):
        valid = True

        # Create while loop to make the color string
        while guess_index < len(user_guess):
            if user_guess[guess_index] == secret_word[guess_index]:
                emoji_str += f"{GREEN_BOX}"
            else:
                chr_exists = False
                # While loop to see if the letter is in the word, doesn't matter about where it is
                secret_index = 0
                while chr_exists is False and secret_index < len(secret_word):
                    if user_guess[guess_index] == secret_word[secret_index]:
                        chr_exists = True
                    else:
                        secret_index += 1

                if chr_exists is True:
                    emoji_str += f"{YELLOW_BOX}" 
                else:
                    emoji_str += f"{WHITE_BOX}"
            guess_index += 1

        print(emoji_str)

        # Tell user if their guess was correct        
        if user_guess == secret_word:
            print("Woo! You got it!")
        else:
            print("Not quite. Play again soon!")
    else:
        user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
