import random
dayEvents = []
day = 0
exitStatus = ""
playerAction = ""
def makeDays(t):
    for i in range(t):
        dayEvents.append(random.randint(1,3))
def actionMenu():
    print("Attacks [A]  Potions [P]  Spells [S]    Exit [exit]")
    playerAction = input("\nChoose wisely...\n")
    if playerAction == "exit":
        exitStatus = "1"
def ReadDay(d):
    if d >= len(dayEvents):
        makeDays(100)
    else:
        if dayEvents[d] == 1:
            print(f"Nothing happend today... (Day {day})")
        elif dayEvents[d] == 2:
            print("A enemy approaches you!")
            spawnEnemy()
        elif dayEvents[d] == 3:
            findItem()
            # finding text will be in findItem()
def spawnEnemy():
    enemyHealth = 50
    enemyRandBump = 25 * random.randint(0,10)
    enemyHealth *= enemyRandBump
def findItem():
 pass
gameStatus = input("New Game... (Y)\n")
if gameStatus == "Y":
    makeDays(100)
    # print(dayEvents)
# exit = input("Exit?")
while exitStatus != "1":
    ReadDay(day)
    actionMenu()
