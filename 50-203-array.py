from array import array

int_lis = array('i', [11, 25, 47, 10, 25])

print(int_lis)
print(type(int_lis))

int_lis.append(777)
print(int_lis)

int_lis.pop()
print(int_lis)

print(int_lis.count(25))
print(len(int_lis))

for i in int_lis:
    print(i)

print(int_lis[0])


with open("new.bin", 'wb') as my_file:
    int_lis.tofile(my_file)

import_arr = array('i')

with open('new.bin', 'rb') as my_file:
    import_arr.fromfile(my_file, 3)
    print(import_arr)


import_arr.reverse()
print(import_arr)
