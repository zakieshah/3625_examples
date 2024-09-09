import python_crash_course.numpy_basics as np

# dymamic array is called list
l1 = list()
l1.append(1)
l1.append(2)

l2 = ['a', 'b', 'c']
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

# tuples
t = (1, 2, 3)

# dictionaries
d = dict()
d['a'] = 5
print(d)

d2 = {'a': 1, 'b': 2, 'c': 3}
print(d2)
d2['d'] = 4
d2['d'] = 5
print(d2)
del d2['d']
print(d2)

# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = [n for n in numbers if n % 2 == 1]
print(odds)

# dict comprehension
d = {num: num+1 for num in numbers}
print(d)

