set1 = {2, 5, 10, 45, 0}

print(1, set1)

set1.add(77)
print(2, set1)

set2 = {5, 77, 8, 66, 99}
print(3, set2)

set_unit1 = set1 | set2
print(4, set_unit1)
set_unit2 = set1.union(set2)
print(4, set_unit2)
print('4+', set_unit1 == set_unit2)

list_union = list(set_unit1)
print(5, list_union)

set3 = {'99999', 666666}
list_union.append('888')
list_union.extend(set3)

print('5+', list_union)
