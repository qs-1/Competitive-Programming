import random

def word_guess_optimized():
    words = ["apple", "banana", "cherry", "grapes", "orange"]
    word = random.choice(words)
    guessed_letters = set()
    tries = 6

    print("\n🚀 Optimized Word Guess Game!")
    revealed = ["_"] * len(word)  # Preallocated list → efficient

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    revealed[i] = guess
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! {tries} tries left.")

        print("Word:", " ".join(revealed))

        if "_" not in revealed:
            print("🎉 You win! Word was:", word)
            return

    print("💀 Game Over! Word was:", word)

word_guess_optimized()