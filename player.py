class Player:
    def __init__(self, level, hp):
        self.level = level
        self.hp = hp

    def levelUP(self, amount):
        self.level +=amount


    #def damage(self, damage):
        #self.health -= damage

    def attack(self):
        print("player attacks!")
    def heal(self):
        print("player heals!")
    def walk(self):
        print("player walks")

player1 = Player(10)
player1.levelUP(5)

#player1 = Player(20)
#player1.health(3)
#print(player1.health)
print(player1.level)