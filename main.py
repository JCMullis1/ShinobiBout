import random


class Shinobi:
    def __init__(self, name=str, element=str, health=int):
        self.name = name
        self.element = element
        self.health = health

    def setplayers(self):
        name1 = str(input('enter name:'))
        element1 = str(input('element:'))
        health1 = int(input('health:'))

        name2 = str(input('enter name:'))
        element2 = str(input('element:'))
        health2 = int(input('health:'))

        global player1
        global player2

        player1 = Shinobi(name1, element1, health1)
        player2 = Shinobi(name2, element2, health2)
        return player1
        return player2


class Bout:
    def __init__(self):
        return

    global choiceList
    global letterChoice
    global actionTuple
    letterChoice = []
    choiceList = []
    actionTuple = ('water', 'earth', 'fire', 'wind', 'lightning', 'attack', 'block', 'dodge', 'counter', 'summon')

    # changed for clear method but still make some dynamic gameplay and if there are more players you could make the
    # check a variable depending on how many players are added to the game remember to make it where the choiceList
    # adds a Null element to make sure that if two players pick different choices but player 2 did block it allows
    # block without fetching the 0 position

    # picks an element and adds it to a list used for figuring out who won the game
    @staticmethod
    def pickleaction():
        global selectedAction
        global choiceList
        global letterChoice

        # figure out a way to go back to the selection so they aren't stuck if they made a mistake
        # potentially make it give an answer that if it is equal to it will send it back to the while loop returning them to the previous if statement

        if letterChoice[0] == 'A':
            print("Choose your attack!")
            print("0(water) 1(earth) 2(fire) 3(wind) 4(lightning) 5(basic attack)")
            selectedAction = int((input("enter here:")))
            letterChoice.clear()
            choiceList.append(selectedAction)

        elif letterChoice[0] == 'B':
            print("Choose your defense!")
            print("6(block) 7(dodge) 8(counter)")
            selectedAction = int((input("enter here:")))
            letterChoice.clear()
            choiceList.append(selectedAction)

        elif letterChoice[0] == 'C':
            print("Choose your special action!")
            print("9(summon)")
            selectedAction = int((input("enter here:")))
            letterChoice.clear()
            choiceList.append(selectedAction)

    # compares the choices of the players to find a suitable output
    @staticmethod
    def rps():
        global choiceList
        global actionTuple
        global selectedAction
        global z
        z = 0

        if actionTuple[choiceList[0]] == 'water' and actionTuple[choiceList[1]] == 'fire':
            z += 1
        elif actionTuple[choiceList[0]] == 'fire' and actionTuple[choiceList[1]] == 'water':
            z -= 1
        elif actionTuple[choiceList[0]] == 'fire' and actionTuple[choiceList[1]] == 'wind':
            z += 1
        elif actionTuple[choiceList[0]] == 'wind' and actionTuple[choiceList[1]] == 'fire':
            z -= 1
        elif actionTuple[choiceList[0]] == 'wind' and actionTuple[choiceList[1]] == 'lightning':
            z += 1
        elif actionTuple[choiceList[0]] == 'lightning' and actionTuple[choiceList[1]] == 'wind':
            z -= 1
        elif actionTuple[choiceList[0]] == 'lightning' and actionTuple[choiceList[1]] == 'earth':
            z += 1
        elif actionTuple[choiceList[0]] == 'earth' and actionTuple[choiceList[1]] == 'lightning':
            z -= 1
        elif actionTuple[choiceList[0]] == 'earth' and actionTuple[choiceList[1]] == 'water':
            z += 1
        elif actionTuple[choiceList[0]] == 'water' and actionTuple[choiceList[1]] == 'earth':
            z -= 1
        elif actionTuple[choiceList[0]] == actionTuple[1:5] and actionTuple[choiceList[1]] == 'block':
            z += 1
        elif actionTuple[choiceList[0]] == 'block' and actionTuple[choiceList[1]] == actionTuple[1:5]:
            z -= 1
        return


    # wincon checks the win condition 'z' to see who won the match
    @staticmethod
    def wincon():
        global player1
        global player2
        global actionTuple

        if z == 1:
            print(''
                  '')
            print(f"{player1.name} has won the round!")
            print(f"{player1.name} chose {actionTuple[choiceList[0]]} and {player2.name} chose {actionTuple[choiceList[1]]}")

            if player1.element == actionTuple[choiceList[0]]:
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
            print(''
                  '')
            print(f"{player2.name} has won the round!")
            print(f"{player1.name} chose {actionTuple[choiceList[0]]} and {player2.name} chose {actionTuple[choiceList[1]]}")

            if player2.element == actionTuple[choiceList[1]]:
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
            print(''
                  '')
            print('The round is undecided!')
            print(f"{player1.name} chose {actionTuple[choiceList[0]]} and {player2.name} chose {actionTuple[choiceList[1]]}")

            player1.health -= 10
            player2.health -= 10

            print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at "
                  f"{player2.health} health!")
            print('')


    # game loop and turn system
    @staticmethod
    def round():
        ranLet = ['A']
        players = Shinobi
        players.setplayers(players)
        global player1
        global player2
        global letterChoice
        global actionTuple

        while player1.health or player2.health > 0:
            print(f"{player1.name}\'s turn")
            print("pick your action")
            print("(A for attack options) or (B for defensive options) or (C for special options)")
            answer = str(input())
            letterChoice.append(answer)
            Bout.pickleaction()
            print('')
            print(f"{player2.name}\'s turn")
            if random.choice(ranLet) == 'A':
                letterChoice.append(ranLet)
                Bout.pickleaction()
                Bout.rps()
                Bout.wincon()
                choiceList.clear()
                if player1.health < 2:
                    print(f"Game over! {player2.name} wins!")
                    break
                elif player2.health < 2:
                    print(f"Game over! {player1.name} wins!")
                    break
                else:
                    continue

                    # player 1 chooses block
            # player 1 chooses action


battle = Bout()
battle.round()
