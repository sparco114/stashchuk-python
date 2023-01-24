# import datetime
#
#
# def time_now():
#     now = datetime.datetime.now().strftime('%H:%M:%S')
#     print(now)
#     return now
#
#
# def today(city, time=time_now()):
#     info = f"It is {time} now in {city}"
#     return info
#
#
# print(today(city='Matara'))
# --------------------------------------------------------------------------------------------------------------
# def func1(number):
#     """function ONE"""
#     if (number % 2) == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
#
#
# def func2(num, reply):
#     reply(num)
#     # return info
#
#
# def func1_1(number):
#     inf = f"Square your number is {number * number}"
#     print(inf)
#     return inf
#
#
# ask = int(input('Enter number: '))
#
#
# func2(ask, func1)
# func2(ask, func1_1)
# func1_1(ask)
# --------------------------------------------------------------------------------------------------------------


# a = 10
#
#
# def my_fn():
#     a = True
#     global b
#     b = 10
#     print('a fn = ', a)
#     print('b fn = ', b)
#     return b
#
#
# my_fn()
#
# print('a global = ', a)
# print('b global = ', b)

a = {1, 7, 25, 2.5, 14}
b = {1, 7, 25, 2.5, 14}
print('--1--')
print(type(a))
print(id(a))
print(id(b))

print('--2--')
print(a == b)
print(a.__eq__(b))

print('--3--')
print(a is b)

print('--4--')
print(7 in a)
print(22 in b)
