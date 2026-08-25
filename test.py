class Person:
    def __init__(self):
         self.förnamn = ""
         self.efternamn = ""
         self.födelseår = ""
         self.singel = True

person1 = Person()
person1.förnamn = "TUvA"
person1.efternamn = "TEnghall"
person1.födelseår = "2008"
person1.singel = True

print(person1.förnamn)