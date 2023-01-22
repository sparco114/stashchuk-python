lis = [1, 'fff', True, 5.45, [1, 2, 50]]
print(1, lis)

del lis[2]
print(2, lis)

print(3, len(lis))

# lis.sort(reverse=True)
# print(4, lis)

lis.reverse()
print(4, lis)

lis2 = ['ddd', 222]
print(5, lis2)

lis.extend(lis2)
print(6, lis)


