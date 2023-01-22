dic1 = {}

print(1, dic1)

# dic1[input('key1: ')] = input('val 1: ')
# dic1[input('key2: ')] = input('val 2: ')
# dic1[input('key3: ')] = input('val 3: ')
# print(2, dic1)

key1 = input('Key 1:')
val1 = input('Value 1: ')
dic1[key1] = val1


val2 = int(input('Price : '))
dic1['price'] = val2


print(2, dic1)

dic1['Locat'] = 'Matara'
print(3, dic1)
print(len(dic1))

del dic1['price']
print(3, dic1)
print(len(dic1))