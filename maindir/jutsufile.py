
class Jutsu:
    def __init__(self, dictkey=str, damage=int, atrange=int):
        self.dictkey = dictkey
        self.damage = damage
        self.atrange = atrange
# jutsu list used for the main file
fireball = Jutsu("fire", 20, 3)
waterprison = Jutsu("water", 10, 1)


