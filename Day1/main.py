def main():
    with open("input","r") as f:
        line = f.readline()
        left = []
        right = []
        while(line):
            x,y = line.strip().split()
            left.append(x)
            right.append(y)
            line = f.readline()
            print(line)
        left = list(map(int,left))
        right = list(map(int,right))
        left.sort()
        right.sort()

        total = 0
        for l,r in zip(left,right):
            total += abs(l-r)

        sim_score = 0
        count = {}
        for l in left:
            count[l] = 0

        for r in right:
            try:
                count[r]+=1
            except:
                pass
        for key,val in count.items():
            sim_score+= (key*val)

        print("total ", total)
        print("sim_score ", sim_score)
        return 0

if __name__ ==  "__main__":
    main()
