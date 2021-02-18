# fucntional programming

# def test(x, y, z):
#     pass


# print(test)

# adder = test
# print(adder(1, 2,3)


# can pass the function as an argument
# def adder(x, y, z):
#     return x+y+z


# def something(adder_function):
#     print(adder_function(1, 2, 3))


# something(adder)


# can return the function
# def adder(x, y, z):
#     return x+y+z


# def something():
#     return adder


# new_adder = something()
# print(new_adder(1, 2, 3))


# def test(x, y):
#     print("upper")


# def test():
#     print("lower")


# test(1, 2)


# returns none
# def test1():
#     print("hello world")


# def test2():
#     return test1()

# print(test2())


# def test1():
#     return ("hello world")


# def test2():
#     test1()


# print(test2())

# def adder(x, y, z):
#     return x+y+z


# print(adder(y=1, x=2, z=3))
# # correct 1 and 2 are positional argument but z is the keyword argument
# print(adder(1, 2, z=3))
# # adder(1, x=2, 3) incorrect


# *args = 0 to any number of positional arguments
# **kwargs = 0 to any number of keyword arguments


# def adder(*args):
#     print(args, type(args))
#     print(sum(args))


# adder()
# adder(1, 2, 3, 4)


# def adder(start, *args):
#     result = start * 10
#     print(args, type(args))
#     print(sum(args))
#     print(start)


# # adder()
# adder(1, 2, 3, 4)
# adder(5, 2)
# adder(5, 2, 3)


# 2x+5y+3z

# def adder(**kwargs):
#     print(kwargs, type(kwargs))
#     print(2 * kwargs['x'] + 5 * kwargs['y'] + 3 * kwargs['z'])

# adder(x=1, y=2, z=3)

# def outer():
#     print("I am at outer")

#     def inner():
#         print("I am at inner")

# print(outer())
