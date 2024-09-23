
# variables
x = 5 # interpreter will figure out this is an int
y = 'a' # str
z = 6.0 # float (because of the .0)
b = True # bool

# this is a java loop
# for (int a=0; a<5; a++) {
#     repeat this stuff
# }

# this is the same python loop
for a in range(0, 5):
    pass
    # repeat this stuff
 # note this is really a "for-each" loop through every int
 # in the range 0-5 (exclusive on the upper)

# this is a list
l = list()
l.append(10)
l.append(20)
print(l)
for item in l:
    print(item)

# there's still a while looop
while (False):
    pass
    # this line wont be reached


# create a function with "def"
def add_two_numbers(num1: float, num2: float) -> float:
    return num1 + num2

print(add_two_numbers(4, 6.0))
print(add_two_numbers('a', 'b'))

# lambda functions
my_func = lambda x: x+1
print(my_func(5))
my_func2 = lambda x, y: x + y
