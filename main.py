import random
import nltk
from nltk.corpus import words
# nltk.download('words')
word_list=[x for x in words.words() if len(x)==6]
word=['_' for x in range(6)]

def random_word_generator():
    rand_word=random.choice(word_list)
    return rand_word



def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, both legs
        """
           --------
           |      |
           |      O
           |     /|\|
           |     / \|
           -
        """,
        # head, torso, both arms, one leg
        """
           --------
           |      |
           |      O
           |     /|\|
           |     /  |
           -
        """,
        # head, torso, both arms
        """
           --------
           |      |
           |      O
           |     /|\|
           |      
           -
        """,
        # head, torso and one arm
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def play_hangman():
    word = random_word_generator()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word: " + "_ " * len(word))

    while tries > 0 and word_letters != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            print("Good guess!")
        else:
            tries -= 1
            print("Wrong guess! Tries left:", tries)

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: " + " ".join(word_display))
        print(display_hangman(tries))

    if word_letters == guessed_letters:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
