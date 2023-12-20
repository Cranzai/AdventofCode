class CamelCards:
    def __init__(self, game):
        cardValue = {"2":1, "3": 2, "4": 3, "5": 4, "6": 5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
        self.hands = [[sorted(list(map(lambda val: cardValue[val], [*line.split()[0]])), reverse=True), int(line.split()[1])] for line in open(game, "r").readlines()]

    def __find_types(self):
        self.types = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
        for hand in self.hands:
            count = {}
            for card in hand[0]:
                if not card in count.keys():
                    count[card]=1
                elif card in count.keys():
                    count[card]+=1

            counts = sorted(count.values())
            if counts[-1] == 5:         #five of a kind
                self.types[6].append(hand)
            if counts[-1] == 4:         #four of a kind
                self.types[5].append(hand)
            if counts[-1] == 3:         
                if counts[-2] == 2:     #full house
                    self.types[4].append(hand)
                else:                   #three of a kind
                    self.types[3].append(hand)
            if counts[-1] == 2:         
                if counts[-2] == 2:     #two pair
                    self.types[2].append(hand)
                else:                   #one pair
                    self.types[1].append(hand)
            if counts[-1] == 1:         #high card
                self.types[0].append(hand)

        #i suppose this should sort the sublists properly too
        for type, vals in self.types.items():
            if len(vals)>1:
                self.types[type] = sorted(vals, key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))

    def partA(self):
        if not hasattr(self, "types"):
            self.__find_types()

        sum = 0
        rank = 1
        for hand in self.types.values():
            for _, bid in hand:
                sum += bid*rank
                rank +=1

        return sum

day07 = CamelCards("day07.inp")
print(day07.partA())