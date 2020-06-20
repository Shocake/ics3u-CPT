import random

def Opposite_game():
    Opposite = {'Up': 'Down', 'Left': 'Right','Fast':'Slow','First': 'Last', 'Happy':'Sad', 'Big':'Small', 'Light':'Dark', 'Tall':'Short', 'Night':'Day'}
    Answer1 = random.choice(list(Opposite.values()))
    Answer = str(input("What is the opposite of: "+ Answer1 + "?"))
    if Answer in ['Up', 'Left', 'Fast']:
        print("You're Right! You Won!")
    elif Answer in [ 'First', 'Happy', 'Big']:
        print("You're Right! You Won!")
    elif Answer in [ 'Light', 'Tall', 'Night']:
        print("You're Right! You Won!")
    else:
        print("Wrong. Game Over!")
Opposite_game()
