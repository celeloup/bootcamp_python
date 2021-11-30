import sys

if (len(sys.argv) > 1):
    args = ' '.join(sys.argv[1:])
    print(args[::-1].swapcase())
