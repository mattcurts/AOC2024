import sys
import re

def find_in_x(grid):
    count = 0
    for i in range(len(grid)-2):
        for j in range(len(grid[i])-2):
            sub_grid = []
            for k in range(3):
                sub_grid.append(grid[i+k][j:j+3])
            if(sub_grid[0][0] == "M" and sub_grid[1][1] == "A" and sub_grid[0][2] == "S" and
               sub_grid[2][0] == "M" and sub_grid[1][1] == "A" and sub_grid[2][2] == "S"):
                count+=1
            elif(sub_grid[0][0] == "S" and sub_grid[1][1] == "A" and sub_grid[0][2] == "M" and
               sub_grid[2][0] == "S" and sub_grid[1][1] == "A" and sub_grid[2][2] == "M"):
                count+=1
            elif(sub_grid[0][0] == "M" and sub_grid[1][1] == "A" and sub_grid[0][2] == "M" and
                sub_grid[2][0] == "S" and sub_grid[1][1] == "A" and sub_grid[2][2] == "S"):
                count+=1
            elif(sub_grid[0][0] == "S" and sub_grid[1][1] == "A" and sub_grid[0][2] == "S" and
                sub_grid[2][0] == "M" and sub_grid[1][1] == "A" and sub_grid[2][2] == "M"):
                count+=1
    return count

def find_in_diag(grid):
    count = 0
    for i in range(len(grid)-3):
        for j in range(len(grid[i])-3):
            sub_grid = []
            for k in range(4):
                sub_grid.append(grid[i+k][j:j+4])
            if(sub_grid[0][0] == "X" and sub_grid[1][1] == "M" and sub_grid[2][2] == "A" and sub_grid[3][3] == "S"):
                count+=1
            elif(sub_grid[0][0] == "S" and sub_grid[1][1] == "A" and sub_grid[2][2] == "M" and sub_grid[3][3] == "X"):
                count+=1
    return count

def find_in_row(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(0,len(grid[i])):
            if("".join(grid[i][j:j+4]) == "XMAS"):
                count +=1
            elif("".join(grid[i][j:j+4]) == "SAMX"):
                count +=1
    return count

def main():
    grid = []
    part1 = 0
    part2 = 0
    with open(sys.argv[1],"r") as f:
        line = f.read().split()
        for l in line:
            grid.append(list(l))
    count = 0
    part1+= find_in_row(grid)
    trans = list(map(list, zip(*grid)))
    part1 += find_in_row(trans)
    part1 += find_in_diag(grid)
    part2 += find_in_x(grid)
    for row in grid:
        row.reverse()
    part1 += find_in_diag(grid)
    print(count)
    print(part1)
    print(part2)

#    for line in grid:
        #print(line)
    #print(part1)
if __name__ ==  "__main__":
    main()
