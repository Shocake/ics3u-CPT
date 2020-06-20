import sys, time, MultiplicationGame, MineralCost, OppositeGame #As Joseph and I worked together, importing was useful to organize and share code

#This function makes the print statements come slowly and make them easy to take in
def delay(str):
    print(str)
    time.sleep(1.5)

name = input("What is your Name?")
delay(name + " had been exploring the cosmos in search of meaning, but the ship crashed into a meteorite, forcing the ship to crash land on Planet Z.")
delay(".....")
delay(".......")
time.sleep(1)
delay("You wake up in an escape pod, and see your broken ship in the distance.")
print("*REBOOTING SYSTEMS*")
time.sleep(0.1)
print("*REBOOTING SYSTEMS*")
time.sleep(0.1)
print("*REBOOTING SYSTEMS*")
time.sleep(0.1)
print("*REBOOTING SYSTEMS*")
time.sleep(0.1)
print("*REBOOTING SYSTEMS*")
time.sleep(0.1)
delay("*User " + name + ", systems are damaged. It seems you have crashed your spacecraft. I, EVA am still able to assist you through your earpiece.")
delay("To commence protocol REPAIRSHIP, you will have to search this alien planet for resources. You will need tin, gold, and hellstone.*")
delay("*Scanning for material in the area*")
delay("---^^^_____^----^")
print("*I have found [3 COUNTS] of relevant material in the vicinity. You can find tin on a mountain, [2 KM] north.*")
decision = input("*Commence? Y/N*")
if decision == "N":
    print("You lived a lonely life on Planet Z, surviving off solely potatoes... The End.")
    sys.exit()#sys.exit() will end the game
delay("You arrive at the mountain.")
delay("You walk into a cave, but there seems to be some sort of technology blocking off many stores of tin.")
delay("*USER [" + name + "], there seems to be some sort of primitive computer hooked up to the gate.*")
choice1 = input("Do you want to [1]: Break the gate or [2]: Tinker with the computer")
if choice1 == "1":
    print("You burn a whole through it with a high power laser, but it the computer shoots back... The End.")
    sys.exit()
if choice1 == "2":
    delay("The computer wants you to play a game...")
    delay("Apparently, the creatures it wants to keep out aren't too good at math. It's a math game.")
if MultiplicationGame.game() == False:
    print("You are liquified by a large green laser. The End.")
    sys.exit()
delay("The gate opens.")
delay("*We may now collect all the tin we need. This will be enough for protocol REPAIRSHIP.*")

#Second task
delay("*Next, we must infiltrate a nearby Alien warehouse to obtain gold.*")
delay("You find a uniform lying in a trashcan at the back of the warehouse. This will have to do.")
delay("*Stench levels are high. Proceed with caution*")
delay("You walk into the warehouse. Its packed and no one pays too much attention to you.")
delay("You get tapped on the shoulder. An alien asks you to do some calculations for him. It is in an alien language.")
animal = input("*I can translate this for you if you tell me which animal is better: TURTLES or DUCKS")
if animal == "DUCKS":
    print("*That doesn't match up. Try again.*")
    animal2 = input("*Which animal is better: [TURTLES] or [DUCKS]*")#Because turtles are much cuter than ducks obviously
    if animal == "DUCKS":
        print("The translations fail and you are caught.")
        sys.exit()
if animal == "TURTLES":
    print("Translation successful.")
if MineralCost.MineralCost() == False:
    delay("Sniff*")
    delay("....")
    delay("RASDkkkDioaLL..")
    delay("DJSAIODJADOWAJ")
    delay("You end up in a prison. The End.")
    sys.exit()
delay("*The gold is in the back room. It should be smooth sailing from here.*")
delay("You pick up the gold and walk out the back door.")
delay("*One more task left for completion.")

#Third task
delay("*The hellstone is locked deep inside a vault, as it is a very volatile substance. We will have to crack the vault's puzzles.*")
delay("*I can solve the logical problems, but you will have to solve the simple problems. They are so simple that the developers saw no need to account for them.*")
if OppositeGame.Opposite_game() == False:
    print("The alarm was triggered. You were made into lunch meat.")
    sys.exit()
delay("You were able to get in an out with the hellstone without triggering a single alarm.")
delay("*Congratulations, User " + name + "! You will now be able to initiate protocol REPAIRSHIP!*")
delay("After a week, your ship was repaired back into pristine condition.")
delay("The ship took off, and you flew into the dark abyss that is space.")
delay("However, you forgot something...")
delay("The fuel...")