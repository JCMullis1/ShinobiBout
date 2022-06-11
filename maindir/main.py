
# battle field creation using matrix
bfSize = int(input('How big shall the battlefield be? The area will be your input squared: '))
print('')
coords = [[None] * bfSize for _ in range(bfSize)]
print(coords)

targetxList = []
targetyList = []
playerList = []
elementList = ["water", "fire", "wind" "lightning", "earth"]

actiondict = {
    "water": ["fire", "attack", "block", "counter", "guard break"],
    "fire": ["wind", "attack", "block", "counter", "guard break"],
    "wind": ["lightning", "attack", "block", "counter", "guard break"],
    "lightning": ["earth", "attack", "block", "counter", "guard break"],
    "earth": ["water", "attack", "block", "counter", "guard break"],
    "counter": ["attack", "dodge"],
    "block": ["attack", "counter"],
    "attack": ["guard break", "dodge"],
    "dodge": ["water", "fire", "wind", "lightning", "earth"],
    "guard break": ["counter", "block", "dodge"]
}

print()
# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, choice=str):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.choice = choice
        self.playerX = playerX
        self.playerY = playerY
        self.targetX = targetX
        self.targetY = targetY
        self.tired = tired

    # places players on the map
    @staticmethod
    def placeplayers():
        y = 0
        x = 0
        for ele in range(len(playerList)):
            coords[x][y] = playerList[ele]
            playerList[ele].playerX = x
            playerList[ele].playerY = y
            x += 1
            if x >= bfSize:
                x -= bfSize
                y += 1
            if y > bfSize:
                print('there is too many players')

    # this just defines the players used in the demo of the game
    @staticmethod
    def setplayers():
        global player, playuhs
        playuhs = int((input('How many players will be fighting today?: ')))
        playhealth = int(input('How much health will each player have?: '))
        playchakra = int(input('How much chakra will each player have?: '))
        print('')
        playID = 0
        for number in range(playuhs):
            player = f"player{playID}"
            globals()[player] = Shinobi(name=str(input('Enter name: ')), element=str(input('Enter element: ')),
                                        health=playhealth, chakra=playchakra, playerX=int, playerY=int, targetX=int,
                                        targetY=int, tired=False, choice=str)
            playerList.append(globals()[player])
            print('')
            playID += 1

# class for jutsu
class Jutsu:
    def __init__(self, dictkey=str, damage=int, atrange=int):
        self.dictkey = dictkey
        self.damage = damage
        self.atrange = atrange

global playuhs
Shinobi.setplayers()
Shinobi.placeplayers()
# game loop
running = True
while running:
    elementString = "(water) (earth) (fire) (wind) (lightning) (attack) (block) (dodge) (counter) (guard " \
                    "break) (summon)"
    # turn system
    for i in range(len(playerList)):
        if playerList[i].health <= 0:
            print(f"It seems {playerList[i].name} has died in combat and can no longer fight...")
            print('')
            playerList.remove(playerList[i])
            if len(playerList) == 1:
                print('game over')
                print(f"{playerList[0].name} has won the match!")
                running = False
                exit(0)
            continue
        playerList[i].tired = False
        print(playerList[i].name + f"'s turn")
        print(f"You have {playerList[i].chakra} chakra")
        print("Choose your action!")
        print(elementString)
        playerList[i].choice = (input("enter here: ").strip())
        if playerList[i].choice == "move":
            # moving not added
            pass
        print("Where do you want to attack?")
        for j in range(len(playerList)):
            print(f"{playerList[j].name} is at x{playerList[j].playerX}  y{playerList[j].playerY}")
        print('')
        playerList[i].targetX = int(input("Enter x coordinate: "))
        playerList[i].targetY = int(input("Enter y coordinate: "))
        targetxList.append(playerList[i].targetX)
        targetyList.append(playerList[i].targetY)

        # add a check to see if attack is out of range

        print('')
        if playerList[i].choice in elementList:
            if playerList[i].chakra <= 0:
                print('Not enough chakra')
                playerList[i].choice = "block"
                continue
            else:
                playerList[i].chakra -= 10
        print('')

    # turn execution
    tempList = []
    for e in range(len(playerList)):
        tempList.clear()

        if coords[playerList[e].targetX][playerList[e].targetY] is not None:
            tempList.append(coords[playerList[e].targetX][playerList[e].targetY])
            if coords[tempList[0].targetX][tempList[0].targetY] == coords[playerList[e].playerX][playerList[e].playerY]:
                tempList[0].tired = True

            if not playerList[e].tired:

                # attacker won
                if tempList[0].choice in actiondict[playerList[e].choice]:
                    if playerList[e].choice == playerList[e].element:
                        tempList[0].health -= 20
                        print(f"{playerList[e].name} has won the bout!")
                        print(
                            f"{playerList[e].name} chose {playerList[e].choice}, and {tempList[0].name} chose {tempList[0].choice}!")
                        print(
                            f"{playerList[e].name} is now at {playerList[e].health}, and {tempList[0].name} is at {tempList[0].health}!")
                        print('')

                    else:
                        tempList[0].health -= 10
                        print(f"{playerList[e].name} has won the bout!")
                        print(
                            f"{playerList[e].name} chose {playerList[e].choice}, and {tempList[0].name} chose {tempList[0].choice}!")
                        print(
                            f"{playerList[e].name} is now at {playerList[e].health}, and {tempList[0].name} is at {tempList[0].health}!")
                        print('')
                # attacker won

                # defender won
                elif playerList[e].choice in actiondict[tempList[0].choice]:
                    if tempList[0].choice == tempList[0].element:
                        playerList[e].health -= 20
                        print(f"{tempList[0].name} has won the bout!")
                        print(
                            f"{tempList[0].name} chose {tempList[0].choice}, and {playerList[e].name} chose {playerList[e].choice}!")
                        print(
                            f"{tempList[0].name} is now at {tempList[0].health}, and {playerList[e].name} is at {playerList[e].health}!")
                        print('')

                    else:
                        playerList[e].health -= 10
                        print(f"{tempList[0].name} has won the bout!")
                        print(
                            f"{tempList[0].name} chose {tempList[0].choice}, and {playerList[e].name} chose {playerList[e].choice}!")
                        print(
                            f"{tempList[0].name} is now at {tempList[0].health}, and {playerList[e].name} is at {playerList[e].health}!")
                        print('')
                # defender won

                # nobody won
                else:
                    if tempList[0].choice and playerList[e].choice == "block":
                        print("Both Shinobi blocked so nothing happened!")
                    else:
                        playerList[e].health -= 10
                        tempList[0].health -= 10
                        print("The bout ended in stalemate!")
                        print(
                            f"{playerList[e].name} chose {playerList[e].choice}, and {tempList[0].name} chose {tempList[0].choice}!")
                        print(
                            f"{tempList[0].name} is now at {tempList[0].health}, and {playerList[e].name} is at {playerList[e].health}!")
                # nobody won

            elif playerList[e].tired:
                print(f"{playerList[e].name} is too tired to continue this fight for now.")
                print('')

        else:
            print('you missed!')
            continue