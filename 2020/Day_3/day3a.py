
#TODO: swap row and col, its confusing!

def slopeCalculator(trackFile, move):

    with open(trackFile, 'r') as file:
        track = file.readlines()
        
    for i, line in enumerate(track):
        track[i] = line.replace('\n', '')
        
    #move = (1, 3)

    trackLen = len(track)
    trackWidth = len(track[0])

    for row in track:
        print(row)
        
    print('\n')

    currentLoc = [0, 0]
    cnt = 0
    while currentLoc[0] < trackLen: # execute another move
        
        char = track[currentLoc[0]][currentLoc[1]]
        print(currentLoc, char)
        
        if char == '#':
            cnt += 1
        
        currentLoc[0] += move[0]
        currentLoc[1] = (currentLoc[1] + move[1])%trackWidth    

    print('\n', cnt)    

    return cnt

track1 = slopeCalculator('track.txt', (1, 1))
track2 = slopeCalculator('track.txt', (1, 3))
track3 = slopeCalculator('track.txt', (1, 5))
track4 = slopeCalculator('track.txt', (1, 7))
track5 = slopeCalculator('track.txt', (2, 1))

answer = track1*track2*track3*track4*track5
print(answer)