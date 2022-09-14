"""EX03 -- Structured Wordle!"""

__author__= "730550997"


"""Function that checks if a letter is in a given word; returns True or False based on result"""
def contains_char(word: str, char: str) -> bool:
    assert len(char) == 1
    chr_exists = False

    # While loop to see if the letter is in the word, doesn't matter about where it is
    secret_index = 0
    while chr_exists is False and secret_index < len(word):
        if char == word[secret_index]:
            chr_exists = True
        else:
            secret_index += 1

    if chr_exists is True:
        return True 
    else:
        return False


"""Given 2 strings of same length, one a guess the other the answer, this function
returns an emoji string that shows which letters are right or wrong"""
def emojified(user_guess: str, secret_word: str) -> str:
    # define colors
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    assert len(user_guess) == len(secret_word)

    guess_index = 0
    emoji = ""

    while guess_index < len(user_guess):
        if user_guess[guess_index] == secret_word[guess_index]:
            emoji += f"{GREEN_BOX}"
        else:
            inside_str = contains_char(secret_word, user_guess[guess_index])
            if inside_str is True:
                emoji += f"{YELLOW_BOX}"
            else:
                emoji += f"{WHITE_BOX}"

        guess_index += 1
    
    return emoji


"""Function that asks user for guess and then checks if it is of correct length"""
def input_guess(expected_len: int) -> str:
    guess = input(f"Enter a {expected_len} character word: ")
    valid_guess= False
    while valid_guess is False:
        if len(guess) != expected_len:
            print(f"That wasn't {expected_len} chars! Try again: ")
            guess = input(f"Enter a {expected_len} character word: ")
        else:
            valid_guess = True
            return guess


"""Function that runs all functions, entrypoint for the program and main game loop """
def main() -> None:
    turn = 1
    secret = "codes"
    win = False

    while turn <= 6 and win is False:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(5)
        emoji = emojified(guess,secret)

        if guess == secret:
            print(emoji)
            print(f"You won in {turn}/6 turns!")
            win = True
        else:
            print(emoji)
            turn += 1

    if win is False:
        print("X/6 - Sorry, try again tomorrow!")



# icing to make the module more accessible
if __name__ == "__main__":
    main()