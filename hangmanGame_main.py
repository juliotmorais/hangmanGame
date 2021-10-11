import random
import hangmanWord
import hangmanArt


chosen_word = random.choice(hangmanWord.word_list)
chosen_word_list = list(chosen_word)
blanks = []
blank_count = 0
tries =6
game_over_text =" Sorry you lose! Try again!"

print("")
for letter in chosen_word:
    blanks.append("_")
    blank_count+=1

# ------FOR DEBUGGING-----
#print(chosen_word)
#print(chosen_word_list)
#print(blanks)
#print(blank_count)
# ------FOR DEBUGGING-----

print(hangmanArt.logo)
print("")
print("Welcome to Hangman!")
print("Your word is: ")
print(blanks)

while tries !=0:

    if blank_count == 0:
        game_over_text= "Congratulations! You win!"
        break

    else:
        print(hangmanArt.stages[tries])
        print("")
        guess = input ("Pick a letter: ")
        print("")
        print(f"You chose '{guess}' !")

        if guess in chosen_word_list:
                for i, letter in enumerate(chosen_word_list):
                    if guess == letter:
                        blanks[i] = guess
                        blank_count-=1

        else:
            tries-=1
            print(f"Sorry '{guess}'' is incorrect. {tries} tries left")

        print(blanks)

print("")
print()
print(hangmanArt.stages[tries])
print(game_over_text)
print(f"The word was '{chosen_word}'")
print("")
