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
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''','''
 +---+
 |   |
     |
     |
     |
     |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in chosen_word:
      lives -= 1
      print(stages[lives])
      if lives == 0:
        end_of_game = True 
        print("You lose.")
        
    if "_" not in display:
        end_of_game = True
        print("You win.")     
  