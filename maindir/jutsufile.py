jutsuList = []

class Jutsu:
    def __init__(self, name=str, dictkey=str, bloodline=str, damage=int, atrange=int, chakracost=float):
        self.name = name
        self.dictkey = dictkey
        self.bloodline = bloodline
        self.damage = damage
        self.atrange = atrange
        self.chakracost = damage*.9

class Summon:
    def __init__(self, race=str, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, jutsu=list, bline=str, choice=Jutsu):
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
        self.choice = choice

# jutsu list used for the main file
fireball1 = Jutsu("fireball", "fire", "land of fire", 20, 3)
jutsuList.append(fireball1)
waterprison1 = Jutsu("waterprison", "water", "land of water", 10, 1)
jutsuList.append(waterprison1)
# create a method that creates jutsu for the ninja to use instead and the chakra cost is based on the damage that will obviously have a limit
# and for summons they will have jutsu as well but less and they will be fun/funky

