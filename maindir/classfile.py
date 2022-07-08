jutsuList = []
amountList = [4, 6, 3]
choiceList = []
playerList = []
tempList = []
mapList = list(playerList)
elementList = ["water", "fire", "wind" "lightning", "earth", "summon"]
latestPlayer = int(len(playerList)-1)
def healthChakra():
    global playhealth, playchakra
    playhealth = int(input('How much health will each player have?: '))
    playchakra = int(input('How much chakra will each player have?: '))


contextdict = {
    "move": ["move", "dodge"],
    "defend": ["block", "guard break", "counter"],
    "strike": ["attack"],
    "chakra": ["water", "earth", "fire", "lightning", "wind", "summon", "transform", "clone", "shadow clone"],
    "nothing": ["nothing"]
}
#
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
    "move": ["nothing"],
    "summon": ["nothing"],
    "clone": ["nothing"],
    "shadow clone": ["nothing"],
    "transform": ["nothing"],
    "nothing": [""]
}

# class for jutsu techniques
class Jutsu:
    def __init__(self, name=str, dictkey=str, bloodline=str, damage=int, atrange=int, chakracost=float):
        self.name = name
        self.dictkey = dictkey
        self.bloodline = bloodline
        self.damage = damage
        self.atrange = atrange
        self.chakracost = damage*1.2

# class for trees boxes and other such objects
class Entity:
    def __init__(self, name=int, form=int, entityX=int, entityY=int, istransformed=False, chakra=int, ID=int):
        self.name = name
        self.form = form
        self.entityX = entityX
        self.entityY = entityY
        self.istransformed = istransformed
        self.chakra = chakra
        self.ID = ID

# class for weapons from kunai to samehada
class Weapon:
    def __init__(self, name=str, dictkey="attack", buff=str, buffamount=int, istransform=False, chakra=int,
                 weaponkey=str, isranged=False, amount=int, damage=int, atrange=int, position=int, weaponX=int, weaponY=int, ID=int):
        self.name = name
        self.dictkey = dictkey
        self.buff = buff
        self.buffamount = buffamount
        self.istransform = istransform
        self.chakra = chakra
        self.weaponkey = weaponkey
        self.isranged = isranged
        self.amount = amount
        self.damage = damage
        self.atrange = atrange
        self.position = position
        self.weaponX = weaponX
        self.weaponY = weaponY
        self.ID = ID

class Summon:
    def __init__(self, race=str, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, jutsu=list, bline=str, context=str, istransform=False, weapon=Weapon, choice=Jutsu, ID=int):
        self.race = race
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
        self.context = context
        self.istransform = istransform
        self.weapon = weapon
        self.choice = choice
        self.ID = ID

attack1 = Jutsu("attack", "attack", str, 10, 2)
move1 = Jutsu("move", "move", str, 0, 10000)
guardbreak1 = Jutsu("guard break", "guard break", str, 10, 2)
counter1 = Jutsu("counter", "counter", str, 10, 2)
dodge1 = Jutsu("dodge", "dodge", str, 10, 2)
block1 = Jutsu("block", "block", str, 10, 2)
summon1 = Jutsu("summon", "summon", str, 0, 3, 40)
transform1 = Jutsu("transform", "transform", str, 0, 2, 20)
clone1 = Jutsu("clone", "clone", str, 0, 3, 20)
shadowclone1 = Jutsu("shadow clone", "shadow clone", str, 0, 3)


#struggling right now
fists1 = Weapon(name="fists", weaponkey="fists", damage=10, atrange=2)
kunai1 = Weapon(name="kunai", weaponkey="kunai", isranged=True, damage=16, atrange=2, position=0)
shuriken1 = Weapon(name="shuriken", weaponkey="shuriken", isranged=True, damage=12, atrange=5, position=1)
paperbomb1 = Weapon(name="paper bomb", weaponkey="paper Bomb", isranged=False, position=2)

# jutsu list used for the main file
fireball1 = Jutsu("fireball", "fire", "land of fire", 20, 3)
jutsuList.append(fireball1)
waterprison1 = Jutsu("waterprison", "water", "land of water", 10, 1)
jutsuList.append(waterprison1)

