import random

# List of predefined words
words = ["apple", "tiger", "house", "water", "music"]

# Select a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("Welcome to Hangman!")
print("Guess the word:")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        print("Correct!")

        # Reveal the letter in the word
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)