import random
import Art
import Word_list

print(f"{Art.logo}\n")

end_game = False
lives = 6
word = random.choice(Word_list.word_list)
print(word)

display = []

for item in range(len(word)):
    display += "_"
print(display)

while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
       print(f"You've already guessed {guess} . ")
    
    for position in range(len(word)):
       item = word[position]
       if guess == item :
        display[position] = guess
    
    if guess not in display:
        print(f"You guessed {guess} , thats not in the word. You lose a live.")
        lives -=1
        if lives == 0:
            end_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You win!")

    print(Art.stages[lives])
 
        



    

