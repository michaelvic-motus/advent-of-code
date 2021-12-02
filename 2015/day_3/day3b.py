# Tests

def findHouses(path):
    x = 0; y = 0# Define origin Santa

    # Apply movements
    locations = ['00']
    for move in path:
        if move == '>':
            x += 1
        elif move == '<':
            x -= 1
        elif move == '^':
            y += 1
        elif move == 'v':
            y -= 1
            
        locations.append(f'{x}{y}')
        
    return locations

#===============================================================================

if __name__ == '__main__':
    
    # Tests
    # -----
    
    # Test 1
    path = '^v'
    pathSanta = [x for i, x in enumerate(path) if i%2 == 0]
    print('moves Santa:', pathSanta)
    pathRobot = [x for i, x in enumerate(path) if i%2 != 0]
    print('moves Robot:', pathRobot)
    locations = findHouses(pathSanta) + findHouses(pathRobot)
    print(locations)
    assert len(set(locations)) == 3, f'Answer: {len(set(locations))} Fail test 1'
    print('Pass test 1')
     
    # Test 2
    path = '^>v<'
    pathSanta = [x for i, x in enumerate(path) if i%2 == 0]
    print('moves Santa:', pathSanta)
    pathRobot = [x for i, x in enumerate(path) if i%2 != 0]
    print('moves Robot:', pathRobot)
    locations = findHouses(pathSanta) + findHouses(pathRobot)
    assert len(set(locations)) == 3, 'Fail test 2'
    print('Pass test 2')
 
    # Test 3
    path = '^v^v^v^v^v'
    pathSanta = [x for i, x in enumerate(path) if i%2 == 0]
    print('moves Santa:', pathSanta)
    pathRobot = [x for i, x in enumerate(path) if i%2 != 0]
    print('moves Robot:', pathRobot)
    locations = findHouses(pathSanta) + findHouses(pathRobot)
    assert len(set(locations)) == 11, 'Fail test 2'
    print('Pass test 3')


    # Puzzle input
    # ------------

    with open('puzzle_input.txt') as file:
        path = file.readlines()[0]

    locations = findHouses(path[0::2]) + findHouses(path[1::2])
    print('Answer:', len(set(locations)))


    




    # Not working yet