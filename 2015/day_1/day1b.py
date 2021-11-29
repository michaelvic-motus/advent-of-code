
with open('directions.txt', 'r') as file:
    directions = file.readlines()
    
floor = 0

for i, val in enumerate(directions[0]):
    if val == '(':
        floor += 1
    elif val == ')':
        floor -= 1
    else:
        print('Unknown character in directions')
        
    if floor < 0:
        print(i + 1)
        break



