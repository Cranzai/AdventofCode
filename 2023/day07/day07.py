class CamelCards:
    def __init__(self, game, part):
        self.part = part
        if self.part == "A":
            cardValue = {"2":1, "3": 2, "4": 3, "5": 4, "6": 5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
            self.hands = [[list(map(lambda val: cardValue[val], [*line.split()[0]])), int(line.split()[1])] for line in open(game, "r").readlines()]
            self.__winnings()
        
        elif self.part == "B":
            cardValue = {"J":1, "2":2, "3": 3, "4": 4, "5": 5, "6": 6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}
            self.hands = [[list(map(lambda val: cardValue[val], [*line.split()[0]])), int(line.split()[1])] for line in open(game, "r").readlines()]
            self.__winnings()

    def __find_types(self):
        self.types = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
        for hand in self.hands:
            count = {}
            for card in hand[0]:
                if not card in count.keys():
                    count[card]=1
                elif card in count.keys():
                    count[card]+=1

            if not 1 in count.keys():
                count[1] = 0

            if self.part == "B":
                for key in count.keys():
                    if not key == 1:
                        print(count[1])
                        count[key] += count[1]


            counts = sorted(count.values())
            if counts[-1] == 5:         #five of a kind
                self.types[6].append(hand)
            elif counts[-1] == 4:         #four of a kind
                self.types[5].append(hand)
            elif counts[-1] == 3:     
                second = counts[-2] - count[1] if self.part == "B" else counts[-2]    
                if second == 2:     #full house
                    self.types[4].append(hand)
                else:                   #three of a kind
                    self.types[3].append(hand)
            elif counts[-1] == 2:
                second = counts[-2] - count[1] if self.part == "B" else counts[-2]             
                if second == 2:     #two pair
                    self.types[2].append(hand)
                else:                   #one pair
                    self.types[1].append(hand)
            elif counts[-1] == 1:         #high card
                self.types[0].append(hand)


        #i suppose this should sort the sublists properly too
        for type, vals in self.types.items():
            if len(vals)>1:
                self.types[type] = sorted(vals, key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))

    def __winnings(self):
        if not hasattr(self, "types"):
            self.__find_types()

        self.sum = 0
        rank = 1
        for hand in self.types.values():
            for _, bid in hand:
                self.sum += bid*rank
                rank +=1

print("A: ", CamelCards("day07.inp", "A").sum)
print("B: ", CamelCards("day07.inp", "B").sum)