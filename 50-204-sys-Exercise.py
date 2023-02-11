import sys
from array import array

if sys.argv[1] == 'new.bin':
    with open('new.bin', 'rb') as new:
        unpack = array('i')
        unpack.fromfile(new, 5)
        print(unpack)
