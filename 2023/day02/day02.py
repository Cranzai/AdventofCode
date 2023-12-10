#function for part A
def ValidHigh(input, red, green, blue):
    file = open(input, "r")

    check = {"red": red, "green": green, "blue":blue}
    valids = []

    for game in file.readlines():
        id, plays = game.strip().split(": ")
        id = int(id.split()[-1])
        plays = plays.split("; ")

        valid = True
        for play in plays:
            if valid == False: break

            for entry in play.split(", "):
                num, col = entry.split(" ")

                if int(num) > check[col]:
                  valid = False

        if valid: valids.append(id)

    return sum(valids)

#part A
print(ValidHigh("day02.inp", 12, 13, 14))

#function for part B
def LowPos(input):
    file = open(input, "r")

    powers = []
    for game in file.readlines():
        _, plays = game.strip().split(": ")
        plays = plays.split("; ")

        highs = {"red": 0, "green": 0, "blue": 0}
        for play in plays:
            for entry in play.split(", "):
                num, col = entry.split(" ")

                if int(num) > highs[col]: highs[col]=int(num)

        powers.append(highs["red"]*highs["green"]*highs["blue"])

    return sum(powers)

print(LowPos("day02.inp"))