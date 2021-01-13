# Hangman Game

worder = input("What word would you like to hang? ").lower()
nosses = len(worder) // 2
print(f"You have {nosses} guesses. Fail well :)")
word = set(worder)
list = []

for letter in worder:
    list.append("_")
fill = "".join(list)
used = set()
def hangman(no_of_guesses, word):
    fill = "".join(list)
    while no_of_guesses > 0 and fill != word:
        guess = input("What is your guess? ").lower()
        if ((guess in word) == False):
            print("""
Wrong!!""")
            no_of_guesses -= 1
            print(f"""You have {no_of_guesses} guesses remaining""")

        elif ((guess in word) == True):
            lister = [index for index, letter in enumerate(word) if letter == guess]
            for num in lister:
                list[num] = guess
            fill = "".join(list)
            print("""
""" + fill)
        used.add(guess)
        oppor = f"""You have used these letters: {used}
"""
        print(oppor)
    del oppor
    if ((fill in word) == True):
        print(f"""Congratulations, You have guessed the word, {worder}, correctly.""")
    elif no_of_guesses == 0:
        print(f"""Unfortunately, you're out of guesses, FAILURE!!""")

hangman(nosses, worder)
