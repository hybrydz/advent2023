# with open('test_input.txt', "r") as file:
#     lines = file.read().splitlines()

with open('input_day1.txt', "r") as file:
    lines = file.read().splitlines()

sum = 0 
for line in lines:
    calibrationValue = ''
    for char in line:
        if char.isdigit():
            calibrationValue +=char
            break
    for char in line[::-1]:
        if char.isdigit():
            calibrationValue +=char
            break
    sum += int(calibrationValue)

print("First Part",sum)



sum = 0
validDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in lines:
    calibrationValue = ''
    firstIndex = -1
    lastIndex = -1
    firstDigit = 0
    lastDigit = 0
    for digit in validDigits:
        if digit in line:
            if line.index(digit) == line.rfind(digit):
                index = line.index(digit)
                if firstIndex == -1 and lastIndex ==-1:
                    firstIndex = index
                    firstDigit = validDigits.index(digit)+1
                elif index<firstIndex:
                    if index >lastIndex:
                        lastIndex = firstIndex
                        lastDigit = firstDigit
                    firstIndex = index
                    firstDigit = validDigits.index(digit)+1
                elif index > firstIndex and index > lastIndex:
                    lastIndex = index
                    lastDigit = validDigits.index(digit)+1
            else:
                index = line.index(digit)
                lastOccurence = line.rfind(digit)
                # print(firstDigit,lastDigit, firstIndex,lastIndex,index, lastOccurence)
                if firstIndex == -1 and lastIndex ==-1:
                    firstIndex = index
                    firstDigit = validDigits.index(digit)+1
                    lastIndex = lastOccurence
                    lastDigit = firstDigit
                    # print(firstDigit,lastDigit)
                elif index<firstIndex:
                    if index >lastIndex:
                        lastIndex = firstIndex
                        lastDigit = firstDigit
                    if lastOccurence >lastIndex:
                        lastIndex = lastOccurence
                        lastDigit = validDigits.index(digit)+1
                    firstIndex = index
                    firstDigit = validDigits.index(digit)+1
                elif lastOccurence > firstIndex and lastOccurence > lastIndex:
                    lastIndex = lastOccurence
                    lastDigit = validDigits.index(digit)+1
    for i,char in enumerate(line):
        if char.isdigit():
            if i < firstIndex or firstIndex == -1:
                if lastIndex == -1:
                    lastIndex = firstIndex
                    lastDigit = firstDigit
                firstIndex = i
                firstDigit = char
            if i > lastIndex:
                lastIndex = i
                lastDigit = char
    if lastIndex == -1:
        lastDigit = firstDigit
    calibrationValue = str(firstDigit)+str(lastDigit)
    sum += int(calibrationValue)
    # print(calibrationValue)

print("Second Part", sum)


