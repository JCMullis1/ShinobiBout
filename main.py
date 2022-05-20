
bfSize = int(input('How big shall the battlefield be? The area will be your input squared:'))


# call y before x I think it matters


# defining players
class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, choice=str):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.choice = choice

    # this just defines the players used in the demo of the game
    @staticmethod
    def setplayers():
        global player, choice, p
        playuhs = int((input('How many players will be fighting today?:')))
        print(f"there will be {playuhs} players")
        playhealth = int(input('how much health will each player have?:'))
        playchakra = int(input('and how much chakra will each player have?'))
        y = 0
        p = 1

        while y != playuhs:
            player = f"player{p}"
            globals()[player] = Shinobi(name=str(input('enter name:')), element=str(input('enter element:')),
                                        health=playhealth, chakra=playchakra, choice=str)
            p += 1
            y += 1


# the main class with all the stuff happening, it's to define fights and the functions are what regulate it
class Bout:
    def __init__(self, x=int(bfSize), y=int(bfSize)):
        Bout.x = x
        Bout.y = y

    global letterChoice
    letterChoice = []

    @staticmethod
    def chakraloss():
        global letterChoice, player

    # picks an element and adds it to a list used for figuring out who won the game
    @staticmethod
    def pickleaction():
        global selectedAction, letterChoice, player, choice, p

        # this just checks the answer given in the round method, depending on the answer it changes the options given
        # to the player
        if len(letterChoice) == 2:
            if letterChoice[1] == 'A':
                print("Choose your attack!")
                print("(water) (earth) (fire) (wind) (lightning) (attack)")
                selectedAction = str((input("enter here:")))
                player2.choice = str(selectedAction)
                return player2.choice

            if letterChoice[1] == 'B':
                print("Choose your defense!")
                print("(block) (dodge) (counter)")
                selectedAction = str((input("enter here:")))
                player2.choice = str(selectedAction)
                return player2.choice

            if letterChoice[1] == 'C':
                print("Choose your special action!")
                print("(summon) (guard break)")
                selectedAction = str((input("enter here:")))
                player2.choice = str(selectedAction)
                return player2.choice
        else:
            if letterChoice[0] == 'A':
                print("Choose your attack!")
                print("(water) (earth) (fire) (wind) (lightning) (attack)")
                selectedAction = str((input("enter here:")))
                player1.choice = str(selectedAction)
                return player1.choice

            if letterChoice[0] == 'B':
                print("Choose your defense!")
                print("(block) (dodge) (counter)")
                selectedAction = str((input("enter here:")))
                player1.choice = str(selectedAction)
                return player1.choice

            if letterChoice[0] == 'C':
                print("Choose your special action!")
                print("(summon) (guard break)")
                selectedAction = str((input("enter here:")))
                player1.choice = str(selectedAction)
                return player1.choice

    # compares the choices of the players to find a suitable output
    @staticmethod
    def rps():
        global z, player, choice, p
        z = 0

        # element checks
        if player1.choice == 'water' and player2.choice == 'fire':
            z += 1
        elif player1.choice == 'fire' and player2.choice == 'water':
            z -= 1
        elif player1.choice == 'fire' and player2.choice == 'wind':
            z += 1
        elif player1.choice == 'wind' and player2.choice == 'fire':
            z -= 1
        elif player1.choice == 'wind' and player2.choice == 'lightning':
            z += 1
        elif player1.choice == 'lightning' and player2.choice == 'wind':
            z -= 1
        elif player1.choice == 'lightning' and player2.choice == 'earth':
            z += 1
        elif player1.choice == 'earth' and player2.choice == 'lightning':
            z -= 1
        elif player1.choice == 'earth' and player2.choice == 'water':
            z += 1
        elif player1.choice == 'water' and player2.choice == 'earth':
            z -= 1

        # basic attack checks
        elif player1.choice == 'water' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'water':
            z -= 1
        elif player1.choice == 'fire' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'fire':
            z -= 1
        elif player1.choice == 'wind' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'wind':
            z -= 1
        elif player1.choice == 'lightning' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'lightning':
            z -= 1
        elif player1.choice == 'earth' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'earth':
            z -= 1
        elif player1.choice == 'block' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'block':
            z -= 1
        elif player1.choice == 'counter' and player2.choice == 'attack':
            z += 1
        elif player1.choice == 'attack' and player2.choice == 'counter':
            z -= 1

        # block checks
        elif player1.choice == 'water' and player2.choice == 'block':
            z += 1
        elif player1.choice == 'block' and player2.choice == 'water':
            z -= 1
        elif player1.choice == 'earth' and player2.choice == 'block':
            z += 1
        elif player1.choice == 'block' and player2.choice == 'earth':
            z -= 1
        elif player1.choice == 'fire' and player2.choice == 'block':
            z += 1
        elif player1.choice == 'block' and player2.choice == 'fire':
            z -= 1
        elif player1.choice == 'wind' and player2.choice == 'block':
            z += 1
        elif player1.choice == 'block' and player2.choice == 'wind':
            z -= 1
        elif player1.choice == 'lightning' and player2.choice == 'block':
            z += 1
        elif player1.choice == 'block' and player2.choice == 'lightning':
            z -= 1

        # dodge checks
        elif player1.choice == 'water' and player2.choice == 'dodge':
            z -= 1
        elif player1.choice == 'dodge' and player2.choice == 'water':
            z += 1
        elif player1.choice == 'earth' and player2.choice == 'dodge':
            z -= 1
        elif player1.choice == 'dodge' and player2.choice == 'earth':
            z += 1
        elif player1.choice == 'fire' and player2.choice == 'dodge':
            z -= 1
        elif player1.choice == 'dodge' and player2.choice == 'fire':
            z += 1
        elif player1.choice == 'wind' and player2.choice == 'dodge':
            z -= 1
        elif player1.choice == 'dodge' and player2.choice == 'wind':
            z += 1
        elif player1.choice == 'lightning' and player2.choice == 'dodge':
            z -= 1
        elif player1.choice == 'dodge' and player2.choice == 'lightning':
            z += 1

        # counter checks
        elif player1.choice == 'counter' and player2.choice == 'water':
            z -= 1
        elif player1.choice == 'water' and player2.choice == 'counter':
            z += 1
        elif player1.choice == 'counter' and player2.choice == 'fire':
            z -= 1
        elif player1.choice == 'fire' and player2.choice == 'counter':
            z += 1
        elif player1.choice == 'counter' and player2.choice == 'wind':
            z -= 1
        elif player1.choice == 'wind' and player2.choice == 'counter':
            z += 1
        elif player1.choice == 'counter' and player2.choice == 'lightning':
            z -= 1
        elif player1.choice == 'lightning' and player2.choice == 'counter':
            z += 1
        elif player1.choice == 'counter' and player2.choice == 'earth':
            z -= 1
        elif player1.choice == 'earth' and player2.choice == 'counter':
            z += 1
        elif player1.choice == 'counter' and player2.choice == 'block':
            z -= 1
        elif player1.choice == 'wind' and player2.choice == 'counter':
            z += 1
        elif player1.choice == 'counter' and player2.choice == 'block':
            z -= 1
        elif player1.choice == 'block' and player2.choice == 'counter':
            z += 1

        # print(z) this print statement is used for debugging
        return

    # wincon checks the win condition 'z' to see who won the match
    @staticmethod
    def wincon():
        global player, choice, p, z

        if z == 1:
            # print(z) debugging
            print(''
                  '')
            print(f"{player1.name} has won the round!")
            print(f"{player1.name} chose {player1.choice} and {player2.name} chose {player2.choice}")

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
            print(f"{player1.name} chose {player1.choice} and {player2.name} chose {player2.choice}")

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
                print(f"{player1.name} chose {player1.choice} and {player2.name} chose {player2.choice}")

                print('But nothing happened.')

                print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                      f"{player2.health} health!")
                print('')

            else:
                print(''
                      '')
                print('The round is undecided!')
                print(f"{player1.name} chose {player1.choice} and {player2.name} chose {player2.choice}")

                player1.health -= 10
                player2.health -= 10

                print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                      f"{player2.health} health!")
                print('')

    # game loop and turn system
    @staticmethod
    def round():
        Shinobi.setplayers()
        global player, letterChoice, p, choice

        while player1.health or player2.health > 0:
            if len(letterChoice) == 2:
                letterChoice.clear()
            print(f"{player1.name}\'s turn")
            print("pick your action")
            print("(A for attack options) or (B for defensive options) or (C for special options)")
            answer = str(input('enter here:'))
            letterChoice.append(answer)
            Bout.pickleaction()

            print('')

            print(f"{player2.name}\'s turn")
            print("pick your action")
            print("(A for attack options) or (B for defensive options) or (C for special options)")
            answer2 = str(input('enter here:'))
            letterChoice.append(answer2)
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


# making the dynamic matrix
n = int(bfSize+1)
b = []
b.extend(range(n))
a = list([b]*bfSize)
print(a)

Bout.round()

