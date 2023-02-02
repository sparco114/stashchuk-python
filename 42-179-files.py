from pathlib import Path

# # Он учил писать так:
# here = Path('.') / 'files'

# Но работает и такЖ
here = Path('./files')

if not here.exists():
    here.mkdir()

# Можно так:
with open('./files/first.txt', 'w') as first:
    first.write('aaaaaaaaaaaaaaa\n')
    first.write('bbbbbbbbbbbbbbb\n')
    first.write('ccccccccccccccc\n')

# А можно так, но тогда в конце нужно закрывать файл, с которым работал
second = open('./files/second.txt', 'w')
second.write('xxx\n')
second.write('yyy\n')
second.write('zzz\n')
second.close()

with open('./files/first.txt') as first:
    print(first.read())

with open('./files/first.txt') as first:
    print(first.readlines())

second = open('./files/second.txt')
for line in second:
    print(line.upper())
second.close()

with open('./files/first.txt') as first:
    while True:
        line = first.readline()
        if line:
            print(line)
        else:
            break

f1 = Path('./files/first.txt')
f2 = Path('./files/second.txt')
d = Path('./files')

if f1.exists():
    f1.unlink()
if f2.exists():
    f2.unlink()
if d.exists():
    d.rmdir()
