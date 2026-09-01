



class Rektangel:
    def __init__(self, height, lenght):
        self.height = height
        self.lenght = lenght

    def räkna_area(self):
        return self.height * self.lenght

    def räkna_omkrets(self):
        return self.height*2 + self.lenght*2

    def set_height(self, height):
        self.height = height


rektangel1 = Rektangel(3, 4)
rektangel1.set_height(7)

rektangel2 = Rektangel(4, 2)
rektangel3 = Rektangel(49, 26)
rektangel4 = Rektangel(36, 44)

print("Area: ", rektangel1.räkna_area(), "    Omkrets: ", rektangel1.räkna_omkrets())
print("Area: ",rektangel2.räkna_area(), " Omkrets: ", rektangel2.räkna_omkrets())
print("Area: ",rektangel3.räkna_area(),"  Omkrets: ", rektangel3.räkna_omkrets())
print("Area: ",rektangel4.räkna_area(),"  Omkrets: ", rektangel4.räkna_omkrets())