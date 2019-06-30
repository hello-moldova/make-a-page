import re

class Me:

    def __init__(self):
        self.name = "Sooa"
        self.likes = ["Cats", "Nature", "Python"]
        self.gender = "Female"
        self.country = "South Korea"


    def say_name(self):
        return "My name is %s" % self.name

    def say_likes(self):
        return "I like %s" % ', '.join(self.likes)

    def do_plus(self,a,b):  # Your class function can have parameters. Just don't forget 'self'!
        if type(a) == type('wow'):
            a = int(a)
        if type(b) == type('wow'):
            b = int(b)

        return "%d plus %d is %d" % (a,b,a+b)


    def listen(self, command, params):
        if command == "name":
            return self.say_name()
        if command == "likes":
            return self.say_likes()
        if command == "plus":
            return self.do_plus(*params)

        return "I'm sorry, I couldn't understand."


me = Me()

commands = input()
commands = re.split(' ', commands)

result = me.listen(commands[0], commands[1:])
print(result)