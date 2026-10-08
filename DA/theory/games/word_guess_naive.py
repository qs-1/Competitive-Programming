import random

def word_guess_naive():
    words = ["apple", "banana", "cherry", "grapes", "orange"]
    word = random.choice(words)
    print(word)
    guessed_letters = []
    tries = 6

    print("🎯 Welcome to the Word Guess Game (Naive Version)!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")
        else:
            print("Good guess!")

        # Inefficient: rebuilds the word string each time (O(n))
        display = ""
        for ch in word:
            if ch in guessed_letters:
                display += ch
            else:
                display += "_"
        print("Word:", " ".join(display))

        print(guessed_letters)
        if "_" not in display:
            print("🎉 You win! Word was:", word)
            return

    print("💀 Game Over! Word was:", word)

word_guess_naive()