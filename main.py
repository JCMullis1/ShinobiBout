import random

class shinobi:
    def __init__(self, name, play, element, health):
        self.name = name
        self.play = play
        self.element = element
        self.health = health

class bout:
    def __init__(self):
        return

    def rps(self):

        global typeList
        global randomElement
        global selectedElement
        global z

        z = 0
        typeList = ['water', 'earth', 'fire', 'wind', 'lightning']
        randomElement = random.choice(typeList)
        print('choose your type: 0(water) 1(earth) 2(fire) 3(wind) 4(lightning)')
        selectedElement = int(input("enter here:"))

        if typeList[selectedElement] == 'water' and randomElement == 'fire':
            z += 1
        elif typeList[selectedElement] == 'fire' and randomElement == 'water':
            z -= 1
        elif typeList[selectedElement] == 'fire' and randomElement == 'wind':
            z += 1
        elif typeList[selectedElement] == 'wind' and randomElement == 'fire':
            z -= 1
        elif typeList[selectedElement] == 'wind' and randomElement == 'lightning':
            z += 1
        elif typeList[selectedElement] == 'lightning' and randomElement == 'wind':
            z -= 1
        elif typeList[selectedElement] == 'lightning' and randomElement == 'earth':
            z += 1
        elif typeList[selectedElement] == 'earth' and randomElement == 'lightning':
            z -= 1
        elif typeList[selectedElement] == 'earth' and randomElement == 'water':
            z += 1
        elif typeList[selectedElement] == 'water' and randomElement == 'earth':
            z -= 1
        return

    def round(self):
        typeList = ['water', 'earth', 'fire', 'wind', 'lightning']

        name1 = str(input('enter name:'))
        play1 = 1
        element1 = str(input('element:'))
        print(element1)
        health1 = int(input('health:'))

        name2 = str(input('enter name:'))
        play2 = 2
        element2 = str(input('element:'))
        print(element2)
        health2 = int(input('health:'))

        player1 = shinobi(name1, play1, element1, health1)
        player2 = shinobi(name2, play2, element2, health2)

        while player2.health or player1.health > 0:
            bout.rps(self)

            if z == 1:
                print(''
                      '')
                print(f"{player1.name} has won the round!")
                print(f"{player1.name} chose {typeList[selectedElement]} and {player2.name} chose {randomElement}")

                if player1.element == selectedElement:
                    player2.health -= 20
                    print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at {player2.health} health!")

                    if player1.health < 2:
                        print('game over!')
                        break
                    else:
                        continue
                else:
                    player2.health -= 10
                    print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at {player2.health} health!")

                    if player1.health < 2:
                        print('game over!')
                        break
                    else:
                        continue

            elif z == -1:
                print(''
                      '')
                print(f"{player2.name} has won the round!")
                print(f"{player1.name} chose {typeList[selectedElement]} and {player2.name} chose {randomElement}")

                if player2.element == randomElement:
                    player1.health -= 20
                    print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at {player2.health} health!")

                    if player1.health < 2:
                        print('game over!')
                        break
                    else:
                        continue
                else:
                    player1.health -= 10
                    print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at {player2.health} health!")
                    if player1.health < 2:
                        print('game over!')
                        break
                    else:
                        continue

            else:
                print(''
                      '')
                print('The round is undecided!')
                print(f"{player1.name} chose {typeList[selectedElement]} and {player2.name} chose {randomElement}")

                player1.health -= 10
                player2.health -= 10

                print(f"{player1.name} is now at {player1.health} health! And {player2.name} is now at {player2.health} health!")

                if player1.health < 2:
                    print('game over!')
                    break
                elif player2.health < 2:
                    print('game over!')
                    break
                else:
                    continue


battle = bout()
battle.round()
