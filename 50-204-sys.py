import sys

print(sys.argv)

if len(sys.argv) < 3:
    raise IOError("insert PASS and NAME")
elif sys.argv[2] != 'passs':
    raise IOError('invalid PASSWORD')

user = sys.argv[1]
pas = sys.argv[2]

print(pas, user)
