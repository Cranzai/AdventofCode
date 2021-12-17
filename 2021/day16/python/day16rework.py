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

    def decode(self):
        self.binary = deque()
        for char in list(self.message):
            for bit in self.hex_bin[char]:
                self.binary.append(bit)

        answer = []
        self.packet(self.binary, answer, False)

        return answer

    def packet(self, block, values, limit):
        if not '1' in block:
            return values

        version = int(''.join([str(block.popleft()) for i in range(3)]), 2)
        self.versionSum += version
        typeID = int(''.join([str(block.popleft()) for i in range(3)]), 2)

        #operator
        if typeID != 4:
            field = 15 - 4 * int(block.popleft())
            part = deque()

            if field == 15:
                length = int(''.join([str(block.popleft()) for i in range(field)]), 2)
                for i in range(length):
                    part.append(block.popleft())

                opvals = []
                self.packet(part, opvals, False)
                values.append(self.operate(typeID, opvals))


            elif field == 11:
                num = int(''.join([str(block.popleft()) for i in range(field)]), 2)
                
                opvals = []
                for i in range(num):
                    tempvals = []
                    self.packet(block, tempvals, True)
                    opvals.extend(tempvals)

                values.append(self.operate(typeID, opvals))

        #literal value
        elif typeID == 4:
            binary = ''
            while block:
                part = ''.join([str(block.popleft()) for i in range(5)])
                binary += part[1:]
                if part[0] == '0':
                    break

            values.append(int(binary,2))

        if not limit:
            self.packet(block, values, False)
        else:
            return values

    def operate(self, operator, values):
        if operator == 0:
            result = sum(values)

        elif operator == 1:
            result = 1
            for val in values:
                result = result * val

        elif operator == 2:
            result = min(values)

        elif operator == 3:
            result = max(values)

        elif operator == 5:
            result = 0
            if values[0] > values[1]:
                result = 1


        elif operator == 6:
            result = 0
            if values[0] < values[1]:
                result = 1

        elif operator == 7:
            result = 0
            if values[0] == values[1]:
                result = 1
            
        return result

if __name__ == "__main__":
    message = BITS(sys.argv[1])
    print(message.decode())

