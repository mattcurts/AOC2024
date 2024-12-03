import sys
import re

def mul(a,b):
    return a*b

def main():
    with open(sys.argv[1],"r") as f:
        string = f.read()
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)",string)
        matches1 = re.findall(r"mul\(\d+,\d+\)",string)
        total = 0

        for match in matches1:
                total += eval(match)

        print("part 1 ",total)
        total = 0
        add = True
        for match in matches:
            if match.startswith("do()"):
                add = True
            elif match.startswith("don't()"):
                add = False
            elif(match.startswith("mul") and add is True):
                total += eval(match)

    print("part 2 ",total)

if __name__ ==  "__main__":
    main()
