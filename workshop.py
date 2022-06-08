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


# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, choice=str):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.choice = choice
        self.playerX = playerX
        self.playerY = playerY
        self.targetX = targetX
        self.targetY = targetY

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
                                        targetY=int, choice=str)
            playerList.append(globals()[player])
            print('')
            playID += 1


Shinobi.setplayers()
# game loop
global playuhs
Shinobi.placeplayers()
print(coords)
while True:
    elementString = "(water) (earth) (fire) (wind) (lightning) (attack) (block) (dodge) (counter) (guard " \
                    "break) (summon)"
    # turn system
    for i in range(len(playerList)):
        print(playerList[i].name + f"'s turn")
        print("Choose your action!")
        print(elementString)
        playerList[i].choice = (input("enter here: ").strip())
        if playerList[i].choice in elementList:
            playerList[i].chakra -= 10
        print("Where do you want to attack?")
        for j in range(len(playerList)):
            print(f"{playerList[j].name} is at x{playerList[j].playerX}  y{playerList[j].playerY}")
        print('')
        targetX = int(input("Enter x coordinate: "))
        targetY = int(input("Enter y coordinate: "))
        targetxList.append(targetX)
        targetyList.append(targetY)
        print('')
        if playerList[i].choice in elementList:
            playerList[i].chakra -= 10
        print('')

    tempList = []
    for e in range(len(playerList)):
        tempList.clear()
        playerPosX = playerList[e].playerX
        playerPosY = playerList[e].playerY
        playerTarX = targetxList[e]
        playerTarY = targetyList[e]
        if coords[playerTarX][playerTarY] is not None:
            tempList.append(coords[playerTarX][playerTarY])
            if tempList[0].choice in actiondict[playerList[e].choice]:
                # add the health losses and print statement abusing for the attacker winning
                print('attacker won i think')
            elif playerList[e].choice in actiondict[tempList[0].choice]:
                # defending player won
                print('defender won i think')
            else:
                print('nobody won or this didnt work')
