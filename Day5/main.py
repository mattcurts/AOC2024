import sys
import re


def ordering(order, rule_after,rule_before):
    rules  = rule_after[order[0]]
    for i in range(len(order)):
        for j in range(i,len(order)-1):# read forward
            try:
                if(order[j+1] not in rule_after[order[j]]):
                    print("Bad order")
                    print(order)
                    return 0
            except:
                print("Bad order")
                print(order)
                return 0
    print("good order ", order)
    return order[len(order)//2]
                    

def main():
    grid = []
    part1 = 0
    part2 = 0
    with open(sys.argv[1],"r") as f:
        rule_after = {}
        rule_before = {}
        pages = []
        rules = True
        for l in f.readlines():
            if(l == "\n"):
                rules = False
                continue
            if rules:
                l = list(map(int,l.strip().split("|")))
                if  l[0] in rule_after:
                    rule_after[l[0]].append(l[1]) # adding to rule list for value
                else:
                    rule_after[l[0]] =  [l[1]] # first time seeing it
                if  l[1] in rule_before:
                    rule_before[l[1]].append(l[0]) # adding to rule list for value
                else:
                    rule_before[l[1]] =  [l[0]] # first time seeing it
            else:
                order = list(map(int,l.strip().split(',')))
                pages.append(order)
    

    for order in pages:
        part1 += ordering(order,rule_after,rule_before)

            


    print(part1)
    print(part2)

#    for line in grid:
        #print(line)
    #print(part1)
if __name__ ==  "__main__":
    main()
