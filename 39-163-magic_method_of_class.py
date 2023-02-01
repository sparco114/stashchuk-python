# class Image:
#     total_change = 0
#
#     def __init__(self, text):
#         self.text = text
#         self.qty = 0
#
#     def adding(self):
#         self.qty += 1
#
#     def __add__(self, other):
#         return {
#             'Text': f"{self.text} {other.text}",
#             'Quantity': self.qty + other.qty,
#         }
#
#     def __eq__(self, other):
#         return True if self.qty == other.qty and self.text == other.text else False
#
#
# im1 = Image('PYTHON')
# im2 = Image('PYTHON')
#
# im1.adding()
# im2.adding()
# # im2.adding()
#
#
# print(im1.qty)
# print(im2.qty)
# print(im1 + im2)
# print(type(im1 + im2))
# print(im1 == im2)
# ---------------------------------------------------------

class CustomList(list):
    def print_length(self):
        print(f"The length of this list is {len(self)}")


lis1 = [1, 3, 5]

cust_lis = CustomList(lis1)

cust_lis.append(777)
cust_lis.insert(2, 111)
print(cust_lis)
cust_lis.print_length()
print(list.__subclasses__())
