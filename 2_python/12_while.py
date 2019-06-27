i = 0

print("Let's count from 0 to 9!")

while(i<10):
    print(i)    # The indentation (tab or 4 spaces) is very, very, very important!
    i+=1

print("What's the sum from 0 to 9?")

i = 0
s = 0

while(i<10):
    s+=i
    i+=1

print(s)

print("Let's make some rectangle with 2 while's")

i = 0
j = 0
while(i < 10):
    j = 0

    while(j < 10):
        print('*', end='')  # This prevents newline
        j+=1

    print('')

    i +=1


print("Triangle!")

i=0
while(i < 10):
    j = 0

    while(j <= i):
        print('*', end='')  # This prevents newline
        j+=1

    print('')

    i +=1


