word_list = ["ardvark", "baboon", "camel"]

#TODO-1 Randomly choose a word from the word_list and assign it to 
#a variable called chosoe_word
import random
print("Start")
choose_word = random.choice(word_list)

#TODO_2 ask the user to guess a letter and assign
#their answer to a variable called guess. Make guess 
# lowercase.
guess = input("Guess the letter").lower()


# TODO_3 - check if the letter the user guessed (guess) is one of 
# the letters in the chosen_word.

for letter in choose_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")