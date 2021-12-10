import numpy as np


# Run problem
# -----------

# Create board
with open('input.txt') as f:
    data = f.readlines()

dataNew = []
for row in data:
    row = [int(x) for x in row.strip()]
    dataNew.append(row)
data = np.array(dataNew)

# Search for basins
# -----------------
lowPoints = []
lowVal = []
# Search corners
cornerIdxs = [[0, 0], [-1, 0], [0, -1], [-1, -1]]
adjCorners = [
    [data[0, 1], data[1, 0]], # left Top
    [data[-1, 1], data[-2, 0]], # left bottom
    [data[0, -2], data[1, -1]], # right top
    [data[-1, -2], data[-2, -1]]# right bottom
    ] 
for idx, cornerIdx in enumerate(cornerIdxs):
    row, col = cornerIdx
    adj = np.array(adjCorners[idx])
    if len(adj[adj > data[row, col]]) == 2:
        lowPoints.append(cornerIdx)
        row, col = cornerIdx
        lowVal.append(data[row, col])

# Search top row
icol = 1
topRow = data[0, 1:-1]
for item in topRow:    
    adj = np.array([data[0, icol - 1], data[0, icol + 1], data[1, icol]])
    if len(adj[adj > item]) == 3:
        lowPoints.append([0, icol])
        lowVal.append(data[0, icol])
    icol += 1

# Search bottom
icol = 1
btmRow = data[-1, 1:-1]
for item in btmRow:   
    adj = np.array([
        data[-1, icol - 1],#  left
        data[-1, icol + 1],# right
        data[-2, icol]]# above
    )
    if len(adj[adj > item]) == 3:
        lowPoints.append([-1, icol])
        lowVal.append(data[-1, icol])
    icol += 1
    
# Search left
irow = 1
leftRow = data[1:-1, 0]
for item in leftRow:
    adj = np.array([data[irow - 1, 0], data[irow, 1], data[irow + 1, 0]])
    if len(adj[adj > item]) == 3:
        lowPoints.append([irow, 0])
        lowVal.append(data[[irow, 0]])
    icol += 1

# Search right
irow = 1
rightRow = data[1:-1, -1]
for itemIdx, item in np.ndenumerate(rightRow):   
    adj = np.array([data[irow - 1, -1], data[irow, -2], data[irow + 1, -1]])
    if len(adj[adj > item]) == 3:
        lowPoints.append([irow, -1])
        lowVal.append(data[[irow, -1]])
    icol += 1

# Search centre
irow = 1
centre = data[1:-1, 1:-1]
for row in centre:
    icol = 1
    for item in row:
        adj = np.array([data[irow-1, icol], data[irow+1, icol], data[irow, icol+1], data[irow, icol-1]]) 
        if len(adj[adj > item]) == 4:
            lowPoints.append([irow, icol])
            lowVal.append(data[[irow, icol]])
        icol += 1    
    irow += 1
    

print('lowPoints:', lowPoints)

# Find basins
# -----------

# lowPoints = [[0, 1]]

floorMap = data.copy()
size = []
for lowPoint in lowPoints:
    floorMap = data.copy()
    irow, icol = lowPoint
    
    old = len(floorMap[floorMap < 0])
    
    floorMap[irow, icol] = -1
    while (len(floorMap[floorMap < 0]) - old) > 0:
        
        old = len(floorMap[floorMap < 0])
        
        for irow, row in enumerate(floorMap):
            for icol, col in enumerate(row):
                if floorMap[irow, icol] == -1:
                    print(irow, icol)
                    try:
                        r = max(irow - 1, 0)
                        c = icol
                        if (floorMap[r, c] != 9) and (floorMap[r, c] != -1):
                            floorMap[r, c] = -1
                    except:
                        print('NA')
                    try:
                        r = max(irow + 1, 0)
                        c = icol
                        if (floorMap[r, c] != 9) and (floorMap[r, c] != -1):
                            floorMap[r, c] = -1
                    except:
                        print('NA')
                    try:
                        r = irow
                        c = max(icol - 1, 0)
                        if (floorMap[r, c] != 9) and (floorMap[r, c] != -1):
                            floorMap[r, c] = -1
                    except:
                        print('NA')
                    try:
                        r = irow
                        c = max(icol + 1, 0)
                        if (floorMap[r, c] != 9) and (floorMap[r, c] != -1):
                            floorMap[r, c] = -1                    
                    except:
                        print('NA')
    size.append(len(floorMap[floorMap < 0]))
    
    
size.sort(reverse=True)
answer = 1
for item in size[0:3]:
    answer = answer * item

print('Answer:', answer)


                        
        
        
                    
                    
                    
                    
        




