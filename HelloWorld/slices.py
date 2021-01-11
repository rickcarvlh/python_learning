parrot = 'Norwegian Blue'

print(parrot[0:6])
print(parrot[-4:-2])
print(parrot[-4: 12])
print(parrot[-14: 6-14])

print(parrot[0:6:2]) #Nre
# we extend to 6 not counting 6 in steps of 2
print(parrot[0:6:3]) #Nw
# we extend to 6 not counting 6 in steps of 3

number = "9,223;372,036 854,775;807"
separators = number[1::4]
print(separators)

# doesn't make sence
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])