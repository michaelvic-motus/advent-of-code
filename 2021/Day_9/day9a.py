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

print(data)


# Search for lowpoints
# --------------------
score = 0

# Search corners
corners = [data[0, 0], data[-1, 0], data[0, -1], data[-1,-1]]
adjCorners = [
    [data[0, 1], data[1, 0]], # left Top
    [data[-1, 1], data[-2, 0]], # left bottom
    [data[0, -2], data[1, -1]], # right top
    [data[-1, -2], data[-2, -1]]# right bottom
    ] 

for idx, item in enumerate(corners):
    adj = np.array(adjCorners[idx])
    if len(adj[adj > item]) == 2:
        print(item)
        score += 1 + item
        #print(idx, corner, score)

# Search top row
icol = 1
topRow = data[0, 1:-1]
for item in topRow:    
    adj = np.array([data[0, icol - 1], data[0, icol + 1], data[1, icol]])
    if len(adj[adj > item]) == 3:
        print(item)
        score += 1 + item
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
        print(item)
        score += 1 + item
    icol += 1
    
# Search left
icol = 1
leftRow = data[1:-1, 0]
for item in leftRow:   
    adj = np.array([data[icol - 1, 0], data[icol, 1], data[icol + 1, 0]])
    if len(adj[adj > item]) == 3:
        print(item)
        score += 1 + item
    icol += 1

# Search right
icol = 1
rightRow = data[1:-1, -1]
for item in rightRow:   
    adj = np.array([data[icol - 1, -1], data[icol, -2], data[icol + 1, -1]])
    if len(adj[adj > item]) == 3:
        print(item)
        score += 1 + item
    icol += 1

# Search centre
irow = 1
centre = data[1:-1, 1:-1]
for row in centre:
    icol = 1
    for item in row:
        adj = np.array([data[irow-1, icol], data[irow+1, icol], data[irow, icol+1], data[irow, icol-1]]) 
        if len(adj[adj > item]) == 4:
            print(item)
            score += 1 + item

        icol += 1    
    irow += 1
    


print('Score:', score)
