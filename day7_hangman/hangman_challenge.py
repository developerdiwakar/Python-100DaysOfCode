import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
    "apple", "baboon", "elephant", "pineapple", "pomegranate", "crocodile", "rhinoceros",
    "raspberries"
]
display = []
# assign random word choosen to a variable
choosen_word = random.choice(word_list)
# print(choosen_word)
# add "-" to display list in place of choosen_word letter
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"

print(display)
# ask user to guess a letter
lives = 6
while lives >= 0:
    guess = input("\nGuess a letter: ").lower()
    matched_count = 0
    for index in range(word_length):
        letter = choosen_word[index]
        if letter == guess:
            display[index] = guess
            matched_count += 1            
    print(display)
    if matched_count == 0:
        print(stages[lives])
        lives -= 1
    if display.count("_") == 0:
        print("\n Congrats! You win.😉")
        break
else:
    print("\n Oops! You lose.😜")


