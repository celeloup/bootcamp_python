import sys

MORSE_CODE_DICT = {'A':  '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----'}
code = ""
str = ' '.join(sys.argv[1:]).upper()
for letter in str:
    if (letter != ' ' and letter not in MORSE_CODE_DICT):
        print("ERROR")
        code = ""
        break
    elif (letter == ' '):
        code += '/'
    else:
        code += MORSE_CODE_DICT[letter]
    code += ' '

if (code != ""):
    print(code)
