def findMarker(stream, length):
    mark = stream[:length]
    if not len(set(mark))==length:
        for i, char in enumerate(stream[length:], start=length+1):
            mark = mark[1:]+char
            if len(set(mark))==length:
                return i
                break
    else:
        return length

with open("day6.inp") as input:
    stream = input.readline().strip()
    print(findMarker(stream, 4))
    print(findMarker(stream, 14))
