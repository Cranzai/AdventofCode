shape = {"X":1, "Y":2, "Z":3}
outcome = {"A X":3, "A Y":6, "A Z":0,
           "B X":0, "B Y":3, "B Z":6,
           "C X":6, "C Y":0, "C Z":3}
play = {"A X":"A Z", "A Y":"A X", "A Z":"A Y",
        "B X":"B X", "B Y":"B Y", "B Z":"B Z",
        "C X":"C Y", "C Y":"C Z", "C Z":"C X"}

with open("day2.inp") as input:
    pointsA = 0
    pointsB = 0
    for line in input.readlines():
        pointsA += shape[(line.strip()).split(" ")[-1]]+outcome[line.strip()]
        pointsB += shape[play[line.strip()].split(" ")[-1]]+outcome[play[line.strip()]]

    print("Part A", pointsA)
    print("Part B", pointsB)
