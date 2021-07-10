import random

stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
          """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
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
word_list = ['raju', 'riaj', 'shuvo']
chosen_word = random.choice(word_list)
print(f"what is your list name {chosen_word}")
display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print(display)
end_of_game = False
lives=6
while not end_of_game:
    guess = input("guess letter: ").lower()
    for position in range(word_len):
        letter = chosen_word[position]
        print(f"what {position} and {letter} and {chosen_word}")
        if letter == guess:
            display[position] = letter
    print(f"{''.join(display)}")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")
    print(stages[lives])
