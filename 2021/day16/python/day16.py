import sys
from collections import deque

class packet:
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

    def decode(self):
        print('decode')
        self.binary = deque()
        for char in list(self.message):
            for bit in self.hex_bin[char]:
                self.binary.append(bit)
        
        self.packet(self.binary, 0, 0)

    def packet(self, block, value, ops):
        print(block)
        version = int(''.join([str(block.popleft()) for i in range(3)]), 2)
        self.versionSum += version
        typeID = int(''.join([str(block.popleft()) for i in range(3)]), 2)

        if typeID == 4:
            value = self.literal_value(block)
        elif typeID != 4:
            ops = self.operator(block)

        if not block:
            print(value, ops)
            return value, ops

        self.packet(block, value, ops)

    def literal_value(self, block):
        print('value')
        binary = ''

        while block:  
            part = ''.join([str(block.popleft()) for i in range(5)])
            binary += part[1:]
            if part[0] == '0':
                break

        return int(binary, 2)

    def operator(self, block):
        print('operator')
        field = 15 - 4 * int(block.popleft())
        part = deque()

        if field == 15:
            length = int(''.join([str(block.popleft()) for i in range(field)]), 2)
            for i in range(length):
                part.append(block.popleft())
            
            self.packet(part, 0, 0)

        if field == 11:
            num = int(''.join([str(block.popleft()) for i in range(field)]), 2)
            part = block
            for i in range(num):
                self.packet(block, 0, 0)









if __name__ == "__main__":
    part_a = packet(sys.argv[1])
    part_a.decode()