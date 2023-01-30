# class Comment:
#     def __init__(self):
#         pass
#
#     def addcom(self, num):
#         self.qty = 1000
#         self.txt = self.qty + num
#         self.ddd = 1
#
#     def reset_votes(self):
#         self.qty = 0
#         self.txt = 0
#         # self.ddd = 0
#
#
# # my_com = Comment()
# # print(my_com.__dict__)
#
# my_com = Comment()
# my_com.aaa = 100000
# my_com.addcom(55)
# print(my_com.__dict__)
#
# my_com1 = Comment()
# # my_com1.addcom(999)
# print(my_com1.__dict__)
#
# my_com1.reset_votes()
# print(my_com1.__dict__)
#
# ---------------------------------------------------------------------------------------------

class Image:
    total_change = 0

    def __init__(self):
        self.resolution = '300 * 300'
        self.title = 'cat'
        self.extension = 'jpeg'

    def resize(self, a, b):
        self.resolution = f"{a} * {b}"
        Image.total_change += 1

    def rename(self):
        self.title = input("New name: ")
        Image.total_change += 1

    def up(self):
        self.extension = self.extension.upper()
        Image.total_change += 1

    @staticmethod
    def sum(x, y):
        Image.total_change += 1
        return f"Static method summ is equal {x + y}"


im = Image()
print(im.__dict__)
print(f"It was {Image.total_change} changes in class")

print(Image.sum(3, 11))
print(im.sum(3, 11))
print(Image.sum(3, 11) == im.sum(3, 11))

# im.rename()
im.up()
print(f"It was {Image.total_change} changes in class")

im.resize(200, 500)
print(im.__dict__)

im.resize(1920, 1080)
print(im.__dict__)

print(f"It was {Image.total_change} changes in class")

