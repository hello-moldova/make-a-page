a = [1,2,3,4,5,6,7]

print("What's in list 'a'?")
print(a)

print("What's the first number?")
print(a[0])		# Remember, python's index starts from 0!
print("What's the third number?")
print(a[2])		# First index is 0, second is 1, so third is 2.

print("What's the last?")
print(a[-1])	# Going backwards from 0!
print("What about second to last?")
print(a[-2])

print("Give me second to fifth!")
print(a[1:4])	# This is called 'slicing' the list. Important!

print("How long is 'a'?")
print(len(a))

print("So... what was the type of 'a'?")
print(type(a))