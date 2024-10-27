
import random
word_list = ["advard","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Testing code
print(f"Pasted, the solution is {chosen_word}")

# TODO 1: Create an empty list called display. 
# For each letter in the chosen_word, add a "-"
# 'display'
display = []

for underscore in range(word_length):
    display+="_"
print(display)
# So if the chosen_word was "apply", display 
# should be ["_","_","_","_"] with 5 "_" representing
# each  letter to guess. 


# TODO 2: Loop through each position in the chosen_word
# If the letter at that position matches 'guess' then 
# reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word 
# was "apple", then display should be ["_","p","p","_","_"].

end_of_life = False
while not end_of_life:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]=guess 
    print(display)

# this is to check there _ more left or not or You won. 
    if "_" not in display:
        end_of_life = True
        print("You Win")



# for letter in chosen_word:  
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

#TODO-3: Print 'display' and you should see the 
# guessed letter in the correct position and every other
# letter replace with "_".
# Hint - Don't worry about getting the user to guess the 
# next letter. We'll tackle that in step 3. 
        