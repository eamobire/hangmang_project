# Step 2

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

# Testing code
print(hangman_art.logo)
print(f'Psst, the solution is {chosen_word} .')

# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.


display = []
for hypen in range(len(chosen_word)):
    display += "_"
print(display)
lives = 6

end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed '{guess}'")

    # TODO-2: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    position = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}' that's not in the word. You loose a life")
        print(hangman_art.stages[lives])
        if lives == 0:
            end_game = True
            print("Game Over")
            print(f"The word was {chosen_word}")

    # TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter
    #  replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in
    #  step 3.
    print(display)
    if "_" not in display:
        end_game = True
        print("You win")
