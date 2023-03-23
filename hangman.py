import random
from hangman_visual import lives_visual_dict
# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1"  # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values
# for the player's lives
# sample data, normally the word should be chosen from the countries-and-capitals.txt
word_to_guess = "Cairo"
lives = 5  # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here  # this list will contain all the tried letters
already_tried_letters = []
already_tried_wrong_letters = []

# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.


# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4

word = ""  # O pereche random din lista de tari si capitale
with open("D:\Codecool\hangman-python-cristimihaescu\countries-and-capitals.txt") as f:
    lines = f.readlines()  # daca atribui f la lines , se inchide automat fisierul
word = random.choice(lines)
wordposition = word.index(" ")
word = word[0:wordposition]
guessedletters = ""
difficulty = input("Choose your difficulty level ! 1.EASY, 2.MEDIUM, 3.HARD:  ")
lives = 0
used_letters = set()

if difficulty == "1":
    lives = 7
elif difficulty == "2":
    lives = 5
elif difficulty == "3":
    lives = 3
elif difficulty == "quit":
    print("See you next time, bye !")
    quit()
else:
    print("That is not a choice!")

print(len(word) * "_ ")
wrongletters = 0
wrong_typed_letters = ""


while lives > 0:
    guessed_letter = input(" Enter 1  letter !\n")
    while True:
        if guessed_letter in already_tried_letters:
            print("You've already typed these letters", already_tried_letters)   
        else:      
            already_tried_letters.append(guessed_letter)
        break
  #  for letter1 in word:
   #     if letter1 in guessedletters and letter1 in :
        
    if guessed_letter.lower() in word.lower():
        print(" Congrats! There is a", {guessed_letter}, "in your secret word !")
    else:
        while True:
            already_tried_wrong_letters.append(guessed_letter)
            print ("These are the wrong letters already tried", already_tried_wrong_letters)
            if already_tried_wrong_letters in already_tried_letters:
                lives = lives
            else:
                lives -= 1
                print(lives_visual_dict[lives])
                print("Oh no, you made a mistake! Maybe next time? :). lives left: ", lives)
            break
            
    guessedletters = guessedletters + guessed_letter.lower()

    for letter in word:
        if letter.lower() in guessedletters:
            print(f"{letter}", end="")
        else:
            print("_ ", end="")
            wrongletters += 1
    if wrongletters == 0:
        print(f" \nCongrats ! The secret word was : {word} . YOU WON ! ")
        break
else:
    print("\nSorry , you've been hanged ! ")