jlist = [move1, block1, guardbreak1, counter1, dodge1, summon1, kunai1, shuriken1, paperbomb1, transform1, clone1, shadowclone1]

class Shinobi:
    def __init__(self, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, specaction=False, jutsu=list, bline=str, context=str, istransform=False, itamount=list, weapon=Weapon, choice=Jutsu, ID=int):
        self.name = name
        self.element = element
        self.health = health
        self.chakra = chakra
        self.playerX = playerX
        self.playerY = playerY
        self.targetX = targetX
        self.targetY = targetY
        self.tired = tired
        self.specaction = specaction
        self.jutsu = jutsu
        self.bline = bline
        self.context = context
        self.istransform = istransform
        self.itamount = itamount
        self.weapon = weapon
        self.choice = choice
        self.ID = ID

    # this just defines the players used in the demo of the game
    @staticmethod
    def setplayers():
        global playuhs, players, playchakra, playhealth
        playuhs = int(input('How many players will be fighting today?: '))
        print('')
        playID = 0
        for number in range(playuhs):
            player = f"player{playID}"
            globals()[player] = Shinobi(name=str(input('Enter name: ')),
                                        element=str(input('Enter element: ')),
                                        health=int(playhealth),
                                        chakra=int(playchakra),
                                        jutsu=list(jlist),
                                        itamount=list(amountList),
                                        bline=str(input('Enter bloodline: ')),
                                        ID=int(len(playerList)+1))
            playerList.append(globals()[player])
            for juts in range(len(jutsuList)):
                if playerList[playID].bline == jutsuList[juts].bloodline:
                    playerList[playID].jutsu.append(jutsuList[juts])
            customjutsu = int(input("How many custom jutsu would you like to make?: "))
            for cus in range(customjutsu):
                jutsuID = 0
                jutsu = f"jutsu{jutsuID}"
                globals()[jutsu] = Jutsu(name=str(input("Enter jutsu name: ")),
                                         dictkey=str(input("Enter jutsu type (element or type of action): ")),
                                         bloodline=playerList[playID].bline,
                                         damage=int(input("Enter damage of jutsu: ")),
                                         atrange=int(input("Enter range of jutsu: ")))
                globals()[player].jutsu.append(globals()[jutsu])
                print('')
                jutsuID += 1
            playID += 1
            print('')

def summoning():
    summon = f"summon{latestPlayer + 1}"
    globals()[summon] = Summon(race=str(input('Enter summon race: ')),
                               name=str(input('Enter summon name: ')),
                               element=str(input('Enter summon element: ')),
                               health=playhealth,
                               chakra=playchakra,
                               jutsu=list(jlist),
                               bline=str(input('Enter bloodline: ')),
                               ID=int(len(playerList)+1))
    playerList.append(globals()[summon])

def classFactory(a):
    for i in range(a.total):
        pass
    # not made yet I am not sure how I'd do this anyhow


# attack1 = Jutsu("attack", "attack", str, 10, 2)
# move1 = Jutsu("move", "move", str, 0, 10000)
# guardbreak1 = Jutsu("guard break", "guard break", str, 10, 2)
# counter1 = Jutsu("counter", "counter", str, 10, 2)
# dodge1 = Jutsu("dodge", "dodge", str, 10, 2)
# block1 = Jutsu("block", "block", str, 10, 2)
# summon1 = Jutsu("summon", "summon", str, 0, 3, 40)
#
# #struggling right now
# fists1 = Weapon(name="fists", weaponkey="fists", amount=1, damage=10, atrange=2)
# kunai1 = Weapon(name="kunai", weaponkey="kunai", isranged=True, amount=4, damage=16, atrange=2)
# shuriken1 = Weapon(name="shuriken", weaponkey="shuriken", isranged=True, amount=6, damage=12, atrange=5)
# paperbomb1 = Weapon(name="paper bomb", weaponkey="paper Bomb", isranged=False)
#
# # jutsu list used for the main file
# fireball1 = Jutsu("fireball", "fire", "land of fire", 20, 3)
# jutsuList.append(fireball1)
# waterprison1 = Jutsu("waterprison", "water", "land of water", 10, 1)
# jutsuList.append(waterprison1)
#
# jlist = [move1, block1, guardbreak1, counter1, dodge1, summon1, kunai1, shuriken1, paperbomb1]
