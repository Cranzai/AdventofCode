def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def prioritize(char):
    return ord(char)-96 if char.islower() else ord(char)-38

with open("day3.inp") as input:
    partA = 0
    partB = 0
    for group in chunker(input.readlines(), 3):
        #PART A
        for line in group:
            line = line.strip()
            partA += prioritize(next(iter(set(line[:len(line)//2])&set(line[len(line)//2:]))))

        #PART B
        partB += prioritize(next(iter(set(group[0].strip())&set(group[1].strip())&set(group[2].strip()))))

    print(partA)
    print(partB)
