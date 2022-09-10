# GAME(ORGANIZER-VIRAT.KUMAR)***** ROCK-PAPER-SCISSOR ****
# 1.RULES:- EXAMPLE--> IF A = PAPER,AND B=SCISSOR THEN B WILL CUT A'S PAPER
# 2.RULES:- EXAMPLE--> IF A = PAPER,AND B=GUN THEN B WILL DESTROY A'S PAPER(BECAUSE GUN IS POWERFULL THAN PAPER)
# 3.RULES:- EXAMPLE--> IF A = PAPER,AND B=ROCK THEN A WILL FOLD THAT ROCK WITHIN IT
# 4.RULES:- EXAMPLE--> IF A=B THEN RESULT WILL BE DRAW !
import random


def gameWin(comp, you):
    # If two values are equal, declare a Draw !
    if comp == you:
        return None

    # Check for all possibilities when computer chose rock(r)
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    # Check for all possibilities when computer chose p(paper)
    elif comp == 'p':
        if you == 's':
            return True
    elif comp == 'p':
        if you == 'g':
            return True
    elif comp == 'p':
        if you == 'r':
            return True

        # elif you == 'r':
        #     return False

    # Check for all possibilities when computer chose s(scissor)
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print("Comp Turn: rock(r) paper(p) or scissor(s)?\n")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: rock(r) paper(p) or scissor(s))?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("Draw !")
elif a:
    print("You Win! Because You Chose right One ! ")
else:
    print("You Lose! Keep Trying *")
