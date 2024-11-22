class student:
    name = "Aarush"
    grade = 7
    age = 12

    def introduction(self):
        print("Hello, I am",self.name)
    def details(self):
        print("I am in grade",self.grade)
        print("I am",self.age,"years old.")

ob = student()
ob.introduction()
ob.details()
print()
print()
print()


class parrot:
    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing(self, song):
        print("{} sings {}.".format(self.name, song))
    
    def dance(self):
        print("{} is now dancing.".format(self.name))

blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

print("{} is a {}.".format(blu.name, blu.species))
print("{} is also a {}.".format(woo.name, woo.species))
print()
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

blu.sing("Happy")
woo.sing("Happy")
blu.dance()
woo.dance()
