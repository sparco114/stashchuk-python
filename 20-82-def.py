def merge_lists_to_dict(a, b):
    zip_lis = zip(a, b)
    res = list(zip_lis)
    return res

lis1 = [1, 2, 3]
lis2 = [True, True, False]
final1 = merge_lists_to_dict(lis1, lis2)
print(final1)

di1 = {1: True, 2: True, 3: False}
di2 = {3: 'aaa', 4: 'bbb', 5: 'ccc'}
final2 = merge_lists_to_dict(di1, di2)
print(final2)
