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
lives = 6
while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    
    if guess not in chosen_word:
        lives -= 1
        
    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_letter.append(guess)
            
        elif letter in correct_letter:
            display += letter
            
        else:
            display += "_"
        
            
    print(display)
    #WIN CONDITION
    if "_" not in display:
        print("You Win!! :)")
        game_over = True
    #LOSE CONDITION
    elif lives == 0:
        print("You lose! :(")
        game_over = True
        
        

        
