# my_obj = {
#     'x': 20,
#     'y': True,
#     'z': 70.5,
# }
# ---------------------------------------
# # print(my_obj.get('m'))
# for eee in my_obj.items():
#     # print(eee[1])
#     a, b = eee
#     print(b)
#
# print('---------------------')
#
# for k, v in my_obj.items():
#     print(v)
# --------------------------------------------------------------------------
print('------Exercise 1------')

dic1 = {
    'x': 20,
    'y': True,
    'z': 70.5,
}

print(dic1)


def dic_to_list(diction):
    for k, v in diction.items():
        # if type(v) is int:
        if isinstance(v, int):
            diction[k] = v * 2
        # else:
        #     pass

    lis1 = list(diction.items())
    return lis1


print(dic_to_list(dic1))
# -------------------------------------------------------------------------------------------------
print('------Exercise 2------')

lis2 = [1, 2.5, True, 'Man', None, True, 5.7859, 22, 'Women']
print(lis2)


def filter_list(lis, datatype):
    new = []
    for ee in lis:
        # if type(ee) is datatype:
        if isinstance(ee, datatype):
            new.append(ee)
    return new


print(filter_list(lis2, float))
