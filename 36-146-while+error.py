# import random
#
# random_num = random.randint(1, 5)
#
# while True:
#     try:
#         user_num = int(input('Input number: '))
#     except Exception as e:
#         print("Insert NUMBER!!!", e)
#         break
#     if user_num != random_num:
#         print('Try again')
#         continue
#     print('Congratulates')
#     break
#
# ----------------------------------------------------------------------------------------------------------------


while True:
    try:
        num1 = float(input("Num 1: "))
        num2 = float(input("Num 2: "))
        if num2 == 0:
            raise ZeroDivisionError("NO devided by ZERO")
        res = num1 / num2
        print(res)
        ask = input("Du you want to continue? ")
        if ask == 'Yes' or 'yes' or 'y':
            continue
        else:
            break
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("Insert NUMBER!!!", e)

