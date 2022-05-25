import random

global n, coords
bfSize = int(input('How big shall the battlefield be? The area will be your input squared:'))
print('')
n = int(bfSize + 1)
b = []
b.extend(range(n))
coords = list([b] * n)


# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int,
                 playX=int, playY=int, speed=int, choice=str):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.playX = playX
        self.playY = playY
        self.speed = speed
        self.choice = choice

    # this just defines the players used in the demo of the game
    @staticmethod
    def setplayers():
        global player, choice, p, bfSize
        playuhs = int((input('How many players will be fighting today?:')))
        playhealth = int(input('how much health will each player have?:'))
        playchakra = int(input('and how much chakra will each player have?'))
        print('')
        y = 0
        p = 1
        bf = 0
        bfp = n/2

        while y != playuhs:
            player = f"player{p}"
            globals()[player] = Shinobi(name=str(input('enter name:')), element=str(input('enter element:')),
                                        health=playhealth, chakra=playchakra, playX=int(bfp + bf), playY=int(bfp + bf),
                                        speed=random.randint(1, 100), choice=str)
            print('')
            bf += 1
            p += 1
            y += 1


global turnList
turnList = []


def coordcheck():
    global coords



def chakraloss():
    global turnList, player

    # picks an element and adds it to a list used for figuring out who won the game


def pickleaction():
    global selectedAction, turnList, player, choice, p
    elementString = "(water) (earth) (fire) (wind) (lightning) (attack) (block) (dodge) (counter) (guard " \
                    "break) (summon)"
    # action selection
    if len(turnList) == 2:
        print("Choose your action!")
        print(elementString)
        selectedAction = (input("enter here:").strip())
        player2.choice = selectedAction
        return player2.choice
    else:
        print("Choose your action!")
        print(elementString)
        selectedAction = (input("enter here:").strip())
        player1.choice = selectedAction
        return player1.choice

    # compares the choices of the players to find a suitable output


def rps():
    global z, player, choice, p
    z = 0
    rpsdict = {
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

    if player2.choice in rpsdict[player1.choice]:
        z += 1
        return
    if player1.choice in rpsdict[player2.choice]:
        z -= 1
        return
    else:
        return


# wincon checks the win condition 'z' to see who won the match
def wincon():
    global player, choice, p, z
    actionString = f"{player1.name} chose {player1.choice} and {player2.name} chose {player2.choice}"

    if z == 1:
        # print(z) debugging
        print(''
              '')
        print(f"{player1.name} has won the round!")
        print(actionString)

        if player1.element == player1.choice:
            player2.health -= 20
            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')

        else:
            player2.health -= 10
            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')

    elif z == -1:
        # print(z) debugging
        print(''
              '')
        print(f"{player2.name} has won the round!")
        print(actionString)

        if player2.element == player2.choice:
            player1.health -= 20
            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')

        else:
            player1.health -= 10
            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')

    else:
        if player1.choice and player2.choice == 'block':
            print(''
                  '')
            print('The round is undecided!')
            print(actionString)

            print('But nothing happened.')

            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')

        else:
            print(''
                  '')
            print('The round is undecided!')
            print(actionString)

            player1.health -= 10
            player2.health -= 10

            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')


# game loop and turn system
def round():
    Shinobi.setplayers()
    global player, turnList, p, choice, health, name

    while player1.health or player2.health > 0:
        if len(turnList) == 2:
            turnList.clear()
        print(f"{player1.name} is at x{player1.playX} y{player1.playY}")
        print(f"{player2.name} is at x{player2.playX} y{player2.playY}")
        print('')
        print(f"{player1.name}\'s turn")
        turnList.append(0)
        pickleaction()

        print('')

        print(f"{player2.name}\'s turn")
        turnList.append(0)
        pickleaction()
        rps()
        wincon()

        if player1.health < 2:
            print(f"Game over! {player2.name} wins!")
            break
        elif player2.health < 2:
            print(f"Game over! {player1.name} wins!")
            break
        else:
            continue


round()
