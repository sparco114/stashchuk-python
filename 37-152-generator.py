from sys import getsizeof

gen = (a * a for a in range(1_000_000))

for eee in gen:
    print(eee)
    if eee > 100:
        break

print("Generator size:", getsizeof(gen))
lis = list(gen)
print("List size:", getsizeof(lis))

