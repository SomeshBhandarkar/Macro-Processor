from instructionRecognizer import instructionRecognizer
import re
import tables as t
import os


def main():
    if os.path.exists("output.txt"):
        os.remove("output.txt")

    file = open("input.txt", "r")
    file_content = file.read()
    token = file_content.split("\n")
    file.close()                        

    for i in token:
        delimiters = " ",",","+"
        regPat = '|'.join(map(re.escape, delimiters))
        token = re.split(regPat, i)
        instructionRecognizer(token)

    print("\nMacro Definition Table:")
    t.printMDT()
    print("\nMacro Name Table:")
    t.printMNT()
    print("\nArguments List:")
    t.printArguments()


if __name__ == '__main__':
    main() 