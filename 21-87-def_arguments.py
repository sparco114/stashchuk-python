# def kor(*person):
#     """print(inf)"""
#     print(person)
#     info = f"i {person[0]} and {person[1]}"
#     return info
#
#
#
#
# inf = kor('Anton', 33)
# print(inf)
# -----------------------------------------------------------------------------------
print('Exercise 1')
def merge_lists_to_dict(numbers, availible):
    zip_lis = zip(numbers, availible)
    res = dict(zip_lis)
    return res


lis1 = [1, 2, 3]
lis2 = [True, True, False]
final1 = merge_lists_to_dict(numbers=lis1, availible=lis2)
print(final1)

del lis2[0]
lis2.append(None)
final1 = merge_lists_to_dict(lis1, availible=lis2)
print(final1)


# -----------------------------------------------------------------------------------
print('Exercise 2')


def update_car_info(**car):
    print(car)
    car['is_availible'] = True
    return car


res1 = update_car_info()
print(res1)

res2 = update_car_info(brand='DELL', price=115_000)
print(res2)
