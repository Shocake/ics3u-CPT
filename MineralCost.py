import random
def MineralCost():
    Mineral_Cost = {
        'Stone' : 3.50,
        'Iron' : 1.50,
        'Metal' : 4.00,
        'Wood' : 5.00,
    }
    print("Here are the prices" + str(Mineral_Cost))
    Number = [1, 2, 3, 4, 5]
    a = str(random.choice(Number))
    b = str(random.choice(Number))
    c = str(random.choice(Number))
    d = str(random.choice(Number))

    Answer = float(input("What is the price of  " +  a + " pieces of stone " + b + " pieces of iron " + c + " pieces of metal " + d + " pieces of wood"))
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)

    Total = (a * Mineral_Cost['Stone']) + (b * Mineral_Cost['Iron']) + (c * Mineral_Cost['Metal']) + (d * Mineral_Cost['Wood'])
    if float(Answer) == Total:
        print("hrmmmmsmmmm....ooo!")
        victoryroyale = True
    if float(Answer) != Total:
        victoryroyale = False
    
    return victoryroyale