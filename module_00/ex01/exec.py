import sys

if (len(sys.argv) > 1):
    str_list = list(filter(None, sys.argv))
    args = ' '.join(str_list[1:])
    print(args[::-1].swapcase())
