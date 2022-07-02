from maindir.classfile import *

# battle field creation using matrix
bfSize = int(input('How big shall the battlefield be? The area will be your input squared: '))
print('')
coords = [[None] * bfSize for _ in range(bfSize)]
healthChakra()

global playuhs, players
Shinobi.setplayers()
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


def whereYouAt():
    for j in range(len(playerList)):
        if playerList[i].playerX > playerList[j].playerX:
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
    if playerList[i].playerY - playerList[i].targetY > playerList[i].choice.atrange:
        playerList[i].targetX = int(playerList[i].playerX)
        playerList[i].targetY = int(playerList[i].playerY)


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
        playerList[q].specaction = False
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
            if playerList[i].playerX > playerList[o].playerX:
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
                        if playerList[i].jutsu[y].dictkey == "attack":
                            playerList[i].weapon = playerList[i].jutsu[y]
                            playerList[i].weapon.amount = playerList[i].itamount[playerList[i].weapon.position]
                            print(
                                f'{playerList[i].name} has {playerList[i].weapon.amount} {playerList[i].weapon.name}.')
                            if playerList[i].weapon.amount <= 0:
                                print(f'You couldn\'t find {playerList[i].weapon.name} in your inventory.')
                                playerList[i].weapon = fists1
                                playerList[i].choice = fists1
                                going = False
                            if playerList[i].weapon.weaponkey == "kunai":
                                playerList[i].weapon.atrange = 2
                                thrown = input('Do you want to throw the kunai? (Y/N): ')
                                if thrown == 'Y':
                                    playerList[i].itamount[playerList[i].weapon.position] -= 1
                                    playerList[i].weapon.atrange = 4
                                    going = False
                            elif playerList[i].weapon.isranged is True:
                                playerList[i].weapon.amount -= 1
                            going = False
                        going = False

        if playerList[i].choice.dictkey == "transform":
            print('')
            print('(weapon) (object) (other person)')
            form = str(input('What form will you take?: '))
            if form == "weapon":
                trweaponID = 0
                rangedBool = False
                areYouRanged = str(input("Is your weapon transformation ranged? (Y/N): "))
                if areYouRanged == "Y":
                    rangedBool = True
                print("""Enter type of weapon
                (sword) (heavy) (polearm) (kunai) (shuriken) (paper bomb)""")
                weaponType = str(input("Enter Here: "))
                if weaponType == "sword":
                    rangeValue = 2
                elif weaponType == "heavy":
                    rangeValue = 2
                elif weaponType == "polearm":
                    rangeValue = 3
                elif weaponType == "kunai":
                    rangeValue = 2
                elif weaponType == "shuriken":
                    rangeValue = 5
                elif weaponType == "paper bomb":
                    rangeValue = 2
                weaponList = []
                trweapon = f"trweapon{trweaponID}"
                globals()[trweapon] = Weapon(name=playerList[i].name,
                                             buff=str(input("Enter weapon buff: ")),
                                             buffamount=str(input("Enter buff amount: ")),
                                             istransform=True,
                                             chakra=playerList[i].chakra,
                                             weaponkey=weaponType,
                                             isranged=rangedBool,
                                             amount=1,
                                             damage=int(input("How much damage will the weapon do?: ")),
                                             atrange=rangeValue,
                                             position=int(len(amountList)-1),
                                             weaponX=playerList[i].playerX,
                                             weaponY=playerList[i].playerY)
                weaponList.append(globals()[trweapon])
                print(f"Who do you want to equip yourself to?")
                whereYouAt()
                plaholX = int(playerList[i].targetX)
                plaholY = int(playerList[i].targetY)
                if coords[plaholX][plaholY] is not None:
                    for weapon in range(len(weaponList)):
                        if weaponList[weapon].name == playerList[i].name:
                            for v in range(len(playerList)):
                                if coords[plaholX][plaholY].name == playerList[v].name:
                                    acceptWeapon = input(str(f"{playerList[v].name} do you want to equip {playerList[i].name} as a weapon? (Y/N): "))
                                    if acceptWeapon == "Y":
                                        playerList[v].weapon = weaponList[weapon]
                                        print(playerList[v].weapon.name)
                                        playerList[v].jutsu.append(weaponList[weapon])
                playerList[i].specaction = True

        if playerList[i].choice.dictkey == "summon":
            print('')
            summoning()
            for juts in range(len(jutsuList)):
                if playerList[latestPlayer].bline == jutsuList[juts].bloodline:
                    playerList[latestPlayer].jutsu.append(jutsuList[juts])
            customjutsu = int(input(f"How many custom jutsu would {playerList[latestPlayer].name} like to make?: "))
            for cus in range(customjutsu):
                jutsuID = 0
                jutsu = f"jutsu{jutsuID}"
                globals()[jutsu] = Jutsu(name=str(input("Enter jutsu name: ")),
                                         dictkey=str(input("Enter jutsu type (element or type of action): ")),
                                         bloodline=playerList[latestPlayer].bline,
                                         damage=int(input("Enter damage of jutsu: ")),
                                         atrange=int(input("Enter range of jutsu: ")))
                playerList[latestPlayer].jutsu.append(globals()[jutsu])
                print('')
                jutsuID += 1
            playerList[latestPlayer].jutsu.remove(summon1)
            playerList[latestPlayer].choice = Jutsu("nothing", "nothing", str, 0, 100)
            playerList[latestPlayer].playerX = int(
                input(f'Where (x) do you want to summon {playerList[latestPlayer].name}: '))
            playerList[latestPlayer].playerY = int(
                input(f'Where (y) do you want to summon {playerList[latestPlayer].name}: '))
            playerList[latestPlayer].targetX = playerList[latestPlayer].playerX
            playerList[latestPlayer].targetY = playerList[latestPlayer].playerY
            playerList[i].targetX = playerList[latestPlayer].playerX
            playerList[i].targetY = playerList[latestPlayer].playerY
            coords[playerList[i].targetX][playerList[i].targetY] = playerList[latestPlayer]
            playerList[i].specaction = True

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
            playerList[i].targetX = playerList[i].playerX
            playerList[i].targetY = playerList[i].playerY
            playerList[i].specaction = True

        if playerList[i].specaction != True:
            print("Where do you want to attack?")
            print('')
            whereYouAt()

        print('')
        if playerList[i].choice.dictkey in elementList and playerList[i].chakra >= float(
                playerList[i].choice.damage * .9):
            playerList[i].chakra -= float(playerList[i].choice.damage * .9)
        elif playerList[i].choice.dictkey in elementList and playerList[i].chakra < float(
                playerList[i].choice.damage * .9):
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

        if coords[playerList[e].targetX][playerList[e].targetY] is not None:
            tempList.append(coords[playerList[e].targetX][playerList[e].targetY])
            if coords[tempList[0].targetX][tempList[0].targetY] == playerList[e]:
                tempList[0].tired = True

            if not playerList[e].tired:

                # attacker won
                if tempList[0].choice.dictkey in actiondict[playerList[e].choice.dictkey]:
                    if playerList[e].choice.dictkey == playerList[e].element:
                        tempList[0].health -= float(playerList[e].choice.damage * 1.5)
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
                        playerList[e].health -= float(tempList[0].choice.damage * 1.5)
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
