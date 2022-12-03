with open("day1.inp") as input:
    maxElf = [0,0,0]
    thisElf = 0
    for line in input.readlines():
        if line.strip() != "":
            thisElf += int(line)
        else:
            maxElf[0]=max(maxElf[0], thisElf)
            maxElf.sort()
            thisElf=0
     
    print(max(maxElf))
    print(sum(maxElf))
