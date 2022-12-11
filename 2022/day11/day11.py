import copy

class monkey:
    def __init__(self, items=[], operation="old", crit=0, true=0, false=0):
        self.items = items
        self.op = operation
        self.crit = crit
        self.true = true
        self.false = false
        self.inspects = 0

    def inspect(self, worry):
        self.inspects += 1
        return eval(self.op.replace("old", str(worry)))

    def test(self, worry, bored):
        new = self.inspect(worry)
        if bored: new = int(new / 3)
        if new % self.crit == 0:
            return self.true, new
        else:
            return self.false, new

def rounds(monkeys, num, bored=True):
    for _ in range(num):
        for monkey in monkeys:
            for item in monkey.items:
                target, newitem = monkey.test(item, bored)
                monkeys[target].items.append(newitem)

            monkey.items = []
        
    one, two = sorted([monkey.inspects for monkey in monkeys])[-2:]
    return one*two


with open("day11.inp") as input:
    #Parse and generate list of monkeys
    monkeys = []
    for line in input.readlines():
        line = line.strip()
        try:
            info, content = line.split(":")
        except:
            info = ""
            content = ""

        if info[:6] == "Monkey":
            monkeys.append(monkey())

        if info == "Starting items":
            monkeys[-1].items = list(map(str.strip, content.split(",")))

        if info == "Operation":
            monkeys[-1].op = content.split("=")[-1].strip()

        if info == "Test":
            monkeys[-1].crit = int(content.split(" ")[-1])

        if info == "If true":
            monkeys[-1].true = int(content.split(" ")[-1])

        if info == "If false":
            monkeys[-1].false = int(content.split(" ")[-1])

    #Rounds
    monkeys2 = copy.deepcopy(monkeys)
    print("Part A: ", rounds(monkeys, 20))
    print("Part B: ", rounds(monkeys2, 1000, False))
