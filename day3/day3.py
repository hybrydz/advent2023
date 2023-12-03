import re

with open('test_input.txt', "r") as file:
    lines = file.read().splitlines()

# with open('input_day3.txt', "r") as file:
#     lines = file.read().splitlines()

GEAR = '*'

def adjFinder(lineIndex:int,symbolIndex:int,symbol:str,inputLines:list,sum:int,gearRatioSum:int):
    gearRatio = []
    # Check same Line
    numbers = re.finditer(r'\d+', inputLines[lineIndex])
    for match in numbers:
        if index in range(match.span()[0]-1,match.span()[1]+1):
            if symbol == GEAR:
                gearRatio.append(int(match.group()))
            sum += int(match.group())
            print(symbol,symbolIndex,match.group(), match.span(), type(match.span()))
    if lineIndex >=1 and lineIndex<len(inputLines)-1:
        numbersAbove = re.finditer(r'\d+', inputLines[lineIndex-1])
        numbersBelow = re.finditer(r'\d+', inputLines[lineIndex+1])
        # Check Line Above
        for match in numbersAbove:
            if index in range(match.span()[0]-1,match.span()[1]+1):
                if symbol == GEAR:
                    gearRatio.append(int(match.group()))
                sum += int(match.group())
                print(symbol,symbolIndex,match.group(), match.span(), type(match.span()))
        # Check Line Below
        for match in numbersBelow:
            if index in range(match.span()[0]-1,match.span()[1]+1):
                if symbol == GEAR:
                    gearRatio.append(int(match.group()))
                sum += int(match.group())
                print(symbol,symbolIndex,match.group(), match.span(), type(match.span()))
    if len(gearRatio) == 2:
        gearRatioSum += gearRatio[0] * gearRatio[1] 
    return sum, gearRatioSum    


sum = 0
gearRatioSum = 0
for lineIndex, line in enumerate(lines):
    for index,item in enumerate(line):
        if item != '.' and not item.isdigit():
            sum,gearRatioSum = adjFinder(lineIndex,index,item,lines,sum,gearRatioSum)

print(sum,gearRatioSum)
