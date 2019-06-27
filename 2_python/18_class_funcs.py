class Me:

    def __init__(self):
        self.name = "Sooa"
        self.likes = ["Cats", "Nature", "Python"]
        self.gender = "Female"
        self.country = "South Korea"


    def say_name(self):
        print("My name is %s" % self.name)

    def say_likes(self):
        print("I like %s" % ', '.join(self.likes))

    def do_plus(self,a,b):  # Your class function can have parameters. Just don't forget 'self'!
        print("%d plus %d is %d" % (a,b,a+b))


me = Me()

me.say_name()
me.say_likes()
me.do_plus(3,4)