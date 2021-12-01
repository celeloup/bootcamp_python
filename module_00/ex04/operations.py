import sys


def check_args(args):
    len_arg = len(args)
    if (len_arg == 2):
        try:
            int(args[0])
            int(args[1])
            return (0)
        except ValueError:
            print("InputError: only numbers\n")
    elif (len_arg > 2):
        print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>\n\
Example:\n\tpython operations.py 10 3")
    return 1


if (check_args(sys.argv[1:]) == 0):
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"""Sum:        {num1 + num2}""")
    print(f"""Difference: {num1 - num2}""")
    print(f"""Product:    {num1 * num2}""")
    if (num2 != 0):
        print(f"""Quotient:   {num1 / num2}""")
    else:
        print(f"""Quotient:   ERROR (div by zero)""")
    if (num2 != 0):
        print(f"""Remainder:  {num1 % num2}""")
    else:
        print(f"""Remainder:  ERROR (modulo by zero)""")
