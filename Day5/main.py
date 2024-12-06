import sys
import re


def part2f(order, rule_after):
    for i in range(len(order)):
        for j in range(len(order)-1):
            try:
                if(order[j+1] not in rule_after[order[j]]):
                    temp = order[j+1]
                    order[j+1] = order[j]
                    order[j] = temp
            except:
                temp = order[j+1]
                order[j+1] = order[j]
                order[j] = temp
    return order
  


def ordering(order, rule_after):
    rules  = rule_after[order[0]]
    for i in range(len(order)):
        for j in range(i,len(order)-1):
            try:
                if(order[j+1] not in rule_after[order[j]]):
                    return 0,order
            except:
                    return 0,order
    return order[len(order)//2], None
                    

def main():
    grid = []
    part1 = 0
    part2 = 0
    with open(sys.argv[1],"r") as f:
        rule_after = {}
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
            else:
                order = list(map(int,l.strip().split(',')))
                pages.append(order)
    
    bad_pages = []
    for order in pages:
        val,bad_list = ordering(order,rule_after)
        part1 += val
        if(bad_list):
            bad_pages.append(bad_list)

    for pages in bad_pages:
        fixed = part2f(pages,rule_after)
        part2+= fixed[len(fixed)//2]

    print(part1)
    print(part2)


if __name__ ==  "__main__":
    main()
