import random
# TO DO 1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(chosen_word)

# TO DO 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

guess = input("Guess a letter: ").lower()

# TO DO 3: Check if the letter the user guessed is one of the letters in the chosen_word. Print right if it is, wrong it is not.


# for letter in chosen_word:
#     if guess == letter:
#         print("Right")
        
    
#     else:
#         print("Wrong")

# TO DO 4: Create a placeholder with the same number of blanks as the chosen word and fill it with "_" 

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

        
            

