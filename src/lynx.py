import sys
import json

from lexer import Lexer
import error
from parser import Parser
from interpreter import evaluate
import enviornment
from Token import Token, TokenType
import runtimevalues

def report(error):
    print(error)
    sys.exit(1)

def runFile(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
    except FileNotFoundError:
        report(error.LynxError("Specified file path not found"))

    env = enviornment.createGlobalEnv()

    try:
            tokens = Lexer(contents).tokenize()

            parser = Parser(tokens)
            parser.semiafterexpr = True
            ast = parser.parse()

            #print(json.dumps(ast.dict(), indent=2))


            evaluate(ast, env)

    except error.LynxError as err:
        print(err)
        sys.exit(1)

def repl():
    userin = ""

    env = enviornment.createGlobalEnv()

    while userin != ".exit":
        userin = input("> ")

        try:
            tokens = Lexer(userin).tokenize()

            parser = Parser(tokens)
            parser.semiafterexpr = False
            ast = parser.parse()

            #print(json.dumps(ast.dict(), indent=2))

            result = evaluate(ast, env)
            if hasattr(result, "value"):
                print(result.value)

        except error.LynxError as err:
            print(err)
            continue

def main():
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