import sys, getopt
import numpy as np

def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:')
    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt == '-i':
            inputFile = arg

    bingoDraw, bingoCharts = bingoReader(inputFile)

    winner, winNum = bingoPlayWin(bingoDraw, bingoCharts)
    print(winner, winNum)

    remSum=0
    for line in bingoCharts[winner]:
        for num in line:
            if isinstance(num, int): remSum += num

    print(remSum*winNum)

    loser, loseNum = bingoPlayLose(bingoDraw, bingoCharts)
    print(loser, loseNum)

    remSum = 0
    for line in bingoCharts[loser]:
        for num in line:
            if isinstance(num, int): remSum += num

    print(remSum*loseNum)


def bingoReader(inputFile):
    with open(inputFile, "r") as fileIn:
        bingoCharts = []
        readChart = []
        for lineNum, line in enumerate(fileIn):
            if lineNum == 0:
                bingoDraw = (line.rstrip("\n")).split(",")
                #convert to integers
                bingoDraw = [int(i) for i in bingoDraw]
            elif line == "\n" and readChart != []:
                bingoCharts.append(readChart)
                readChart = []
            elif line != "\n":
                intLine = [int(i) for i in line.split()]
                readChart.append(intLine)

        #save last read chart into bingoCharts
        if readChart != []:
            bingoCharts.append(readChart)

    return bingoDraw, bingoCharts

def bingoPlayWin(bingoDraw, bingoCharts):
    for numDraw in bingoDraw:
        for chart in bingoCharts:
            for line in chart:
                for pos, numLine in enumerate(line):
                    if numLine == numDraw: line[pos]="x"

        #assuming square bingo charts
        #no support for simultaneous winners
        for chartNum, chart in enumerate(bingoCharts):
            dim = len(chart)

            for i in range(dim):
                xCountRow = 0
                xCountCol = 0
                for j in range(dim):
                    #rows, chart[i][j]
                    if(chart[i][j]=="x"): xCountRow += 1
                    #columns, chart[j][i]
                    if(chart[j][i]=="x"): xCountCol += 1

                if xCountRow == dim or xCountCol == dim:
                    return chartNum, numDraw

def bingoPlayLose(bingoDraw, bingoCharts):
    playing = list(range(len(bingoCharts)))
    winners = []
    for numDraw in bingoDraw:
        for player in playing:
            for line in bingoCharts[player]:
                for pos, numLine in enumerate(line):
                    if numLine == numDraw: line[pos]="x"

        for player in playing:
            dim = len(bingoCharts[player])
            chart=bingoCharts[player]

            for i in range(dim):
                xCountRow = 0
                xCountCol = 0
                for j in range(dim):
                    #rows, chart[i][j]
                    if(chart[i][j]=="x"): xCountRow += 1
                    #columns, chart[j][i]
                    if(chart[j][i]=="x"): xCountCol += 1

                if xCountRow == dim or xCountCol == dim:
                    winners.append(player)
                    lastNum = numDraw

        for winner in winners:
            if len(playing) != 1:
                if winner in playing: playing.remove(winner)
            else:
                return winner, lastNum

        winners = []




if __name__ == "__main__":
    main(sys.argv[1:])