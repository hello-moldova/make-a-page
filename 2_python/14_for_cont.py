print("'for' in Python is about moving through a list.")
print()

a = [4,2,3,1,6]

print("I have a list:")
print(a)
print()

print("Printing the numbers individually:")
for x in a:
    print(x)

print()
print("You can do this with indexing, if you need indices")
for i in range(len(a)):
    print(a[i])


print()


print("I can iterate through a dictionary, too!")
print()

b = {"Seok-jin": "December 4",
    "Yoon-gi": "March 9",
    "Nam-joon": "September 12",
    "Ho-seok": "February 18",
    "Ji-min": "October 13",
    "Tae-hyung": "December 30",
    "Jung-kook": "September 1"}     # copy - pasted from 10_dict.py

print("Printing out the keys:")
for key in b.keys():
    print(key)

print()

print("Printing out the values:")
for value in b.values():
    print(value)

print()

print("Getting key, value at same time:")
for key, value in b.items():
    print(key+" "+value)