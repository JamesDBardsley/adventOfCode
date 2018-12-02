#Advent of code day 1 exercise 1, get calibration

def calibration():
    inFile = open("N:\AdventOfCode\Day1Puzzle1Input.txt", "r")
    total = 0
    for line in inFile:
        total = total + int(line)
    print(total)
    
