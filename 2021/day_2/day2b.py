with open('input.txt') as f:
    data = f.readlines()

aim = 0
loc = [0, 0]
for move in data:
    move = move.split(' ')
    direction = move[0]
    value = float(move[1])

    if direction == 'forward':
        loc[0] += value
        loc[1] += aim * value 
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    
print(loc[0] * loc[1])
    
