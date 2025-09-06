from lexer import Lexer
import error

import sys

def report(error):
    print(error)
    sys.exit(1)

def runFile():
    pass

def repl():
    userin = ""
    while userin != ".exit":
        userin = input("> ")

        lexer = Lexer(userin)
        try:
            tokens = lexer.tokenize()
        except error.LynxError as err:
            print(err)
            continue
        

        print(tokens)

def main():
    if len(sys.argv) > 1:
        report(error.LynxError("Incorrect Usage, correct usage: lynx [script]"))
    elif len(sys.argv) == 2:
        pass
        # run script
    else:
        repl()

if __name__ == "__main__":
    main()