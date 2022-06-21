from maindir.jutsufile import *

# battle field creation using matrix
bfSize = int(input('How big shall the battlefield be? The area will be your input squared: '))
print('')
coords = [[None] * bfSize for _ in range(bfSize)]

choiceList = []
playerList = []
elementList = ["water", "fire", "wind" "lightning", "earth"]

contextdict = {
    "move": ["move", "dodge"],
    "defend": ["block", "guard break", "counter"],
    "strike": ["attack"],
    "chakra": ["water", "earth", "fire", "lightning", "wind", "summon"],
    "nothing": ["nothing"]
}

weapondict = {
    "sword": ["heavy", "fists"],
    "heavy": ["polearm", "fists"],
    "polearm": ["sword", "fists"],
    "kunai": ["shuriken", "fists"],
    "shuriken": ["paper bomb", "fists"],
    "paper bomb": ["kunai", "fists"],
    "fists": [""]
}

racedict = {
    "serpent": ["slug"],
    "toad": ["serpent"],
    "slug": ["toad"],
    "monkey": ["hound"],
    "hound": ["hawk"],
    "hawk": ["monkey"]
}

# keys are actions and the values are the actions that they defeat
actiondict = {
    "water": ["fire", "attack", "block", "counter", "guard break", "summon", "move", "nothing"],
    "fire": ["wind", "attack", "block", "counter", "guard break", "summon", "move", "nothing"],
    "wind": ["lightning", "attack", "block", "counter", "guard break", "summon", "move", "nothing"],
    "lightning": ["earth", "attack", "block", "counter", "guard break", "summon", "move", "nothing"],
    "earth": ["water", "attack", "block", "counter", "guard break", "summon", "move", "nothing"],
    "counter": ["attack", "dodge", "nothing"],
    "block": ["attack", "counter"],
    "attack": ["guard break", "dodge", "summon", "nothing"],
    "dodge": ["water", "fire", "wind", "lightning", "earth"],
    "guard break": ["counter", "block", "dodge", "nothing"],
    "move": ["block", "dodge"],
    "summon": ["nothing"],
    "nothing": [""]
}

attack1 = Jutsu("attack", "attack", str, 10, 2)
move1 = Jutsu("move", "move", str, 0, 10000)
guardbreak1 = Jutsu("guard break", "guard break", str, 10, 2)
counter1 = Jutsu("counter", "counter", str, 10, 2)
dodge1 = Jutsu("dodge", "dodge", str, 10, 2)
block1 = Jutsu("block", "block", str, 10, 2)
summon1 = Jutsu("summon", "summon", str, 0, 3, 40)

fists1 = Weapon(name="fists", weaponkey="fists", amount=1, damage=10, atrange=2)
kunai1 = Weapon(name="kunai", weaponkey="kunai", isranged=True, amount=4, damage=16, atrange=4)
shuriken1 = Weapon(name="shuriken", weaponkey="shuriken", isranged=True, amount=6, damage=12, atrange=6)
paperbomb1 = Weapon(name="paper bomb", weaponkey="paper Bomb", isranged=False)

jlist = [move1, block1, guardbreak1, counter1, dodge1, attack1, summon1]

wlist = [kunai1, shuriken1, paperbomb1]

# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, jutsu=list, bline=str, inventory=list, context=str, weapon=Weapon, choice=Jutsu):
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
        self.inventory = inventory
        self.context = context
        self.weapon = weapon
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
            if x == bfSize:
                x -= bfSize
                y += 1
            if y > bfSize:
                print('there is too many players')
                break

    # this just defines the players used in the demo of the game
    @staticmethod
    def setplayers():
        global player, playuhs, playhealth, playchakra
        playuhs = int(input('How many players will be fighting today?: '))
        playhealth = int(input('How much health will each player have?: '))
        playchakra = int(input('How much chakra will each player have?: '))
        print('')
        playID = 0
        for number in range(playuhs):
            player = f"player{playID}"
            globals()[player] = Shinobi(name=str(input('Enter name: ')), element=str(input('Enter element: ')),
                                        health=playhealth, chakra=playchakra, jutsu=list(jlist), inventory=list(wlist), bline=str(input('Enter bloodline: ')))
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
    # player death and game over check
    for b in range(len(playerList)):
        if playerList[b].health <= 0:
            print(f"It seems {playerList[b].name} has died in combat and can no longer fight...")
            print('')
            playerList.remove(playerList[b])
            if len(playerList) == 1:
                print('game over')
                print(f"{playerList[0].name} has won the match!")
                running = False
                exit(0)
        continue

    # context turn
    for q in range(len(playerList)):
        playerList[q].tired = False
        playerList[q].context = "nothing"
        print(f'''
        {playerList[q].name}'s turn
            You have {playerList[q].chakra} chakra
                   Choose your action!
            ''')
        print('(move) (defend) (strike) (chakra)')
        playerList[q].context = str(input("Enter here: ")).strip()
        print('')

    # turn system
    for i in range(len(playerList)):
        # context actions
        for o in range(len(playerList)):
            if int(playerList[i].playerX) > int(playerList[o].playerX):
                a = int(playerList[i].playerX)
                b = int(playerList[o].playerX)
            else:
                a = int(playerList[o].playerX)
                b = int(playerList[i].playerX)
            if int(playerList[i].playerY) > int(playerList[o].playerY):
                c = int(playerList[i].playerY)
                d = int(playerList[o].playerY)
            else:
                c = int(playerList[o].playerY)
                d = int(playerList[i].playerY)

            if a - b <= 5 or c - d <= 5:
                if playerList[o].context == "move":
                    print(f'{playerList[o].name} is getting ready to move!')
                elif playerList[o].context == "defend":
                    print(f'{playerList[o].name} is preparing a defense!')
                elif playerList[o].context == "strike":
                    print(f'{playerList[o].name} is preparing an attack!')
                elif playerList[o].context == "chakra":
                    print(f'{playerList[o].name} is weaving hand signs!')
                elif playerList[o].context == "nothing":
                    print(f'{playerList[o].name} hasn\'t done anything yet!')
                print('')

        print(f'''
    {playerList[i].name}'s turn
        You have {playerList[i].chakra} chakra
               Choose your action!
               ''')
        for g in range(len(playerList[i].jutsu)):
            if playerList[i].jutsu[g].dictkey in contextdict[playerList[i].context]:
                choiceList.append(str(playerList[i].jutsu[g].dictkey))
                print(playerList[i].jutsu[g].name)

        going = True
        while going:
            x = str(input("Enter here: ")).strip()
            for y in range(len(playerList[i].jutsu)):
                if x == playerList[i].jutsu[y].name:
                    if playerList[i].jutsu[y].dictkey in choiceList:
                        playerList[i].choice = playerList[i].jutsu[y]
                        going = False

        if playerList[i].choice.dictkey == "summon":
            print('')
            summon = f"summon{int(len(playerList)+1)}"
            globals()[summon] = Summon(race=str(input('Enter summon race: ')), name=str(input('Enter summon name: ')), element=str(input('Enter summon element: ')),
                                       health=playhealth, chakra=playchakra, jutsu=list(jlist),
                                       bline=str(input('Enter bloodline: ')))
            playerList.append(globals()[summon])
            for juts in range(len(jutsuList)):
                if playerList[len(playerList)-1].bline == jutsuList[juts].bloodline:
                    playerList[len(playerList)-1].jutsu.append(jutsuList[juts])
            playerList[len(playerList)-1].jutsu.remove(summon1)
            playerList[int(len(playerList)-1)].choice = Jutsu("nothing", "nothing", str, 0, 100)

        if playerList[i].choice.dictkey == "move":
            prevX = playerList[i].playerX
            prevY = playerList[i].playerY
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
            coords[prevX][prevY] = None

        print("Where do you want to attack?")
        print('')
        for j in range(len(playerList)):
            if int(playerList[i].playerX) > int(playerList[j].playerX):
                a = int(playerList[i].playerX)
                b = int(playerList[j].playerX)
            else:
                a = int(playerList[j].playerX)
                b = int(playerList[i].playerX)
            if int(playerList[i].playerY) > int(playerList[j].playerY):
                c = int(playerList[i].playerY)
                d = int(playerList[j].playerY)
            else:
                c = int(playerList[j].playerY)
                d = int(playerList[i].playerY)

            if a - b <= 5 and c - d <= 5:
                print(f"{playerList[j].name} is at x{playerList[j].playerX}  y{playerList[j].playerY}")
        playerList[i].targetX = int(input("Enter x coordinate: ").strip())
        playerList[i].targetY = int(input("Enter y coordinate: ").strip())

        if playerList[i].choice.dictkey == "summon":
            coords[playerList[i].targetX][playerList[i].targetY] = playerList[int(len(playerList) - 1)]
            playerList[int(len(playerList)-1)].playerX = playerList[i].targetX
            playerList[int(len(playerList)-1)].playerY = playerList[i].targetY
            playerList[int(len(playerList)-1)].targetX = playerList[i].targetX
            playerList[int(len(playerList)-1)].targetY = playerList[i].targetY

        if playerList[i].playerY - playerList[i].targetY > playerList[i].choice.atrange:
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
        if coords[playerList[i].targetX][playerList[i].targetY] == playerList[i]:
            playerList[i].tired = True
    # playerList[i].targetX == playerList[i].playerX and playerList[i].targetY == playerList[i].playerY

    # turn execution
    tempList = []
    for e in range(len(playerList)):
        tempList.clear()

        if playerList[e].choice.dictkey not in actiondict:
            continue
        # coords[playerList[e].playerX][playerList[e].playerY]
        if coords[playerList[e].targetX][playerList[e].targetY] is not None:
            tempList.append(coords[playerList[e].targetX][playerList[e].targetY])
            if coords[tempList[0].targetX][tempList[0].targetY] == playerList[e]:
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
