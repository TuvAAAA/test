class Hund: 
    def __init__(self): #attribut
        self.ras = ""
    def existera(self): #MEtod
        print("jag existerar")

hund1 = Hund()
hund2 = Hund()


hund1.ras = "pudel"
hund2.ras = "golden"


hund1.existera()

print(hund1.ras)

() #används för anropning