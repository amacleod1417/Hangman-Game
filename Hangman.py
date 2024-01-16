import string
from random import choice

def select_word(): 
    with open ("words.txt", mode = "r") as words:
        wordlist = words.readlines()
    return choice(wordlist).strip()

def getplayerinput(guessed_letters):
    while True:
        player_input = input("guess a letter:").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input
    
def _validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )

def joinguessedletters(guessed_letters):
    return "".join(sorted (guessed_letters)) 

def build_guessed_word (target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append (letter) 
        else:
            current_letters.append ("_")
    return " ".join(current_letters)

def draw_hanged_man (wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])

MAX_WRONG_GUESSES = 6

def gameover (wrong_guesses, target_word, guessed_letters): 
    if wrong_guesses == MAX_WRONG_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False

if __name__ == "__main__":
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word (target_word, guessed_letters)
    wrong_guesses = 0
    print ("welcome to hangman!")

    while not gameover(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man (wrong_guesses)
        print (f"your word is {guessed_word}")
        print ("current guess letters:", f"{joinguessedletters(guessed_letters)}")
    

        player_guess = getplayerinput(guessed_letters)
        if player_guess in target_word:
            print("lucky guess :(")
        else:
            print("haha wrong")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_WRONG_GUESSES:
         print("oh no you lose, i win :)")
    else:
            print ("congrats you beat me i guess")
    print (f"your word was : {target_word}" )
    




        



