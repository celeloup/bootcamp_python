import sys
import string


def text_analyser(*args):
    """A function to analyze a text by counting its upper characters, \
lower characters, punctuation and spaces."""

    if (len(args) > 1):
        print("ERROR")
        return
    elif (len(args) == 0):
        print("What is the text to analyze ?")
        text = input()
    else:
        text = args[0]
        print(f"""Text to analyze:\n\"{text}\"\n""")
    lower = 0
    upper = 0
    punctuation = 0
    spaces = 0
    for c in text:
        if c == ' ':
            spaces += 1
        elif c in string.punctuation:
            punctuation += 1
        elif c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    print("The text contains {} characters:\n- {} upper letters\n\
- {} lower letters\n- {} punctuation marks\n- {} spaces"
          .format(len(text), upper, lower, punctuation, spaces))


text_analyser()
