import random

# 4.1 Exercise
hints = ["What would you use to play Doom-2?", 'the room, where \
people usually cook', 'the best tech university in KZ',
         "the best programming language in the world"]
the_words = ["computer", "kitchen", "kbtu", 'python']
random_word = random.randint(0, 3)
the_word = the_words[random_word]
hint = hints[random_word]
game_over = False
board = list("*" * len(the_word))
guessed_letters = []  # 2.1 Exercise
points = 0  # 3.1 Exercise
while not game_over:
    print("")
    print("------------------------------")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {hint}")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        if user_guess in guessed_letters:  # 2.3 Exercise
            print("the letter is already guessed.")
        else:
            for i in range(len(the_word)):
                if the_word[i] == user_guess:
                    board[i] = user_guess
                    point = random.randint(1, 100)
                    points += point
                    print(f'you have won {point} points,'
                          f' total {points} points')  # 3.2 Exercise
                    guessed_letters.append(user_guess)  # 2.2 Exercise
        if user_guess not in the_word:  # 1 Exercise
            print("Incorrect, think again.")
    else:
        if user_guess == the_word:
            print("Correct! Congratulations!")
            game_over = True
        else:
            print("Incorrect, think again.")
