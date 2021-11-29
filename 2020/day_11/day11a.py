import numpy as np

def evalSeat(row, col, floorPlan):
    
    checks = [(row, col-1),# left
              (row, col+1),# right
              (row+1, col),# below
              (row-1, col),# above
              (row-1, col-1),# left upper
              (row-1, col+1),# right upper
              (row+1, col+1),# right lower
              (row+1, col-1)]# left lower 
    
    maxRow, maxCol = np.shape(floorPlan)
    
    occupied = []
    for check in checks:
        
        if check[0] >= 0 and check[0] < maxRow and check[1] >= 0 and check[1] < maxCol:
            #print(check, floorPlan[check])
            occupied.append(floorPlan[check])

        
    #print(occupied)
    #print(row, col, floorPlan[row, col], occupied.count('#') )
    
    if floorPlan[row, col] == 'L' and occupied.count('#') == 0:
        return '#'
    elif floorPlan[row, col] == '#' and occupied.count('#') > 4:
        return 'L'
    elif floorPlan[row, col] == '.':
        return '.'
    else:
        return floorPlan[row, col]

#=======================================================================================================================

data = open('input.txt', 'r').read().splitlines()

#Create Array
floorPlan = []
for row in data:
    floorPlan.append(list(row))
floorPlan = np.array(floorPlan)

cnt = 0
amount = 0
change = 99
while cnt < 200 :
    
    #print('Starting new iteration')

    tempFloor = np.copy(floorPlan)        
    for iRow, row in enumerate(floorPlan):
        for iCol, col in enumerate(row):
            
            if floorPlan[iRow, iCol] != '.':
            
                seat = evalSeat(iRow, iCol, floorPlan)
                tempFloor[iRow, iCol] = seat
            
    cnt += 1

    floorPlan = np.copy(tempFloor)
    
    newAmount = np.count_nonzero(floorPlan == '#') 
    #change = amount - newAmount
    amount = newAmount
         
    print(amount)        
#    

