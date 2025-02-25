import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)





game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    display = ""    
    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_letter.append(guess)
            
        elif letter in correct_letter:
            display += letter
            
        else:
            display += "_"
    
    print(display)
    
    if "_" not in display:
        print("You Win!! :)")
        game_over = True

        
