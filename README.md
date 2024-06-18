# -CodeAlpha_Hangman_game
This Hangman game is a simple command-line Python application where players guess letters to reveal a hidden word. The game randomly selects a word from a predefined list, and players have six attempts to guess the word correctly. 




# Hangman Game

![Hangman](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Hangman_game.jpg/1200px-Hangman_game.jpg)

## Description

This Hangman game is a simple command-line Python application where players guess letters to reveal a hidden word. The game randomly selects a word from the `nltk.corpus` word list, providing a wide variety of meaningful words. Players have six attempts to guess the word correctly. Incorrect guesses decrease the number of remaining tries, and a visual representation of the hangman is displayed after each wrong guess. The game ends when the player successfully guesses the word or runs out of attempts. This project demonstrates basic Python programming concepts, including loops, conditionals, sets, and functions, making it a great learning tool for beginners.

## Features

- Randomly selects a word from the `nltk.corpus` word list
- Visual representation of the hangman with each incorrect guess
- Keeps track of guessed letters and remaining attempts
- Simple and interactive command-line interface

## Getting Started

### Prerequisites

- Python 3.x installed on your machine
- `nltk` library installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```
3. Install the required libraries:
   ```bash
   pip install nltk
   ```
4. Download the NLTK word list:
   ```python
   import nltk
   nltk.download('words')
   ```

### Running the Game

To start the game, simply run the `hangman.py` script:
```bash
python hangman.py
```

## How to Play

1. The game will display the number of letters in the randomly selected word.
2. Guess one letter at a time by typing it and pressing Enter.
3. If the guessed letter is in the word, it will be revealed in its correct position(s).
4. If the guessed letter is not in the word, you lose one attempt, and the hangman drawing progresses.
5. The game ends when you either guess the word correctly or run out of attempts.

## Example

```
Welcome to Hangman!
Word: _ _ _ _ _ _ _
Guess a letter: a
Good guess!
Word: _ a _ _ _ _ _
Guess a letter: e
Wrong guess! Tries left: 5
Word: _ a _ _ _ _ _
  --------
  |      |
  |      O
  |    
  |      
  |     
  -
Guess a letter: n
Good guess!
Word: _ a n _ _ _ _
...
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request


## Acknowledgements

- [Python](https://www.python.org/)
- [NLTK](https://www.nltk.org/)
- [Hangman Image](https://en.wikipedia.org/wiki/Hangman_(game))
