# with open('test_input.txt', "r") as file:
#     lines = file.read().splitlines()

with open('input_day2.txt', "r") as file:
    lines = file.read().splitlines()

# 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
totalSum = 0
sum =0

for line in lines:
    game = line.split()
    gameID = int(game[1].split(':')[0])
    totalSum += gameID
    for i,item in enumerate(game):
        if i<len(game)-1:
            if 'red' in game[i+1] and int(item)>MAX_RED:
                sum += gameID
                break
            elif 'green' in game[i+1] and int(item)>MAX_GREEN:
                sum += gameID
                break
            elif 'blue' in game[i+1] and int(item)>MAX_BLUE:
                sum += gameID
                break
print("First part",totalSum-sum)

powerSum = 0
for line in lines:
    red = 0
    green = 0
    blue = 0
    game = line.split()
    gameID = int(game[1].split(':')[0])
    totalSum += gameID
    for i,item in enumerate(game):
        if i<len(game)-1:
            if 'red' in game[i+1] and int(item) > red:
                red = int(item)
            elif 'green' in game[i+1] and int(item) > green:
                green = int(item)
            elif 'blue' in game[i+1] and int(item) > blue:
                blue = int(item)
        else:
            power = red * green * blue
            # print(red,green,blue, power)
            powerSum += power

print("Second Part",powerSum)