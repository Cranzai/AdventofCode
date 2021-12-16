import sys
from collections import deque
import copy

class BITS:
    def __init__(self, input_file):
        with open(input_file, "r") as file:
            self.message = file.readline().rstrip("\n")

        self.hex_bin = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
        }

        self.versionSum = 0
        self.rawValues = []
        self.values = deque()
        self.operators = deque()

    def decode(self):
        self.binary = deque()
        for char in list(self.message):
            for bit in self.hex_bin[char]:
                self.binary.append(bit)

        self.packet(self.binary)

        values = [value for value in self.rawValues]
        self.values.append(values)
        self.values.popleft()

        return

    def operate(self, operator, value_set):
        if operator == 0:
            return sum(value_set)

        if operator == 1:
            product = 1
            for val in value_set:
                product = product * val

            return product

        if operator == 2:
            return min(value_set)

        if operator == 3:
            return max(value_set)

        if operator == 5:
            if value_set[0] > value_set[1]:
                return 1
            
            return 0

        if operator == 6:
            if value_set[0] < value_set[1]:
                return 1
            
            return 0

        if operator == 7:
            if value_set[0] == value_set[1]:
                return 1
            
            return 0


    def packet(self, block):
        #only the source packet has extra 0's, hence if the deck does no longer contain 1 we are done.
        if not '1' in block:
            return

        version = int(''.join([str(block.popleft()) for i in range(3)]), 2)
        self.versionSum += version
        typeID = int(''.join([str(block.popleft()) for i in range(3)]), 2)

        if typeID == 4:
            value = self.literal_value(block)
            self.rawValues.append(value)

        elif typeID != 4:
            self.operators.append(typeID)
            values = [value for value in self.rawValues]
            self.values.append(values)
            self.rawValues = []

            self.operator(block)

        self.packet(block)

    def literal_value(self, block):
        binary = ''
        count = 0
        while block:
            count += 1
            part = ''.join([str(block.popleft()) for i in range(5)])
            binary += part[1:]
            if part[0] == '0':
                break

        return int(binary, 2)

    def operator(self, block):
        field = 15 - 4 * int(block.popleft())
        part = deque()

        if field == 15:
            length = int(''.join([str(block.popleft()) for i in range(field)]), 2)
            for i in range(length):
                part.append(block.popleft())
            
            self.packet(part)

        if field == 11:
            num = int(''.join([str(block.popleft()) for i in range(field)]), 2)            
            self.packet(block)


if __name__ == "__main__":
    message = BITS(sys.argv[1])
    message.decode()
    print(message.versionSum)

    print(message.operators)
    print(message.values)