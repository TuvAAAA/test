import copy


class Bil:
    def __init__(self):
        self.regnummer = ""
        self.fabrikat = ""
        self.årsmodell = ""
        self.tjänstevikt = ""
        self.motoreffekt = ""
        self.person = ""
        self.bilförare = None


class Person:
    def namn(self):
            self.namn = ""


p1 = Bil()
p1.person = Person()
p1.person.namn = "Robert"
p2 =Bil()
p2.person = Person()
p2.person.namn = "jojo siwa"
            


Bil1 = Bil()
Bil1.regnummer = "456"
Bil1.fabrikat = "Dodge"
Bil1.motoreffekt ="372hk"
Bil1.tjänstevikt = "1833kg"
Bil1.årsmodell = "2010"

Bil2 = Bil()
Bil2.regnummer = "2354"
Bil2.fabrikat = "Smart"
Bil2.motoreffekt ="89hk"
Bil2.tjänstevikt = "880kg"
Bil2.årsmodell = "2016"

Bil3 = copy.copy(Bil2)
Bil3.regnummer = "5632577"


print("2010 Dodge Challenger R/T Coupe 2D RWD:  ", Bil1.årsmodell, Bil1.tjänstevikt, Bil1.motoreffekt, Bil1.fabrikat, Bil1.regnummer)


print("2016 smart fortwo passion RWD: ", Bil2.årsmodell, Bil2.tjänstevikt, Bil2.motoreffekt, Bil2.fabrikat, Bil2.regnummer)

print(p1.person.namn)

print(p2.person.namn)
