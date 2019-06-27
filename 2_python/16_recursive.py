def factorial(x):
    if x<0:
        return 0
    if x==0:
        return 1

    return x*factorial(x-1)


print("What is factorial 4?")
print(factorial(4))


# This is same as...

x = 4
fact = 1
for i in range(1, x+1):    # i starts from 1 instead of 0
    fact *= i

print("What is factorial 4?")
print(fact)