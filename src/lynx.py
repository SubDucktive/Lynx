import sys
import json

from lexer import Lexer
import error
from parser import Parser
from interpreter import evaluate

def report(error):
    print(error)
    sys.exit(1)

def runFile(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
    except FileNotFoundError:
        report(error.LynxError("Specified file path not found"))

    tokens = Lexer(contents).tokenize()
    ast = Parser(tokens).parse()

    print(json.dumps(ast.dict(), indent=3))

def repl():
    userin = ""
    while userin != ".exit":
        userin = input("> ")

        try:
            tokens = Lexer(userin).tokenize()
            ast = Parser(tokens).parse()
            
            result = evaluate(ast)
            if hasattr(result, "value"):
                print(result.value)

        except error.LynxError as err:
            print(err)
            continue

def main():
    print(sys.argv)
    if len(sys.argv) > 2:
        report(error.LynxError("Incorrect Usage, correct usage: lynx [script]"))
    elif len(sys.argv) == 2:
        try:
            runFile(sys.argv[1])
        except error.LynxError as err:
            report(err)
    else:
        repl()

if __name__ == "__main__":
    main()