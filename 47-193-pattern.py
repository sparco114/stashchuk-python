import re

me = "My name is Anton. And he is Anton."

res = re.search(r'Anton\.', me)
print(res)
res1 = re.findall(r'Anton\.', me)
print(res1)


pattern = re.compile(r'Anton\.')
print(pattern)
print(pattern.findall(me))

print(res.span())
print(res.start())
print(res.end())


print('Anton\n!!!')
print(r'Anton\n!!!')
print(rf'Anton\n!!! {me}')

