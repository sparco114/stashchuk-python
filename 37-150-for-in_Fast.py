# lis1 = [-3, 8, 10, -2, -3]
#
# new_lis = [num * 2 for num in lis1]
# print(new_lis)
#
# positive_lis = [int(num / 2) for num in new_lis if num >= 0]
# print(positive_lis)

# ---------------------------------------------------------------------------------

# dic1 = {
#     'a': 111,
#     'b': 222,
#     'c': 333
# }
#
# new_dic = {k: v * 10 for k, v in dic1.items()}
# new = [k * 5 for k, v in dic1.items()]
# print(type(new))
# print(new)
# # for k, v in dic1.items():
# #     new_dic[k] = v * 10
# print(new_dic)


# --------------------------------------------------------------------------------------

# lis2 = [100, 200, 300]
#
# dic2 = {k: v for k, v in enumerate(lis2)}
# print(lis2)
# print(dic2)

# ---------------------------------------------------------------------------------

print("------Exercise 1 ------")
dic2 = {
    'aaa': 111,
    'bbb': 222,
    'ccc': 333
}

big_dic = {k.upper(): v for k, v in dic2.items()}
print(big_dic)


# --------------------------------------------------------------
print("------Exercise 2 ------")

lis2 = ['abc', 'Anton', 'DELL', 'http', 'z']

big_lis = [e for e in lis2 if len(e) > 3]
print(big_lis)


