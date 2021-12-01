import sys
import string

if (len(sys.argv) == 3):
    try:
        n = int(sys.argv[2])
        s = [x for x in sys.argv[1] if x not in string.punctuation]
        s = ''.join(s)
        tab = [x for x in s.split(' ') if len(x) > n]
        print(tab)
    except ValueError:
        print("ERROR")
else:
    print("ERROR")
