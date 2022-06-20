jutsuList = []

class Jutsu:
    def __init__(self, name=str, dictkey=str, bloodline=str, damage=int, atrange=int, chakracost=float):
        self.name = name
        self.dictkey = dictkey
        self.bloodline = bloodline
        self.damage = damage
        self.atrange = atrange
        self.chakracost = damage*.9

class Transformation:
    def __init__(self, whatami=str):
        self.whatami = whatami

class Weapon:
    def __init__(self, name=str, dictkey="attack", weaponkey=str, isranged=False, amount=int, damage=int, atrange=int):
        self.name = name
        self.dictkey = dictkey
        self.weaponkey = weaponkey
        self.isranged = isranged
        self.amount = amount
        self.damage = damage
        self.atrange = atrange

class Summon:
    def __init__(self, race=str, name=str, element=str, health=int, chakra=int, playerX=int, playerY=int, targetX=int,
                 targetY=int, tired=False, jutsu=list, bline=str, inventory=list, context=str, weapon=Weapon, choice=Jutsu):
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
        self.inventory = inventory
        self.context = context
        self.weapon = weapon
        self.choice = choice

# jutsu list used for the main file
fireball1 = Jutsu("fireball", "fire", "land of fire", 20, 3)
jutsuList.append(fireball1)
waterprison1 = Jutsu("waterprison", "water", "land of water", 10, 1)
jutsuList.append(waterprison1)
