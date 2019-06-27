class Me:

    def __init__(self):
        self.name = "Sooa"
        self.likes = ["Cats", "Nature", "Python"]
        self.gender = "Female"
        self.country = "South Korea"


me = Me()

print("My name is...")
print(me.name)
print("I like...")

for x in me.likes:
    print(x)

print("I am...")
print(me.gender)

print("I am from...")
print(me.country)