from word_list import word_list
import random
from resource import stages, logo

display = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1

for _ in range(word_length):
    display += '_'

print(logo)

is_done = False

while not is_done:

    guess = input("Choose a letter from a to z: ").lower()

    if guess in display:
        print(f"You have guessed this letter! {guess}")

    for idx in range(word_length):
        if chosen_word[idx] == guess:
            display[idx] = chosen_word[idx]

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}. The letter you guessed is not in the word!")
        lives -= 1
        if lives == 0:
            print("Game Over")
            is_done = True

    if '_' not in display:
        is_done = True
        print("You Win!")

    print(stages[lives])
