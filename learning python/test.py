
# 8:12 96%

# x = 1,
# print(type(x))

# a = {}
# print(type(a))

# what we are going to learn
# list
# tuple
# dict
# set

# a = [1, 3, "ram", ["test", "first"]]

# print(a[3][1])
# print(a[-4])
# print(a[-1][-1])


# # displays all the methods and the properties of parent element
# print(dir(a))

# # tuple
# a = (1, 3, "ram", ["test", "first"])
# print(type(a))
# print(a[3][1])
# print(a[-4])
# print(a[-1][-1])

# # describes it/
# print(help(a.count))

# x = {1, 3, 2, 1}
# print(x)

# # //returns true because no ordering of elemets
# print({1, 2, 3} == {2, 1, 3})

y = {"name": "ram", "college": "khec", "sem": 6}

# print(y, type(y))

for i, j in y.items():
    print(f"{i} = {j}")

for i in y:
    print(f"{i} = {y[i]}")

print(dir(y))


# MUTABLE AND IMMUTABLE

# mutable
# list set dict are mutable other are immutable

a = 1.01
print(id(a))
a = 2
print(id(a))

# interview question
a = "ram"
b = a
print(a is b)  # returns true cause both point on same location
print(id(a) == id(b))
a = "shyam"
print(a is b)  # a creates next location


# mutable
a = [1, 2, 3]
print(id(a))
a.append(4)
print(id(a))

a = "ram"
print(a, id(a))
a += " shyam"
print(a, id(a))


# here both returns same address location
def something(x):
    print(id(x))


y = "ram"
print(id(y))
something(y)


# here both returns different address location
def something1(x):
    x = "shyam"
    print(id(x))


y = "ram"
print(id(y))
something1(y)


a = [1, 2, 3]
b = a
b.append(4)
print(a)


def something4(x):
    x.append(4)


y = [1, 2, 3]
something4(y)
print(y)


a = [1, 2, 3]
b = a
print(id(a), id(b))
print(b.append(4))
print(b)


a = 1
b = 1
print(a is b)

a = "1234"
b = "1234"
print(a is b)


# LIST COMPREHENSION

# Syntax
# 1 . [item for item in iterable]
# 2 . [expression for item in iterable]
# 3 . [expression for item in iterable if condition]


# mylist = []

# for i in range(101, 201, 2):
#     print(i)

mylist = [i*2 for i in range(101, 201, 2)]
print(mylist)

mylist = [i for i in range(101, 201) if i % 5 == 0]
print(mylist)


# # DICT COMPREHENSIONS
# Syntax
# 1. {keyexpression : valueexpression for key , value in iterable}
# 2 . {keyexpression: valueexpression for key, value in iterable if condition}
# 3 . {keyexpression: valueexpression for key in iterable if condition}

eg_dict = {
    'name': 'ram',
    "class": 20,
    'college': 'khec'
}


result = {}

for key, value in eg_dict.items():
    result[value] = key

print(result)


result = {
    value: key for key, value in eg_dict.items()
}
print(result)


result = {}
for key, value in eg_dict.items():
    if key != 'class':
        result[key] = value

print(result)

result = {key: value for key, value in eg_dict.items() if key != 'class'}
print(result)


xyz = [10, 20, 30]
result = [i*2 for i in xyz if i*2 < 50]
print(result)


def test(y):
    y["sem"] = 6


x = {"name": "ram"}
test(x)
print(x)

b = x  # (memory address is copied)
