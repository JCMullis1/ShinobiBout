from maindir.jutsufile import *

# battle field creation using matrix
bfSize = int(input('How big shall the battlefield be? The area will be your input squared: '))
print('')
coords = [[None] * bfSize for _ in range(bfSize)]

jutsuList1 = []
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
    "guard break": ["counter", "block", "dodge"],
    "move": ["block", "dodge"]
}

attack1 = Jutsu("attack", "attack", str, 10, 1)
move1 = Jutsu("move", "move", str, 0, 10000)
guardbreak1 = Jutsu("guard break", "guard break", str, 10, 1)
counter1 = Jutsu("counter", "counter", str, 10, 1)
dodge1 = Jutsu("dodge", "dodge", str, 10, 1)
block1 = Jutsu("block", "block", str, 10, 1)

rlist = [move1, block1, guardbreak1, counter1, dodge1, attack1]

# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, jutsu=list, bline=str, choice=Jutsu):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.playerX = playerX
        self.playerY = playerY
        self.targetX = targetX
        self.targetY = targetY
        self.tired = tired
        self.jutsu = jutsu
        self.bline = bline
        self.choice = choice

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
                break

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
                                        health=playhealth, chakra=playchakra, jutsu=list(rlist), bline=str(input('Enter bloodline: ')))
            playerList.append(globals()[player])
            for juts in range(len(jutsuList)):
                if playerList[playID].bline == jutsuList[juts].bloodline:
                    playerList[playID].jutsu.append(jutsuList[juts])
            customjutsu = int(input("How many custom jutsu would you like to make?: "))
            for cus in range(customjutsu):
                jutsuID = 0
                jutsu = f"jutsu{jutsuID}"
                globals()[jutsu] = Jutsu(name=str(input("Enter jutsu name: ")), dictkey=str(input("Enter jutsu type (element or type of action): ")),
                                         bloodline=playerList[playID].bline, damage=int(input("Enter damage of jutsu: ")),
                                         atrange=int(input("Enter range of jutsu: ")))
                globals()[player].jutsu.append(globals()[jutsu])
                print('')
            playID += 1
            print('')

global playuhs
Shinobi.setplayers()
Shinobi.placeplayers()
# game loop
running = True
while running:
    # turn system
    for i in range(len(playerList)):
        # player death and game over check
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
        print(f'''
    {playerList[i].name}'s turn
        You have {playerList[i].chakra} chakra
               Choose your action!
        ''')
        for g in range(len(playerList[i].jutsu)):
            print(f"{playerList[i].jutsu[g].name}")
        x = str(input("Enter here: ")).strip()
        for y in range(len(playerList[i].jutsu)):
            if x == playerList[i].jutsu[y].name:
                playerList[i].choice = playerList[i].jutsu[y]

        if playerList[i].choice.dictkey == "move":
            a = int(input("How many units do you want to move?: ").strip())
            if a > 3:
                a = 3
            print("Which direction?")
            print("(up~y + input) (down~y - input) (left~x - input) (right~x + input)")
            d = str(input("enter here: ")).strip()
            if d == "up":
                playerList[i].playerY += a
            if d == "down":
                playerList[i].playerY -= a
            if d == "right":
                playerList[i].playerX += a
            if d == "left":
                playerList[i].playerX -= a
            if playerList[i].playerX < 0:
                playerList[i].playerX = 0
            if playerList[i].playerY < 0:
                playerList[i].playerY = 0

        print("Where do you want to attack?")
        print('')
        for j in range(len(playerList)):
            print(f"{playerList[j].name} is at x{playerList[j].playerX}  y{playerList[j].playerY}")
        playerList[i].targetX = int(input("Enter x coordinate: ").strip())
        playerList[i].targetY = int(input("Enter y coordinate: ").strip())
        if playerList[i].playerX - playerList[i].targetX > playerList[i].choice.atrange:
            playerList[i].targetX = int(playerList[i].playerX)
            playerList[i].targetY = int(playerList[i].playerY)

        elif playerList[i].playerY - playerList[i].targetY > playerList[i].choice.atrange:
            playerList[i].targetX = int(playerList[i].playerX)
            playerList[i].targetY = int(playerList[i].playerY)

        print('')
        if playerList[i].choice.dictkey in elementList and playerList[i].chakra >= float(playerList[i].choice.damage*.9):
            playerList[i].chakra -= float(playerList[i].choice.damage*.9)
        elif playerList[i].choice.dictkey in elementList and playerList[i].chakra < float(playerList[i].choice.damage*.9):
            print('Not enough chakra')
            playerList[i].choice = playerList[i].jutsu[1]
            # changes player action to block if they don't have enough chakra
        print('')
        if playerList[i].targetX == playerList[i].playerX and playerList[i].targetY == playerList[i].playerY:
            playerList[i].tired = True

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
                if tempList[0].choice.dictkey in actiondict[playerList[e].choice.dictkey]:
                    if playerList[e].choice.dictkey == playerList[e].element:
                        tempList[0].health -= float(playerList[e].choice.damage*1.5)
                        print(f'''
                        {playerList[e].name} has won the bout!
                        {playerList[e].name} chose {playerList[e].choice.name}, and {tempList[0].name} chose {tempList[0].choice.name}!
                        {playerList[e].name} is now at {playerList[e].health}, and {tempList[0].name} is at {tempList[0].health}!
                        ''')

                    else:
                        tempList[0].health -= float(playerList[e].choice.damage)
                        print(f'''
                        {playerList[e].name} has won the bout!
                        {playerList[e].name} chose {playerList[e].choice.name}, and {tempList[0].name} chose {tempList[0].choice.name}!
                        {playerList[e].name} is now at {playerList[e].health}, and {tempList[0].name} is at {tempList[0].health}!
                        ''')
                # attacker won

                # defender won
                elif playerList[e].choice.dictkey in actiondict[tempList[0].choice.dictkey]:
                    if tempList[0].choice.dictkey == tempList[0].element:
                        playerList[e].health -= float(tempList[0].choice.damage*1.5)
                        print(f'''
                        {tempList[0].name} has won the bout!
                        {tempList[0].name} chose {tempList[0].choice.name}, and {playerList[e].name} chose {playerList[e].choice.name}!
                        {tempList[0].name} is now at {tempList[0].health}, and {playerList[e].name} is at {playerList[e].health}!
                        ''')

                    else:
                        playerList[e].health -= float(tempList[0].choice.damage)
                        print(f'''
                        {tempList[0].name} has won the bout!
                        {tempList[0].name} chose {tempList[0].choice.name}, and {playerList[e].name} chose {playerList[e].choice.name}!
                        {tempList[0].name} is now at {tempList[0].health}, and {playerList[e].name} is at {playerList[e].health}!
                        ''')
                # defender won

                # nobody won
                else:
                    if tempList[0].choice.dictkey == "block" and playerList[e].choice.dictkey == "block":
                        print("Both Shinobi blocked so nothing happened!")
                    else:
                        playerList[e].health -= float(tempList[0].choice.damage)
                        tempList[0].health -= float(playerList[e].choice.damage)
                        print(f'''
                        The bout ended in stalemate!
                        {playerList[e].name} chose {playerList[e].choice.name}, and {tempList[0].name} chose {tempList[0].choice.name}!
                        {tempList[0].name} is now at {tempList[0].health}, and {playerList[e].name} is at {playerList[e].health}!
                        ''')
                # nobody won

            elif playerList[e].tired:
                print(f"{playerList[e].name} is too tired to continue this fight for now.")
                print('')

        else:
            print('you missed!')
            continue