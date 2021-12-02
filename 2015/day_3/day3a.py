# Tests
tests = []
tests.append('>')
tests.append('^>v<')
tests.append('^v^v^v^v^v')


# Puzzle input
with open('puzzle_input.txt') as file:
    moves = file.readlines()


for run in moves:
    # Define origin
    x = 0; y = 0
    # Apply movements
    locations = ['00']
    for move in run:
        if move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        
        locations.append(f'{x}{y}')
 
    print(len(set(locations)))


