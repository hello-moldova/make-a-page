i = 0

print("Let's count from 0 to 9!")

for i in range(10):		# range(10) means 0, 1, ..., 9. In other words, numbers starting from 0, and less than 10.
    print(i)	# The indentation (tab or 4 spaces) is very, very, very important!

print("What's the sum from 0 to 9?")

s = 0

for i in range(10):
	s+=i

print(s)


print("Let's make some rectangle with 2 while's")


for i in range(10):
    for j in range(10):
        print('*', end='')
    print('')


print("Triangle!")

for i in range(10):
    for j in range(i):
        print('*', end='')
    print('')
