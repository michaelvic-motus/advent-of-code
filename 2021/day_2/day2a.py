with open('input.txt') as f:
    data = f.readlines()

loc = [0, 0]
for move in data:
    move = move.split(' ')
    direction = move[0]
    value = float(move[1])

    if direction == 'forward':
        loc[0] += value 
    elif direction == 'down':
        loc[1] += value
    elif direction == 'up':
        loc[1] -= value
        
    print(direction, value)
    
print(loc)
print(loc[0] * loc[1])
    
    