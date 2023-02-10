import random
import secrets
import string
import math

print('------random------')
print(random.randint(1, 10))

print(random.choice('abcd'))
print(random.choice([1, 55, 20, 88, None, False, 'ddd']))
print(random.choices('abcdef', k=2))
print(random.choices([1, 55, 20, 88, None, False, 'ddd'], k=3))

lis1 = [1, 55, 20, 88, None, False, 'ddd']
random.shuffle(lis1)
print(lis1)

print(''.join(random.choices('ABCDefghij1234567890', k=5)))

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print('random Password:', ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8)))

print('------secrets------')
all_chars = (string.ascii_letters + string.digits + string.punctuation)

print('secret Password:', ''.join(secrets.choice(all_chars) for i in range(8)))

print('------math------')

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(dir(math))

print('------recursiv_function------')


def calc_factorial(num):
    if type(num) is not int:
        raise TypeError('Number must be INTEGER')
    if num <= 0:
        raise ValueError('Number must be POSITIVE')
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num


print(calc_factorial(10))
print(math.factorial(10))
