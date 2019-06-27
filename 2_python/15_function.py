def plus(a, b):     # 'def' is shorthand for 'define', or 'definition'
    print("What is %d + %d?" % (a,b))
    print(a+b)

plus(3,4)
plus(6,2)


def minus(a, b):
    print("What is %d - %d?" % (a,b))
    print(a-b)


def do_everything(a, b):
    print("I'm gonna do %d + %d and %d - %d!" % (a,b,a,b))
    plus(a,b)
    minus(a,b)


print()     # You know, this is also a function!
do_everything(9, 2)


def f(x):
    return 3*x + 4  # A classic linear function

x = 1
y = f(x)

print()
print("x is %d" % (x))
print("y is 3*x + 4 = %d" % (y))



print()
print("Here's a weird thing about functions")
print("functions can be inside a variable!!")

func = plus
print("Let's do func(3,4), after func = plus")
print()

func(3,4)

func = minus
print("Let's do func(3,4), after func = minus")
print()
func(3,4)