import random
def game():
    Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    a = str(random.choice(Number))
    b = str(random.choice(Number))
    Answer = input("What is " +  a + "x" + b + ":")
    Answer = int(Answer)
    a = int(a)
    b = int(b)
    Points = 0
    while int(Answer) > 0:
        if int(Answer) == (int(a) * int(b)):
            Points += 1
            print("You're right! Points:" + str(Points))
            a = str(random.choice(Number))
            b = str(random.choice(Number))
            Answer = input("What is " +  a + "x" + b + ":")
            int(a)
            int(b)
        if Points >= 5:
            print("You won!")
            chikndinr = True
            break
        if int(Answer) != (int(a) * int(b)):
            print("Wrong. Game Over!")
            chikndinr = False
            break
    return chikndinr
game()
