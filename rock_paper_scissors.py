import random

choices = ['rock', 'paper', 'scissors']
end_game = True

def playTurn(user_val, comp_val):
    if user_val == 'paper' and comp_val == 'rock':
        return True
    elif user_val == 'scissors' and comp_val == 'paper':
        return True
    elif user_val == 'rock' and comp_val == 'scissors':
        return True
    return False

def checkWin(end_game):
    if end_game:
        print("You win!")
    else:
        print("You Lost!")

def keepPlaying():
    user_val = " "
    while not (user_val == 'y' or user_val == 'n'):
        try:
            user_val = input("Keep playing (y/n)? >")
        except ValueError:
            print("Re-enter value!")
    if user_val == 'y':
        return True
    return False

while end_game:
    error_chk = True
    comp_val = random.choice(choices)
    while error_chk:
        try:
            user_val = input("Enter 'rock', 'paper' or 'scissors' >")
            if user_val not in choices:
                raise ValueError("Expecting 'rock', 'paper' or 'scissors'. Got " + user_val)
            else:
                error_chk = False
        except ValueError as e:
            print("re-enter value")
            print()
    print("You play " + user_val)
    print("Computer plays " + comp_val)
    end_game = playTurn(user_val,comp_val)
    checkWin(end_game)
    end_game = keepPlaying()
    print()

print("Thanks for playing!")
