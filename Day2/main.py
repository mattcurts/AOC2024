def compare(dif):
    for d in dif:
        if(abs(d) > 3 or abs(d) == 0):
        #print("dif ", nums, not_safe)
            return False

    increase = [d for d in dif if d > 0]
    decrease = [d for d in dif if d < 0]
    if((len(decrease) != 0 or len(increase) == 0) and (len(decrease) == 0 or len(increase) != 0)):
        return False

    return True

import sys
f = open(sys.argv[1],"r")
line = f.readline()
part1 = 0
part2 = 0
safe = False
while(line):
    nums = list(map(int,line.split()))
    dif = [nums[i] - nums[i-1] for i in range(len(nums))]
    dif = dif[1:]
    if(compare(dif) != True):
        for i in range(len(nums)):
            nums1 = [nums[j] for j in range(len(nums)) if j != i]
            dif1 = [nums1[j] - nums1[j-1] for j in range(len(nums1))]
            dif1 = dif1[1:]
            if(compare(dif1)):
                safe = True
                break
    else:
        safe = True
        part1 +=1

    if(safe):
        part2 += 1
    line = f.readline()
    safe = False

print(part1, part2)
