import random

# List of words to guess
word_list = ['apple', 'banana', 'cherry', 'grapes', 'orange', 'papaya', 'mango']
chosen_word = random.choice(word_list)

# Game variables
guessed_letters = []
tries = 6
display_word = ['_'] * len(chosen_word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {tries} incorrect tries allowed.")

while tries > 0 and '_' in display_word:
    print("\nWord:", ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[idx] = guess
    else:
        print("❌ Wrong guess.")
        tries -= 1
        print(f"Tries left: {tries}")

# Game result
if '_' not in display_word:
    print(f"\n🎉 Congratulations! You guessed the word: {chosen_word}")
else:
    print(f"\n😞 You lost! The word was: {chosen_word}")
