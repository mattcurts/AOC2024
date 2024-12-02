f = open("input","r")
line = f.readline()
left = []
right = []
while(line):
    x,y = line.strip().split()
    left.append(x)
    right.append(y)
    line = f.readline()
    print(line)
left.sort()
right.sort()

total = 0
for l,r in zip(left,right):
    total += abs(int(l)-int(r))

sim_score = 0
map = {}
for l in left:
    map[l] = 0

for r in right:
    try:
        map[r]+=1
    except:
        pass
for key,val in map.items():
    sim_score+= (int(key)*int(val))

print("total ", total)
print("sim_score ", sim_score)
