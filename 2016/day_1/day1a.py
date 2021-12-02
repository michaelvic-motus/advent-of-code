
with open('input.txt') as f:
    puzzle = f.readlines()[0]
puzzle = puzzle.split(', ')

#puzzle = test3

headings = ['N', 'E', 'S', 'W']
heading = 'N'
location = [0,0]

for action in puzzle:

    print(heading, end = ' ')
    print(location, end = ' ')
    # Align

    print(action, end = ' ')

    if action[0] == 'R':
        heading = headings[(headings.index(heading) + 1) % 4]
    elif action[0] == 'L':
        heading = headings[(headings.index(heading) - 1) % 4]
    print(heading, end = ' ')

    # Walk
    if heading == 'N':
        location[1] += int(action[1])
    elif heading == 'E':
        location[0] += int(action[1])
    elif heading == 'S':
        location[1] -= int(action[1])
    elif heading == 'W':
        location[0] -= int(action[1])
    
    print(location)

distance = abs(location[0]) + abs(location[1])
print('distance:', distance)