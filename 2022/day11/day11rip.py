with open("day11.inp", "r") as file:
    data = file.read().split('\n\n')
    monkeys1 = {}
    monkeys2 = {}
    for e, monkey in enumerate(data):
        monkey = monkey.splitlines()[1:]
        items = [int(x) for x in monkey[0].split(": ")[1].split(", ")]
        operation = lambda x, y: (x + (int(y[1]) if y[1].isdigit() else x)) if y[0] == "+" else (x * (int(y[1]) if y[1].isdigit() else x))
        test = lambda x, y: [y[1], y[0]][not x % y[2]]
        op = monkey[1].split(" ")[-2:]
        z = [int(monkey[3].split(" ")[-1]), int(monkey[4].split(" ")[-1]), int(monkey[2].split(" ")[-1])]
        monkeys1[e] = {"i" : items, "o" : operation, "t" : test, "op" : op, "bool" : z}
        monkeys2[e] = {"i" : items[:], "o" : operation, "t" : test, "op" : op[:], "bool" : z[:]}

    mod = 1
    for e in monkeys1:
        mod *= monkeys1[e]["bool"][-1]

    inspects1 = {e : 0 for e in monkeys1}
    inspects2 = {**inspects1}
    for x in range(10000):
        for i, monkeys, inspects in [(0, monkeys1, inspects1), (1, monkeys2, inspects2)]:
            if (x < 20 and i == 0) or i == 1:
                for e, monkey in monkeys.items():
                    while monkey["i"]:
                        inspects[e] += 1
                        item = monkey["i"].pop(0)
                        item = monkey["o"](item, monkey["op"])
                        item = item // 3 if not i else item % mod
                        monkeys[monkey["t"](item, monkey["bool"])]["i"].append(item)
    p1 = sorted(inspects1.values())
    p2 = sorted(inspects2.values())
    print("Day 11: ", p1[-2] * p1[-1], p2[-2] * p2[-1])
