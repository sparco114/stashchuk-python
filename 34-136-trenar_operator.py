# my_img = ('1920', '1080')
#
# info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 and type(my_img[0]) is str and type(
#     my_img[1]) is str else "Incorrect formating"
#
# print(type(my_img[0]))
# print(info)
# --------------------------------------------------------------------------------------------------

my_img = ('1920', '1080')

if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str:
    info = f"{my_img[0]}x{my_img[1]}"
else:
    info ="Incorrect formating"

print(type(my_img[0]))
print(info)
# --------------------------------------------------------------------------------------------------

a = 'Adfghl'

print("String is long" if len(a) > 5 else "string is short")


