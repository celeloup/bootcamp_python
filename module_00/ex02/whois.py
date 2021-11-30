import sys

if (len(sys.argv) == 2) and sys.argv[1].isnumeric():
    if (int(sys.argv[1]) == 0):
        print("I'm Zero.")
    else:
        print("I'm Odd." if int(sys.argv[1]) % 2 != 0 else "I'm Even.")
elif (len(sys.argv) != 1):
    print("ERROR")
