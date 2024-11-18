import random

def hangman():
    word_list = ['stranger', 'hangman', 'challenge', 'programming', 'developer', 'artificial', 'intelligence']
    word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_completion = ['_'] * len(word)

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")
    
    while incorrect_guesses < max_incorrect_guesses and '_' in word_completion:
        print("\nCurrent word: ", ' '.join(word_completion))
        print("Guessed letters: ", ' '.join(guessed_letters))
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for index, letter in enumerate(word):
                if letter == guess:
                    word_completion[index] = guess
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        print("Incorrect guesses left:", max_incorrect_guesses - incorrect_guesses)

    if '_' not in word_completion:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()