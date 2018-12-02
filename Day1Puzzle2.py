#Advent of Code day 1 puzzle 2

def main():
    #inFile = open("N:\AdventOfCode\Day1Puzzle1Input.txt", "r")
    totalList = [] 
    total = 0
    gotAnswer = False
    iterations = 0
    while gotAnswer == False:
        inFile = open("N:\AdventOfCode\Day1Puzzle2Input.txt", "r")
        for line in inFile:
            line = int(line)
            total = total + line
            #print(total)
            if total in totalList:
                print(total)
                gotAnswer = True
                break
            else:
                totalList.append(total)
        iterations = iterations + 1
        print(iterations, "iterations")
        inFile.close()