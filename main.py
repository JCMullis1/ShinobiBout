import random

bfSize = int(input('How big shall the battlefield be? The area will be your input squared:'))
print('')
global coords
n = int(bfSize + 1)
b = []
b.extend(range(n))
coords = list([b] * bfSize)

# call y before x I think it matters

# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, choice=str, speed=random.randint(1, 100)):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.choice = choice
        self.speed = speed

    # this just defines the players used in the demo of the game
    @staticmethod
    def setplayers():
        global player, choice, p
        playuhs = int((input('How many players will be fighting today?:')))
        playhealth = int(input('how much health will each player have?:'))
        playchakra = int(input('and how much chakra will each player have?'))
        print('')
        y = 0
        p = 1

        while y != playuhs:
            player = f"player{p}"
            globals()[player] = Shinobi(name=str(input('enter name:')), element=str(input('enter element:')),
                                        health=playhealth, chakra=playchakra, choice=str)
            print('')
            p += 1
            y += 1


# the main class with all the stuff happening, it's to define fights and the functions are what regulate it
class Bout:
    def __init__(self, x=int(bfSize), y=int(bfSize)):
        Bout.x = x
        Bout.y = y

    global turnList
    turnList = []

    @staticmethod
    def chakraloss():
        global turnList, player

    # picks an element and adds it to a list used for figuring out who won the game
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def round():
        Shinobi.setplayers()
        global player, turnList, p, choice, health, name

        while player1.health or player2.health > 0:
            if len(turnList) == 2:
                turnList.clear()
            print(f"{player1.name}\'s turn")
            turnList.append(0)
            Bout.pickleaction()

            print('')

            print(f"{player2.name}\'s turn")
            turnList.append(0)
            Bout.pickleaction()
            Bout.rps()
            Bout.wincon()

            if player1.health < 2:
                print(f"Game over! {player2.name} wins!")
                break
            elif player2.health < 2:
                print(f"Game over! {player1.name} wins!")
                break
            else:
                continue


Bout.round()

