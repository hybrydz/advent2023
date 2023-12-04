import re

# with open('test_input.txt', "r") as file:
#     lines = file.read().splitlines()

with open('input_day4.txt', "r") as file:
    lines = file.read().splitlines()

winningList = []
myList = []
copies = {}
part1sum = 0
part2sum=0

for lineIndex,line in enumerate(lines):
    card = lineIndex + 1
    if card not in copies.keys():
        copies[card] = 0
    count =0
    myList = line.split('|')[1].split()
    winningList = line.split('|')[0].split(':')[1].split()
    for item in myList:
        if item in winningList:
            count += 1
    if count !=0:
        part1sum += 2**(count-1)
        copies[card] += 1
        for copy in range(1,count+1):
            if card+copy not in copies.keys():
                copies[card+copy] = 0
            copies[card+copy] += copies[card]*1
    else:
        copies[card]+=1
    part2sum += copies[card]

print(part1sum)
print(part2sum)


